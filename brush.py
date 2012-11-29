#CobraSketch
#by Andrew Sheldon, Chris Neveu, Ryan Darge, and Collin McAloon

class Brush:
    '''Class for the Brush'''
    size = int
    texture = (int, int)
    shade = float

    def __init__(self, s, tex, sha):
        self.size = s
        self.texture = tex
        self.shape = sha

    def setSize(self, newsize):
        self.size = newsize

    def setShade(self, newshade):
        self.shade = newshade

    def setTexture(self, newtex):
        self.texture = newtex
