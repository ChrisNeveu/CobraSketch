#CobraSketch
#by Andrew Sheldon, Chris Neveu, Ryan Darge, and Collin McAloon
from stroke import Stroke
from action import Action

class History:
    '''Set up basic variables to see if it would run'''
    index = []
    x = 0
    #undo an action
    def undoAction(self, undo):
        if (issubclass(type(undo), Stroke)):
            undo.setVisibility(False)
    #redo an Action
    def redoAction(self, redo):
        if (issubclass(type(redo), Stroke)):
            redo.setVisibility(True)
    #get list of history action
    def getHistory(self):
        return self.index
    #add an action to history
    def addAction(self, Action):
        if (issubclass(type(Action), Stroke)):
            self.index.append(Action.stroke)
        if (issubclass(type(Action), Brush)):
            self.index.append(Action.brush)
        if (issubclass(type(Action), Layer)):
            self.index.append(Action.layer)
        self.x = self.x + 1
        return Action    
    #get the last action saved to history 
    def lastAction(self):   
        return self.index[self.x - 1]


    
