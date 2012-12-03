#CobraSketch
#by Andrew Sheldon, Chris Neveu, Ryan Darge, and Collin McAloon

class Brush:
    '''Class for the Brush'''
    size = int
    texture = (int, int)
    shade = float

    def __init__(self, s, tex, sha):
        '''Constructor'''
        self.size = s
        self.texture = tex
        self.shade = sha

    def setSize(self, newSize):
        '''Resizes the brush'''
        self.size = newSize

    def setShade(self, newShade):
        '''Changes the shade of the brush'''
        self.shade = newShade

    def setTexture(self, newTex):
        '''Changes the texture of the brush'''
        self.texture = newTex
