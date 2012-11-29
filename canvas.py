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

        self.pointQueue = deque([])
        self.batch = graphics.Batch()
        self.canvas = self.batch.add(self.width*self.height,
                                     gl.GL_POINTS,None,
                                     ('v2i'), ('c3B'))

        self._buildCanvas(self.canvas)

    def draw(self):
        self.batch.draw()

    def _buildCanvas(self, canvas):
        for x in range(self.width):
            for y in range(self.height):
                '''We have to convert our 2d coordinates into a 1d array index'''
                i = self._2dTo1d(x, y)
                canvas.vertices[i*2:i*2+2] = [x, y]
                canvas.colors[i*3:i*3+3] = [255, 255, 255]

    def add_point(self, x, y):
        self.pointQueue.append((x, y))
        if (len(self.pointQueue) > 1):
            curPoint = self.pointQueue.popleft()
            lineS = self._interpolate(curPoint[0], curPoint[1],
                                     self.pointQueue[0][0],
                                     self.pointQueue[0][1])
            for point in lineS:
                self.drawPoint(point[0], point[1])
            self.drawPoint(curPoint[0], curPoint[1])


    def end_line(self, x, y):
        curPoint = self.pointQueue.popleft()
        self.drawPoint(curPoint[0], curPoint[1])
        

    def drawPoint(self, x, y):
        for i in range(0, 2):
            for j in range(0, 2):
                self.canvas.colors[((y+i)*self.width+x+j)*3:((y+i)*self.width+x+j)*3+3] = [0, 0, 0]

    def _2dTo1d(self, x, y):
        '''_2dTo1d converts the coordinates for a 2d array to a corresponding
        1d array index'''
        return y*self.width+x

    def _interpolate(self, x1, y1, x2, y2):
        flag = True
        pointList = []
        while x1 != x2 or y1 != y2:
            if(flag):
                if(x1 > x2):
                    x1 -= 1
                elif(x1 < x2):
                    x1 += 1
            else:
                if(y1 > y2):
                    y1 -= 1
                elif(y1 < y2):
                    y1 += 1
            pointList.append((x1, y1))
            flag = not flag
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

        
