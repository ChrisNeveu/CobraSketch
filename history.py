#CobraSketch
#by Andrew Sheldon, Chris Neveu, Ryan Darge, and Collin McAloon
'''from .stroke import Stroke'''
'''from .action import Action'''

class History:
    '''Set up basic variables to see if it would run'''
    index = []
    x = 0
    #undo an action
    def undoAction(undo):
        #History.index[undo]'''Relate to Stroke Class'''
        undo.setVisibility(False)
    #redo an Action
    def redoAction(redo):
        #History.index[redo]'''Relate to Stroke Class'''
        redo.setVisibility(True)
    #get list of history action
    def getHistory():
        return History.index
    #add an action to history
    def addAction(Action):
        if (Action):
            History.index.append(Action.stroke)
        #History.index.append(Action)
        History.x = History.x + 1
        return Action    
    #get the last action saved to history 
    def lastAction():
        return History.index[History.x - 1]


    
