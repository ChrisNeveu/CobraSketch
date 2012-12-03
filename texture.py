#CobraSketch
#by Andrew Sheldon, Chris Neveu, Ryan Darge, and Collin McAloon

class Texture:
    '''Class for the textures for drawing'''

    def __init__(self, center, points):
        '''Texture Constructor'''
        self.center = center
        self.points = points
        
    def brush(self):
        '''returns the points for the brush'''
        return self.points
    
