#CobraSketch
#by Andrew Sheldon, Chris Neveu, Ryan Darge, and Collin McAloon

class Layer:
    '''Layer Class'''

    name = ""
    width = 0
    height = 0
    bitmap = []

    def __init__(self, name, width, height):
        '''Constructs Layer Object'''
        self.name = name
        self.width = width
        self.height = height
        self.bitmap = [[0]*height for x in range(width)]

    def drawLayer(self, bitmap):
        '''Draws the layer to the specified bitmap object'''

    def resizeLayer(self, top, right, bottom, left):
        '''Resizes the layer based on the points added to the top/right/left/bottom'''

    def newStroke(self, points):
        '''Applies a new stroke to the current bitmap'''
        for point in points:
            x = point[0]
            y = point[1]
            s = point[2]
            print("x:",x,"y:",y)
            self.printVals()
            self.bitmap[x][y] = s;
            

    def printVals(self):
        '''Debugging - Prints out the contents of the "bitmap"'''
        print(self.bitmap)

layer = Layer("Spaghetti",5,10)
print(layer.name)
points = ((0,0,255),(1,1,255),(2,2,255),(3,3,255),(4,4,255))
layer.newStroke(points);
