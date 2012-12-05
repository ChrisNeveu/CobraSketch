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
        self.brush = Brush(2,"Nope",110)
        self.his = History()

        self.pointQueue = deque([])
        self.batch = graphics.Batch()
        self.background = graphics.OrderedGroup(0)
        self.foreground = graphics.OrderedGroup(1)
        
        self.canvas = self.batch.add(self.width*self.height,
                                     gl.GL_POINTS, self.background,
                                     ('v2i'), ('c3B'))

        self._buildCanvas(self.canvas)

        self.layers.append(Layer("Layer 1",self.width,self.height,self.batch,self.foreground))
        self.currentLayer = self.layers[0]
        
        self.swap = Layer("Swap",self.width, self.height,self.batch,self.foreground)
        layerAction = Action()
        layerAction.layer = self.currentLayer
        layerAction.name = self.currentLayer.name
        self.his.addAction(layerAction)

    def draw(self):        
        self.batch.draw()

    def _buildCanvas(self, canvas):
        for x in range(self.width):
            for y in range(self.height):
                '''We have to convert our 2d coordinates into a 1d array index'''
                i = self._2dTo1d(x, y)
                canvas.vertices[i*2:i*2+2] = [x, y]
                canvas.colors[i*3:i*3+3] = [255, 255, 255]

    def addPoint(self, x, y):
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
        print("ASKFAJIDSFIADSF")
        '''Saves the end of a stroke to the current layer'''        
        while(len(self.pointQueue) > 0):
            curPoint = self.pointQueue.popleft()
            self.drawPoint(curPoint[0], curPoint[1])
            self.curStroke.append(curPoint)
        

        #If the stroke is complete, clear the swap layer
        #and draw it from the appropriate layer
        newAction = Action()
        newAction.name = 'Stroke'
        finalStroke = Stroke(self.curStroke,255)
        newAction.stroke = finalStroke
        self.canvas.colors = [255,255,255]*self.width*self.height
        self.currentLayer.addStroke(finalStroke,self.brush)
        self.his.addAction(newAction)
        #self.his.getHistory()

    def drawPoint(self, x, y):
        for i in range(0, self.brush.size):
            for j in range(0, self.brush.size):
                self.canvas.colors[((y+i)*self.width+x+j)*3:((y+i)*self.width+x+j)*3+3] = [self.brush.shade]* 3

                
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

    def export(self, filename):
        '''Passes the appropriate information to Sketch for saving'''
        

    def load(self, filename):
        '''Recieves the appropriate information from Sketch for loading'''

    def newStroke(self, points, brush):
        '''Applys the given points using brush to the current layer'''

    def newLayer(self, position):
        '''Creates a new layer at the given position'''

        
