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
    def Stroke(x_value, y_value, shade):
        Stroke.stroke = (x_value, y_value, shade)

    #Toggles the visibility of the stroke
    def setVisibility(flag):
        Stroke.hidden = flag

    #Gets the current visibility
    def getVisibility():
        return Stroke.hidden
