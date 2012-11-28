#CobraSketch
#by Andrew Sheldon, Chris Neveu, Ryan Darge, and Collin McAloon

class Stroke:
    
    vis = bool
    stroke = []
    
    def __init__(self, ptList, shd):
        '''Stroke constructor'''
        self.stroke = ptList
        self.shade = (shd)
        self.vis = True

    def setVisibility(self, flag):
        '''Toggles the visibility of the stroke'''
        self.vis = flag

   
    def getVisibility(self):
        '''Gets the current visibility'''
        return self.vis
    
x = Stroke([(5,5), (2,5)], 2)
