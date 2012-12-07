#CobraSketch
#by Andrew Sheldon, Chris Neveu, Ryan Darge, and Collin McAloon

from pyglet import *

class Layer:
    '''Layer Class'''

    name = ""
    width = 0
    height = 0
    visible = bool
    points = []
    transparent = ""

    def __init__(self, width, height, batch, group, index, name="Untitled Layer", ):
        '''Constructs Layer Object'''
        self.visible = True
        self.name = name
        self.width = width
        self.height = height
        self.index = index

        self.batch = batch
        self.group = group
        self.canvas = batch.add(1, gl.GL_POINTS, group, ('v2i'), ('c3B'))

##        for x in range(self.width):
##            for y in range(self.height):
##                '''We have to convert our 2d coordinates into a 1d array index'''
##                i = self._2dTo1d(x, y)
##                canvas.vertices[i*2:i*2+2] = [x, y]
##                canvas.colors[i*3:i*3+3] = [255, 255, 255]

    def _2dTo1d(self, x, y):
        '''_2dTo1d converts the coordinates for a 2d array to a corresponding
        1d array index'''
        return y*self.width+x

    def toggleVisibility(self, command):
        self._toggleVisibility()

    def _toggleVisibility(self):
        '''Toggles the visibility of this layer'''
        if(self.visible is True):
            self.hiddenColors = self.canvas.colors
            self.hiddenVerts = self.canvas.vertices
            self.canvas.delete()
        else:
            self.canvas = self.batch.add(1,gl.GL_POINTS, self.group, ('v2i'), ('c3B'))
            self.canvas.resize(int(len(self.hiddenVerts)/2))
            self.canvas.colors = self.hiddenColors
            self.canvas.vertices = self.hiddenVerts
            
        self.visible = not self.visible
                    
    def addStroke(self, points, brush):
        '''Adds a stroke to the canvas, drawing the appropriate pixels. The stroke is not saved'''
        vertexStep = len(self.canvas.vertices)
        colorStep = len(self.canvas.colors)
        # newsize = current size (vertices/2) + number of new points)
        newSize = int(len(self.canvas.vertices)/2.0)+(points.size()*(brush.size*brush.size))
        self.canvas.resize(newSize)

        #prepare for moar lagz
        for point in points.getPoints():
            for i in range(0, brush.size):
                for j in range(0, brush.size):
                    #Modify appropriate vertex points...
                    self.canvas.vertices[vertexStep+0] = point[0] + i
                    self.canvas.vertices[vertexStep+1] = point[1] + j
                    vertexStep = vertexStep + 2

        self.canvas.colors[colorStep:] = [brush.shade]*(len(self.canvas.colors)-colorStep)


    def resizeLayer(self, top, right, bottom, left):
        '''Resizes the layer based on the points added to the top/right/left/bottom'''

    def getGroup():
        '''Returns the group index number for rearranging layers'''
        return group
            

    def printVals(self):
        '''Debugging - Prints out the contents of the "bitmap"'''
        print(self.bitmap)

##layer = Layer("Spaghetti",5,10)
##print(layer.name)
##points = ((0,0,255),(1,1,255),(2,2,255),(3,3,255),(4,4,255))
##layer.newStroke(points);
