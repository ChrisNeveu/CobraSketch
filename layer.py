#CobraSketch
#by Andrew Sheldon, Chris Neveu, Ryan Darge, and Collin McAloon

class Layer:
    '''Layer Class'''

    name = ""
    width = 0
    height = 0
    visible = bool
    strokes = []

    def __init__(self, name, width, height):
        '''Constructs Layer Object'''
        self.visible = True
        self.name = name
        self.width = width
        self.height = height

        #Initial single stroke
        points = ((0,0,255),(1,1,255),(2,2,255),(3,3,255),(4,4,255))
        self.newStroke(points)

    def applyTo(self, bitmap):
        '''Draws the layer to the specified batch object'''
        for stroke in self.strokes:
            for point in stroke:
                print(point)
                self.drawPoint(point[0],point[1],bitmap)

    def _2dTo1d(self, x, y):
        '''_2dTo1d converts the coordinates for a 2d array to a corresponding
        1d array index'''
        return y*self.width+x

    def drawPoint(self, x, y, bitmap):
        for i in range(0, 2):
            for j in range(0, 2):
                bitmap.colors[self._2dTo1d(x+j,y+i)*3:self._2dTo1d(x+j,y+i)*3+3] = [0, 0, 0]


    def resizeLayer(self, top, right, bottom, left):
        '''Resizes the layer based on the points added to the top/right/left/bottom'''

    def newStroke(self, points):
        '''Applies a new stroke to the current bitmap'''
        self.strokes.append(points)
            

    def printVals(self):
        '''Debugging - Prints out the contents of the "bitmap"'''
        print(self.bitmap)

##layer = Layer("Spaghetti",5,10)
##print(layer.name)
##points = ((0,0,255),(1,1,255),(2,2,255),(3,3,255),(4,4,255))
##layer.newStroke(points);
