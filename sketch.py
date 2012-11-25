#CobraSketch
#by Andrew Sheldon, Chris Neveu, Ryan Darge, and Collin McAloon

#!/usr/bin/env python3

from pyglet import *
from pyglet.window import mouse
from collections import deque

from canvas import Canvas
from brush import Brush
from layer import Layer
from history import History
from stroke import Stroke
from action import Action

class CobraSketch:
    '''Main Class'''
    
    def __init__(self):
        self.width = 800
        self.height = 600


        self.pointQueue = deque([])

        self.window = window.Window(self.width-1, self.height-1)
        self.batch = graphics.Batch()

        self.canvas = self.batch.add(self.width*self.height,
                                     gl.GL_POINTS,None,
                                     ('v2i'), ('c3B'))
        self._buildCanvas(self.canvas)

        #Create event handlers
        self.on_mouse_drag  = self.window.event(self.on_mouse_drag)
        self.on_draw  = self.window.event(self.on_draw)
        self.on_mouse_press  = self.window.event(self.on_mouse_press)
        self.on_mouse_release  = self.window.event(self.on_mouse_release)

    def _buildCanvas(self, canvas):
        for x in range(self.width):
            for y in range(self.height):
                '''We have to convert our 2d coordinates into a 1d array index'''
                i = self._2dTo1d(x, y)
                canvas.vertices[i*2:i*2+2] = [x, y]
                canvas.colors[i*3:i*3+3] = [255, 255, 255]

    def drawPoint(self, x, y):
        for i in range(0, 2):
            for j in range(0, 2):
                self.canvas.colors[((y+i)*self.width+x+j)*3:((y+i)*self.width+x+j)*3+3] = [0, 0, 0]

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

    def _2dTo1d(self, x, y):
        '''_2dTo1d converts the coordinates for a 2d array to a corresponding
        1d array index'''
        return y*self.width+x

    # # # # # # # # # # # # # #
    # File Manipulation Follows
    # 
    def open(self, file):
        '''Determines whether the file is a CobraSketch file or a bitmap
        and acts accordingly to load that file into the program.'''

    def save(self, file):
        '''Accepts a file location and saves either a bitmap or
        Cobrasketch file.'''

    def _loadFile(self, file):
        '''Sets the program state to the contents of a file'''

    def _saveFile(self, file):
        '''Saves the current program state to a file'''

    def _importImage(self, file):
        '''Loads a bitmap into the canvas'''

    def _exportImage(self, file):
        '''Saves the canvas to a bitmap'''

    # # # # # # # # # # # # #
    # Event Handlers Follow
    #
    def on_mouse_drag(self, x, y, dx, dy, button, modifiers):
        if button == mouse.LEFT:
            self.pointQueue.append((x, y))
            if (len(self.pointQueue) > 1):
                curPoint = self.pointQueue.popleft()
                lineS = self._interpolate(curPoint[0], curPoint[1],
                                         self.pointQueue[0][0],
                                         self.pointQueue[0][1])
                for point in lineS:
                    self.drawPoint(point[0], point[1])
                self.drawPoint(curPoint[0], curPoint[1])

    def on_mouse_press(self, x, y, button, modifiers):
        '''Event handler for mouse pressing.'''

    def on_mouse_release(self, x, y, button, modifiers):
        '''Event handler for mouse release.'''
        curPoint = self.pointQueue.popleft()
        self.drawPoint(curPoint[0], curPoint[1])

    def on_draw(self):
        self.window.clear()
        self.batch.draw()      

sketch = CobraSketch()

app.run()
