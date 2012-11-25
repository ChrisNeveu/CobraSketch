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

        self.canvas = self.batch.add(self.width*self.height, gl.GL_POINTS, None, ('v2i'), ('c3B'))
        self.buildCanvas(self.canvas)

        '''Create event handlers'''
        self.on_mouse_drag  = self.window.event(self.on_mouse_drag)
        self.on_draw  = self.window.event(self.on_draw)

    def buildCanvas(self, canvas):
        for x in range(self.width):
            for y in range(self.height):
                '''We have to convert our 2d coordinates into a 1d array index'''
                canvas.vertices[(y*self.width+x)*2:(y*self.width+x)*2+2] = [x, y]
                canvas.colors[(y*self.width+x)*3:(y*self.width+x)*3+3] = [255, 255, 255]

    def drawPoint(self, x, y):
        for i in range(0, 2):
            for j in range(0, 2):
                self.canvas.colors[((y+i)*self.width+x+j)*3:((y+i)*self.width+x+j)*3+3] = [0, 0, 0]

    def interpolate(self, x1, y1, x2, y2):
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
    
    def on_mouse_drag(self, x, y, dx, dy, button, modifiers):
        if button == mouse.LEFT:
            self.pointQueue.append((x, y))
            if (len(self.pointQueue) > 1):
                curPoint = self.pointQueue.popleft()
                lineS = self.interpolate(curPoint[0], curPoint[1], self.pointQueue[0][0], self.pointQueue[0][1])
                for point in lineS:
                    self.drawPoint(point[0], point[1])
                self.drawPoint(curPoint[0], curPoint[1])

    def on_draw(self):
        self.window.clear()
        self.batch.draw()      

sketch = CobraSketch()


app.run()
