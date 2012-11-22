#CobraSketch
#by Andrew Sheldon, Chris Neveu, Ryan Darge, and Collin McAloon

class Stroke:
    #Temp variables 
    'x_value = 10'
    'y_value = 14'
    'shade = 0'
    
    hidden = True
    
    stroke = (int, int, int)
    #Stroke constructor 
    def __init__(self, x_value, y_value, shade):
        self.stroke = (x_value, y_value, shade)
        self.hidden = True

    #Toggles the visibility of the stroke
    def setVisibility(self, flag):
        self.hidden = flag

    #Gets the current visibility
    def getVisibility(self):
        return self.hidden
