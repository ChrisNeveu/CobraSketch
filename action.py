#CobraSketch
#by Andrew Sheldon, Chris Neveu, Ryan Darge, and Collin McAloon

from .history import History
from .stroke import Stroke
from .brush import Brush

class Action:
    def __init__(self, stroke, brush):
        self.stroke = Stroke.Stroke(int, int, int)
        self.brush = Brush
        
    
