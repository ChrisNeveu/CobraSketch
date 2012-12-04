#CobraSketch
#by Andrew Sheldon, Chris Neveu, Ryan Darge, and Collin McAloon
from stroke import Stroke
from action import Action
from brush import Brush
from layer import Layer


class History:
    '''History Class'''
    index = []
    x = int
    #index holds the classes, index 2 holds the names
    index2 = []
    
    def __init__(self):
        '''Constructor'''
        self.index
        self.index2
        self.x = 0
        
    #undo an action
    def undoAction(self, undo):
        '''Sets visibility of an object to false'''
        if (undo.stroke.vis == True):
            undo.stroke.setVisibility(False)
        if (undo.layer.visible == True):
            undo.layer.visible = False
            
    #redo an Action
    def redoAction(self, redo):
        '''Sets visibility of an object to True'''
        if (redo.stroke.vis == False):
            redo.stroke.setVisibility(True)
        if (redo.layer.visible == False):
            redo.layer.visible = True
                
    def getHistory(self):
        '''get list of history action'''
        z = 0
        for z in range (0, self.x):
            print (self.index2[z])
        #return self.index2
    
    #add an action to history
    def addAction(self, Act):
        '''Checks the type and adds the Class to index'''
        self.index.append(Act)
        self.index2.append((Act.name, self.x))
        self.x = self.x + 1
        
    #get the last action saved to history 
    def lastAction(self):
        '''returns last variable saved to index'''
        return self.index2[self.x - 1]

#History test main
