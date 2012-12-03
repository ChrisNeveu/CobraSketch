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

        self.window = window.Window(self.width-1, self.height-1)

        self.canvas = Canvas(self.width, self.height, "Filename", "Path")

        #Create event handlers
        self.on_mouse_drag  = self.window.event(self.on_mouse_drag)
        self.on_draw  = self.window.event(self.on_draw)
        self.on_mouse_press  = self.window.event(self.on_mouse_press)
        self.on_mouse_release  = self.window.event(self.on_mouse_release)


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
            if(x > 0 and y > 1 and x < self.width and y < self.height-1):
                self.canvas.addPoint(x,y)
                    

    def on_mouse_press(self, x, y, button, modifiers):
        '''Event handler for mouse pressing.'''

    def on_mouse_release(self, x, y, button, modifiers):
        '''Event handler for mouse release.'''
        self.canvas.endLine(x, y)

    def on_draw(self):
        self.window.clear()
        self.canvas.draw()      

sketch = CobraSketch()

app.run()
