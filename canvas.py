#CobraSketch
#by Andrew Sheldon, Chris Neveu, Ryan Darge, and Collin McAloon

from pyglet import *
from collections import deque

from action import Action
from brush import Brush
from history import History
from layer import Layer
from stroke import Stroke



class Canvas:
    '''Canvas Class'''
    width = int
    height = int
    referenceX = int
    referenceY = int
    windowWidth = int
    windowHeight = int
    

    layers = []
    order = []
    
    name = ""
    filepath = "unnamed.cobra"
    
    def __init__(self, width, height, name, path):
        '''Constructor'''

        #Get size from parent
        self.width = width
        self.height = height

        self.name = name
        self.filepath = path

        self.referenceX = 0
        self.referenceY = 0
        self.windowWidth = 800
        self.windowHeight = 600

        self.curStroke = []
        self.brush = Brush(2,"brush",110)
        self.eraser = Brush(2,"eraser",255)
        self.eraserMode = False
        self.his = History()

        self.pointQueue = deque([])
        self.batch = graphics.Batch()
        self.background = graphics.OrderedGroup(0)
        self.drawingLayer = graphics.OrderedGroup(2)
        self.layer1 = graphics.OrderedGroup(1)
        
        self.canvas = self.batch.add(self.width*self.height,
                                     gl.GL_POINTS, self.background,
                                     ('v2i'), ('c3B'))
        self.swap = self.batch.add(self.width*self.height,
                                     gl.GL_POINTS, self.drawingLayer,
                                     ('v2i'), ('c3B'))
        
        self._buildCanvas(self.canvas)
        self._buildSwap(self.swap)

        self.layers.append(Layer(self.width,self.height,self.batch,self.layer1,0))
        
        self.currentLayer = self.layers[0]
        self.order.append(1)
        
        layerAction = Action()
        layerAction.layer = self.currentLayer
        layerAction.name = self.currentLayer.name
        self.his.addAction(layerAction)

    def draw(self):
        '''Updates the canvas, drawing all layers'''
        self.batch.draw()

    def _buildCanvas(self, canvas):
        for x in range(self.width):
            for y in range(self.height):
                '''We have to convert our 2d coordinates into a 1d array index'''
                i = self._2dTo1d(x, y)
                canvas.vertices[i*2:i*2+2] = [x, y]
                canvas.colors[i*3:i*3+3] = [255, 255, 255]
                
    def _buildSwap(self, swap):
        for i in range(self.width*self.height):
            '''We have to convert our 2d coordinates into a 1d array index'''
            swap.vertices[i*2:i*2+2] = [0,0]
            swap.colors[i*3:i*3+3] = [0,0,0]

    def setBrushSize(self, command):
        if(command == 'Increase Brush Size'):
            self._incBrush()
        else:
            self._decBrush()
    def _incBrush(self):
        if(self.brush.size < 10):
            self.brush.size = self.brush.size + 2

    def _decBrush(self):
        if(self.brush.size > 2):
            self.brush.size = self.brush.size - 2

    def setPencil(self):
        self.eraserMode = False

    def setEraser(self):
        self.eraserMode = True

    def addLayer(self):
        self._addLayer()

    def setCurrentLayer(self, index):
        self.currentLayer = layers[index]

    def _addLayer(self, name="Untitled Layer"):
        '''Adds a new layer to the canvas, and selects it as the current canvas'''
        newGroup = graphics.OrderedGroup(len(self.layers)+1)
        self.order.append(len(self.layers)+1)
        self.layers.append(Layer(self.width, self.height, self.batch,newGroup,len(self.layers)))
        self.currentLayer = self.layers[len(self.layers)-1]

    def setLayer(self, layerIndex, orderValue):
        '''Sets the drawing order of a layer to the selected orderValue (0-Background, 1+Foreground)'''
        newGroup = graphics.OrderedGroup(orderValue)
        self.order[layerIndex] = orderValue
        self.layers[layerIndex].group = newGroup
        self.layers[layerIndex].index = orderValue

    def deleteLayer(self, layerIndex):
        '''Deletes a layer from the canvas'''
        if(layerIndex > 0 and layerIndex < len(self.layers)):
            for layer in self.layers[layerIndex:len(self.layers)]:
                layer.index = layer.index -1            
            self.order.pop(layerIndex)
            self.layers.pop(layerIndex)

    def incrementLayer(self, layerIndex):
        '''Increments a layer's drawing order by swapping it's position in the hierarchy with the one above it, if any'''
        if(layerIndex-1 < len(self.order)):
            oldLayer = self.order[layerIndex-1]
            newLayer = self.order[layerIndex]
            self.setLayer(layerIndex-1, newLayer)
            self.setLayer(layerIndex, oldLayer)

    def decrementLayer(self, layerIndex):
        '''Decrements a layer's drawing order by one'''
        if(layerIndex < len(self.layers) and layerIndex > 0):
            oldLayer = self.order[layerIndex]
            newLayer = self.order[layerIndex-1]
            self.setLayer(layerIndex, newLayer)
            self.setLayer(layerIndex-1, oldLayer)
        
    def addPoint(self, x, y):
        '''Adds a point to the current stroke list and calls drawPoint to draw it on the canvas'''
        if(self.currentLayer.visible):
            self.pointQueue.append((x, y))
            if (len(self.pointQueue) > 2):
                curPoint = self.pointQueue.popleft()
                lineS = self._interpolate(curPoint[0], curPoint[1],
                                          self.pointQueue[0][0],
                                          self.pointQueue[0][1],
                                          self.pointQueue[1][0],
                                          self.pointQueue[1][1])
                for point in lineS:
                    self.curStroke.append(point)
                    self.drawPoint(point[0], point[1])
                self.curStroke.append(curPoint)                
                self.drawPoint(curPoint[0], curPoint[1])

    def endLine(self, x, y):
        '''Saves the end of a stroke to the current layer'''
        if(self.currentLayer.visible):
            while(len(self.pointQueue) > 0):
                curPoint = self.pointQueue.popleft()
                self.drawPoint(curPoint[0], curPoint[1])
                self.curStroke.append(curPoint)
            
            #Add the current stroke to the history and the layer
            newAction = Action()
            newAction.name = 'Stroke'
            finalStroke = Stroke(self.curStroke,255)
            if(not self.eraserMode):
                self.currentLayer.addStroke(finalStroke,self.brush)
            else:
                self.currentLayer.addStroke(finalStroke,self.eraser)
                
            newAction.stroke = finalStroke
            self.his.addAction(newAction)

            #Clear the canvas and the temporary stroke
            self.swap.colors = [255,255,255]*self.width*self.height
            self.swap.vertices = [0,0]*self.width*self.height
            self.curStroke = []

    def drawPoint(self, x, y):
        '''Draws a point directly on the swap canvas'''
        for i in range(0, self.brush.size):
            colorRow = []
            vertRow = []
            for q in range(0, self.brush.size):
                vertRow.append(x+q)
                vertRow.append(y+i)
            if(not self.eraserMode):
                colorRow = [self.brush.shade]* 3 * self.brush.size
                self.swap.vertices[((y+i)*self.width+x)*2:((y+i)*self.width+x)*2+2*self.brush.size] = vertRow
                self.swap.colors[((y+i)*self.width+x)*3:((y+i)*self.width+x)*3+3*self.brush.size] = colorRow
            else:
                colorRow = [self.eraser.shade]* 3 * self.brush.size
                self.swap.vertices[((y+i)*self.width+x)*2:((y+i)*self.width+x)*2+2*self.brush.size] = vertRow
                self.swap.colors[((y+i)*self.width+x)*3:((y+i)*self.width+x)*3+3*self.brush.size] = colorRow
            

                
    def _2dTo1d(self, x, y):
        '''_2dTo1d converts the coordinates for a 2d array to a corresponding
        1d array index'''
        return y*self.width+x

    def _interpolate(self, x0, y0, x1, y1, x2, y2):
        t = 0.0
        pointList = []
        #B(t) = (1-t)^2P0 + 2(1-t)tP1 + t^2P2, t E [0,1]
        while t <= 1.0:
            ty = int(pow((1-t), 2) * y0 + 2*(1-t)*t*y1 + (t*t) * y2)
            tx = int(pow((1-t), 2) * x0 + 2*(1-t)*t*x1 + (t*t) * x2)
            t += .01
            pointList.append((tx, ty))
        return pointList

    def resizeCanvas(self, top, right, bottom, left):
        '''Changes the size of the canvas'''
        width = width + right + left
        height = height + top + bottom

        if(top > 0):
            #If adding space to the top, show the extra space
            referenceY = 0 
        else:
            #otherwise move the screen down to show the extra space on the bottom
            referenceY = referenceY + bottom

        if(left > 0):
            #If adding space to the left, show the extra space
            referenceX = 0
        else:
            #Otherwise move the screen right to show the extra space added
            referenceX = referenceX + right

    def export(self):
        '''Passes an array of [R G B] * Pixels to CobraSketch for storing'''
        out = [255] * (self.height * self.width)
        for layer in self.layers:
            cIndex = 0
            for i in range(0,int(len(layer.canvas.vertices)/2)):
                x = layer.canvas.vertices[i*2]
                y = layer.canvas.vertices[i*2+1]
                r = layer.canvas.colors[cIndex]
                g = layer.canvas.colors[cIndex+1]
                b = layer.canvas.colors[cIndex+2]
                out[self._2dTo1d(x,y)] = r
                
                cIndex = cIndex + 3
        print("done exporting")
        return out

    def load(self, pixels):
        '''Recieves the appropriate information from Sketch for loading'''
        print("loading")
        print(len(pixels),len(self.canvas.colors))
        for i in range(0,int(len(self.canvas.colors)/3)):
            self.canvas.colors[i:i+3] = [pixels[i]]*3

        self.layers = []
        self.order = []
        
        self.drawingLayer = graphics.OrderedGroup(2)
        self.layer1 = graphics.OrderedGroup(1)
        self.layers.append(Layer(self.width,self.height,self.batch,self.layer1,0))        
        self.currentLayer = self.layers[0]
        self.order.append(1)
        

    def newStroke(self, points, brush):
        '''Applys the given points using brush to the current layer'''

    def newLayer(self, position):
        '''Creates a new layer at the given position'''

        
