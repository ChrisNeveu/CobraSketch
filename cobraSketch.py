#CobraSketch
#by Andrew Sheldon, Chris Neveu, Ryan Darge, and Collin McAloon

#!/usr/bin/env python3

import os
import pyglet
from pyglet import *
from pyglet.window import mouse
import kytten
from collections import deque

from canvas import Canvas
from brush import Brush
from layer import Layer
from history import History
from stroke import Stroke
from action import Action

# Disable error checking for increased performance
pyglet.options['debug_gl'] = False

class CobraSketch:
    '''Main Class'''
    
    def __init__(self):
        self.width = 800
        self.height = 600

        self.window = window.Window(self.width-1, self.height-1)
        self.window.register_event_type('on_update')
        pyglet.clock.schedule(self.update)

        self.canvas = Canvas(self.width, self.height, "Filename", "Path")

        #Create event handlers
        self.on_mouse_drag  = self.window.event(self.on_mouse_drag)
        self.on_draw  = self.window.event(self.on_draw)
        self.on_mouse_press  = self.window.event(self.on_mouse_press)
        self.on_mouse_release  = self.window.event(self.on_mouse_release)

        #Import theme
        self.cobalt = kytten.Theme(os.path.join(os.getcwd(), 'theme'), override={
            "font_size": 10
        })   
        self.bg_group = pyglet.graphics.OrderedGroup(0)
        self.fg_group = pyglet.graphics.OrderedGroup(500)

        #Create GUI
        self.mainDialog()
        self.layerDialog()


    # # # # # # # # # # # # # #
    # File Manipulation Follows
    # 
    def open(self, file):
        '''Determines whether the file is a CobraSketch file or a bitmap
        and acts accordingly to load that file into the program.'''
        fileName = file.split('.')
        fileType = fileName[len(fileName)-1]
        if fileType.lower() == 'png':
            self.canvas.load(self._loadPNG(file))
        else:
            print(fileType, ' not supported.')

    def save(self, file):
        '''Accepts a file location and saves either a bitmap or
        Cobrasketch file.'''
        fileName = file.split('.')
        fileType = fileName[len(fileName)-1]
        if fileType.lower() == 'png':
            self._savePNG(file, self.canvas.export())
        else:
            print(fileType, ' not supported.')

    def _loadPNG(self, file):
        '''Returns an array containing the pixel data for a PNG''' 
        png = pyglet.image.load(file)
        data = png.get_data('R', png.width)
        return [int.from_bytes(data[i:i+1],'little') for i in range(0,len(data), 1)]

    def _savePNG(self, file, pixels):
        '''Saves the current program state to a file'''
        out = pyglet.image.load('blank.png')
        pixels = [item for sublist in [[x, x, x] for x in pixels] for item in sublist]

        frame = bytes(pixels)

        out.set_data('RGB', out.width*3, frame)
        out.save(file)


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

    # # # # # # # # # # # # #
    # GUI Creator Follows
    #
    # Callback functions for dialogs which may be of interest
        
    def update(self, dt):
        self.window.dispatch_event('on_update', dt)

    
    def on_escape(self, dialog):
        dialog.teardown()

    def create_file_load_dialog(self):
        dialog = None

        def on_select(filename):
            print("File load: %s" % filename)
            self.on_escape(dialog)

        dialog = kytten.FileLoadDialog(  # by default, path is current working dir
            extensions=['.png', '.jpg', '.bmp', '.gif'],
            window=self.window, batch=self.canvas.batch, group=self.fg_group,
            anchor=kytten.ANCHOR_CENTER,
            theme=self.cobalt, on_escape=self.on_escape, on_select=on_select)

    def create_file_save_dialog(self):
        dialog = None

        def on_select(filename):
            print("File save: %s" % filename)
            self.on_escape(dialog)

        dialog = kytten.FileSaveDialog(  # by default, path is current working dir
            extensions=['.png', '.jpg', '.bmp', '.gif'],
            window=self.window, batch=self.canvas.batch, group=self.fg_group,
            anchor=kytten.ANCHOR_CENTER,
            theme=self.cobalt, on_escape=self.on_escape, on_select=on_select)

    def create_directory_select_dialog(self):
        dialog = None

        def on_select(filename):
            print("Directory: %s" % filename)
            self.on_escape(dialog)

        dialog = kytten.DirectorySelectDialog(
            window=self.window, batch=self.canvas.batch, group=self.fg_group,
            anchor=kytten.ANCHOR_CENTER,
            theme=self.cobalt, on_escape=self.on_escape, on_select=on_select)

    def on_select(self, choice):
        if choice == 'Open File':
            self.create_file_load_dialog()
        elif choice == 'Save File':
            self.create_file_save_dialog()
        elif choice == 'Directory Select':
            self.create_directory_select_dialog()
        else:
            print("Unexpected menu selection: %s" % choice)

    def mainDialog(self):
        def brushMenu(command):
            if command == 'Increase Brush Size' or command =='Decrease Brush Size':
                self.canvas.setBrushSize(command)
            elif command == 'Pencil':
                '''thing'''
            elif command == 'Eraser':
                '''thing'''
        
        # Set up a Dialog to choose test dialogs to show
        dialog = kytten.Dialog(
            kytten.Frame(
                kytten.HorizontalLayout([
                    kytten.Dropdown(['Save File', 'Open File'],
                                    on_select=self.on_select, text="File"),
                    kytten.Dropdown(['Copy', 'Cut', 'Paste'],
                                    on_select=self.on_select, text="Edit"),
                    kytten.Dropdown(['Pencil', 'Eraser', 'Increase Brush Size', 'Decrease Brush Size'],
                                    on_select=brushMenu, text="Brush"),
                    kytten.Dropdown(['Create Layer'],
                                    on_select=self.canvas.addLayer, text="Layers"),
                ], padding=0, align=kytten.VALIGN_TOP)
            ),
            window=self.window, batch=self.canvas.batch, group=self.fg_group,
            anchor=kytten.ANCHOR_TOP_LEFT,
            on_mouse_release=self.on_mouse_release,
            theme=self.cobalt)

    def layerDialog(self):
        # Set up a Dialog to choose test dialogs to show
        def createLayer():
            self.canvas.addLayer()
            dialog.teardown()
            self.layerDialog()

        def focusLayer(foo):
            def func():
                ''''''
            return func

        def incLayer(foo):
            def func():
                self.canvas.incrementLayer(foo)
                dialog.teardown()
                self.layerDialog()
            return func

        def decLayer(foo):
            def func():
                self.canvas.decrementLayer(foo)
                dialog.teardown()
                self.layerDialog()
            return func

        def delLayer(foo):
            def func():
                self.canvas.deleteLayer(foo)
                dialog.teardown()
                self.layerDialog()
            return func

        content = [item for sublist in
                   [
                       [kytten.HorizontalLayout([
                           kytten.Button("S", on_click=focusLayer(layer.index)),
                           kytten.Checkbox(layer.name, is_checked=layer.visible,
                                           on_click=layer.toggleVisibility),
                           kytten.Button("^", on_click=incLayer(layer.index)),
                           kytten.Button("v", on_click=decLayer(layer.index)),
                           kytten.Button("X", on_click=delLayer(layer.index))
                           ])
                        ] for layer in self.canvas.layers]
                   for item in sublist]
        content.append(kytten.Button("Create Layer", on_click=createLayer))
        dialog = kytten.Dialog(
            kytten.Frame(
                kytten.VerticalLayout(
                    content,
                    padding=0, align=kytten.VALIGN_TOP)
            ),
            window=self.window, batch=self.canvas.batch, group=self.fg_group,
            anchor=kytten.ANCHOR_TOP_RIGHT,
            on_mouse_release=self.on_mouse_release,
            theme=self.cobalt)


sketch = CobraSketch()

app.run()
