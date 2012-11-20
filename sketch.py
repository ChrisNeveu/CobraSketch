#CobraSketch
#by Andrew Sheldon, Chris Neveu, Ryan Darge, and Collin McAloon

#!/usr/bin/env python3

from pyglet import *
from pyglet.window import mouse
from collections import deque

from .canvas import Canvas
from .brush import Brush
from .layer import Layer
from .history import History
from .stroke import Stroke

'''Window width and height (also the width/height of our canvas'''
WIDTH = 800
HEIGHT = 600

pointQueue = deque([])

window = window.Window(WIDTH-1, HEIGHT-1)
batch = graphics.Batch()

#Build the canvas
canvas = batch.add(WIDTH*HEIGHT, gl.GL_POINTS, None, ('v2i'), ('c3B'))
for x in range(WIDTH):
    for y in range(HEIGHT):
        '''We have to convert our 2d coordinates into a 1d array index'''
        canvas.vertices[(y*WIDTH+x)*2:(y*WIDTH+x)*2+2] = [x, y]
        canvas.colors[(y*WIDTH+x)*3:(y*WIDTH+x)*3+3] = [255, 255, 255]



def drawPoint(x, y):
    #4x4 brush
    for i in range(0, 2):
            for j in range(0, 2):
                canvas.colors[((y+i)*WIDTH+x+j)*3:((y+i)*WIDTH+x+j)*3+3] = [0, 0, 0]

def interpolate(x1, y1, x2, y2):
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
        
@window.event
def on_mouse_drag(x, y, dx, dy, button, modifiers):
    if button == mouse.LEFT:
        pointQueue.append((x, y))
        if (len(pointQueue) > 1):
            curPoint = pointQueue.popleft()
            lineS = interpolate(curPoint[0], curPoint[1], pointQueue[0][0], pointQueue[0][1])
            for point in lineS:
                drawPoint(point[0], point[1])
            drawPoint(curPoint[0], curPoint[1])

@window.event
def on_draw():
        window.clear()
        batch.draw()      

app.run()
