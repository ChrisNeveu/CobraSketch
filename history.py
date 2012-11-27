#CobraSketch
#by Andrew Sheldon, Chris Neveu, Ryan Darge, and Collin McAloon
from stroke import Stroke
from action import Action
#from brush import Brush
from layer import Layer


class History:
    '''Set up basic variables to see if it would run'''
    index = []
    x = int
    #index holds the classes, index 2 holds the variables
    index2 = []
    def __init__(self):
        '''Constructor'''
        self.index
        self.x = 0
        
    #undo an action
    def undoAction(self, undo):
        '''Sets visibility of an object to false'''
        if (issubclass(type(undo), Stroke)):
            if(undo.getVisibility() == True):
                undo.setVisibility(False)
    #redo an Action
    def redoAction(self, redo):
        '''Sets visibility of an object to True'''
        if (issubclass(type(redo), Stroke)):
            if (redo.getVisibility() == False):
                redo.setVisibility(True)
                
    def getHistory(self):
        '''get list of history action'''
        return self.index
    
    #add an action to history
    def addAction(self, Act):
        '''Checks the type and adds the Class to index'''
        if (issubclass(type(Act), Stroke)):
            self.index.append(Act)
            self.index2.append(Act.stroke)
        #if (issubclass(type(Act), Brush)):
         #   self.index.append(Act)
            #need Brush variable
          #  self.index2.append(Act)
        if (issubclass(type(Act), Layer)):
            self.index.append(Act)
            #need Layer variable
            self.index2.append(Act)
        self.x = self.x + 1
        return Act    
    #get the last action saved to history 
    def lastAction(self):
        '''returns last variable saved to index'''
        return self.index[self.x - 1]

#History test main
h = History()
x = Stroke([2,3,5,1,2,3,5,3],6)
h.addAction(x)


    
