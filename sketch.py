#!/usr/bin/env python3

from pyglet import *
from pyglet.window import mouse

'''Window width and height (also the width/height of our canvas'''
WIDTH = 800
HEIGHT = 600


window = window.Window(WIDTH-1, HEIGHT-1)
batch = graphics.Batch()
canvas = batch.add(WIDTH*HEIGHT, gl.GL_POINTS, None, ('v2i'), ('c3B'))
for x in range(WIDTH):
    for y in range(HEIGHT):
        '''We have to convert our 2d coordinates into a 1d array index'''
        canvas.vertices[(y*WIDTH+x)*2:(y*WIDTH+x)*2+2] = [x, y]
        canvas.colors[(y*WIDTH+x)*3:(y*WIDTH+x)*3+3] = [255, 255, 255]
        
@window.event
def on_mouse_drag(x, y, dx, dy, button, modifiers):
    if button == mouse.LEFT:
        '''4x4 brush'''
        canvas.colors[(y*WIDTH+x)*3:(y*WIDTH+x)*3+3] = [0, 0, 0]
        canvas.colors[((y+1)*WIDTH+x)*3:((y+1)*WIDTH+x)*3+3] = [0, 0, 0]
        canvas.colors[(y*WIDTH+x+1)*3:(y*WIDTH+x+1)*3+3] = [0, 0, 0]
        canvas.colors[((y+1)*WIDTH+x+1)*3:((y+1)*WIDTH+x+1)*3+3] = [0, 0, 0]

@window.event
def on_draw():
        window.clear()
        batch.draw()      

app.run()
