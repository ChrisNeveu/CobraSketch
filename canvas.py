#CobraSketch
#by Andrew Sheldon, Chris Neveu, Ryan Darge, and Collin McAloon

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
    
    def __init__(self, parent, name, path):
        '''Constructor'''

        #Get size from parent
        self.parent = parent
        self.width = parent.width
        self.height = parent.height

        self.name = name
        self.filepath = path

        self.referenceX = 0
        self.referenceY = 0
        self.windowWidth = 800
        self.windowHeight = 600

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

    def 

        
