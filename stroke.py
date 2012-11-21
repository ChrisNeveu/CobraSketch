#CobraSketch
#by Andrew Sheldon, Chris Neveu, Ryan Darge, and Collin McAloon

class Stroke:
    #Temp variables 
    x_value = 10
    y_value = 14
    shade = 0
    flag = False
    
    stroke = (x_value, y_value, shade)

    #Toggles the visibility of the stroke
    def setVisibility(hidden):
        Stroke.flag = hidden

    #Gets the current visibility
    def getVisibility():
        return Stroke.flag
