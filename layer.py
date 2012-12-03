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

    def __init__(self, name, width, height, batch):
        '''Constructs Layer Object'''
        self.visible = True
        self.name = name
        self.width = width
        self.height = height

        self.batch = batch
        self.canvas = batch.add(self.width*self.height,
                                     gl.GL_POINTS,None,
                                     ('v2i'), ('c3B'))

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

    def draw(self, canvas):
        '''Draws the current layer to the canvas'''     
            
                

    def addPoint(self, x, y):
        for i in range(0, 2):
            for j in range(0, 2):
                self.canvas = self.batch.add(1, gl.GL_POINTS, None,
                    ('v2i', (x, y)),
                    ('c3B', (0, 0, 0))
                )

                


    def resizeLayer(self, top, right, bottom, left):
        '''Resizes the layer based on the points added to the top/right/left/bottom'''
            

    def printVals(self):
        '''Debugging - Prints out the contents of the "bitmap"'''
        print(self.bitmap)

##layer = Layer("Spaghetti",5,10)
##print(layer.name)
##points = ((0,0,255),(1,1,255),(2,2,255),(3,3,255),(4,4,255))
##layer.newStroke(points);
