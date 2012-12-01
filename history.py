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
        if (undo.Stroke.vis == True):
            undo.Stroke.setVisibility(False)
       # if (undo.Layer.vis == True):
       #     undo.Layer.vis = False
            
    #redo an Action
    def redoAction(self, redo):
        '''Sets visibility of an object to True'''
        if (redo.Stroke.vis == False):
              redo.Stroke.setVisibility(True)
      # if (redo.Layer.vis == False):
       #     redo.Layer.vis = True
                
    def getHistory(self):
        '''get list of history action'''
        z = 0
        for z in range (0, self.x):
            print (self.index[z])
        #return self.index2
    
    #add an action to history
    def addAction(self, Act):
        '''Checks the type and adds the Class to index'''
        self.index.append(Act)
        self.index2.append((Act.name, self.x))
        self.x = self.x + 1
        #Old implementation 
        '''if (issubclass(type(Act), Stroke)):
            self.index.append(Act)
            self.index2.append(('Stroke', self.x))
        #if (issubclass(type(Act), Brush)):
         #   self.index.append(Act)
            #need Brush variable
          #  self.index2.append(Act)
        if (issubclass(type(Act), Layer)):
            self.index.append(Act)
            #need Layer variable
            self.index2.append((Act.name, self.x))
        self.x = self.x + 1    '''
        
    #get the last action saved to history 
    def lastAction(self):
        '''returns last variable saved to index'''
        return self.index2[self.x - 1]

#History test main
h = History()
x = Stroke([(2,3),(5,1),(2,3),(5,3)],6)
y = Stroke((5,3), 5)
#layer = Layer('newLayer', 2, 5,"lulz")
'''
newAction = Action()
newAction.name = 'Stroke'
act1 = Action()
act1.name = layer.name
newAction.Stroke = x
act1.Layer = layer
actStroke = Action
actStroke.Stroke = y
actStroke.name = 'Stroke '
h.addAction(act1)
h.addAction(newAction)
h.addAction(actStroke)
h.undoAction(h.index[2])
'''


    
