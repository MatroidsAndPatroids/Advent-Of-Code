import turtle
import collections # OrderedDict
import time # sleep

# Create Pen to draw on the canvas
class Pen(turtle.Turtle):
    def __init__(self, size):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("black")
        self.fillcolor("white")
        self.speed(0)
        self.penup()
        self.shapesize(size / 24, size / 24, 1)

# Displajs a grid on the canvas
class PixelGrid:
    def __init__(self, height, width):
        # initialize class variables
        self.height = height
        self.width = width
        self.blockPixels = 24
        self.pixels = collections.OrderedDict()
        self.pen = Pen(self.blockPixels - 1)
        self.sleepSec = 0.05
        
        # initalize window
        windowHeight = self.height * self.blockPixels + 75
        windowWidth = self.width * self.blockPixels + 75
        self.windowTopLeftI = int((windowHeight - self.blockPixels) / 2) - 35
        self.windowTopLeftJ = -int((windowWidth - self.blockPixels) / 2) + 35
        self.window = turtle.Screen()
        backgroundColor = 'black'
        self.window.bgcolor(backgroundColor)
        self.window.tracer(0)
        self.window.setup(windowWidth, windowHeight)
        
        # initialize color list and don't allow to draw with the background color
        colors = 'yellow, gold, orange, red, maroon, violet, magenta, purple, navy, blue, skyblue, cyan, turquoise, lightgreen, green, darkgreen, chocolate, brown, black, gray, white'
        self.colors  = colors.split(', ')
        if self.colors.count(backgroundColor) > 0:
            self.colors.remove(backgroundColor)
    
    def numPixels(self):
        return len(self.pixels)

    def update(self, update):
        if update:
            turtle.title(f'{self.numPixels()} pixels are lit')
            self.window.update()
            time.sleep(self.sleepSec)
        
    def drawPixel(self, i, j, startingLayer = 0, update = True):
        if self.pixelExists(i, j):
            stampId, layer = self.pixels.pop(1000000 * i + j)
            self.pen.clearstamp(stampId)
            layer += startingLayer + 1
        else:
            layer = startingLayer
            
        x = self.windowTopLeftJ + j * self.blockPixels
        y = self.windowTopLeftI - i * self.blockPixels
        self.pen.goto(x, y)
        self.pen.color(self.colors[layer % len(self.colors)])
        self.pixels[1000000 * i + j] = self.pen.stamp(), layer
        self.update(update)
        
    def pixelExists(self, i, j):
        return 1000000 * i + j in self.pixels

    def fillArea(self, i1, j1, i2, j2, update = True):
        for i in range(i1, i2):
            for j in range(j1, j2):
                self.drawPixel(i, j, 0, False)
        self.update(update)
    
    def moveBlock(self, i1, j1, i2, j2, deltaI, deltaJ, update = True):
        temp = [] # temporary storage of deleted pixels
        for i in range(i1, i2):
            for j in range(j1, j2):
                if self.pixelExists(i, j):
                    stampId, layer = self.pixels.pop(1000000 * i + j)
                    self.pen.clearstamp(stampId)
                    temp.append([i, j, stampId, layer])
        for i, j, stampId, layer in temp:
            self.drawPixel(i + deltaI, j + deltaJ, layer, False)
        self.update(update)
        
    def movePixel(self, i, j, newI, newJ, update = True):
        self.moveBlock(i, j, i + 1, j + 1, newI - i, newJ - j, False)
       
    def rotateRow(self, i, delta, update = True):
        j, delta1, delta2 = (self.width, 1, -self.width) if delta > 0 else (-1, -1, self.width)
        for d in range(abs(delta)):
            self.moveBlock(i, 0, i + 1, self.width, 0, delta1, False)
            self.moveBlock(i, j, i + 1, j + delta1, 0, delta2, False)
            self.update(update)

    def rotateColumn(self, j, delta, update = True):
        i, delta1, delta2 = (self.height, 1, -self.height) if delta > 0 else (-1, -1, self.height)
        for d in range(abs(delta)):
            self.moveBlock(0, j, self.height, j + 1, delta1, 0, False)
            self.moveBlock(i, j, i + delta1, j + 1, delta2, 0, False)
            self.update(update)
   
    # The canvas stays on after the animation finished
    def __del__(self):
        self.pen.reset()
        self.pen.hideturtle()
        input("Press ENTER to proceed...")

def test(blockSize, blockNumber):
    canvas = PixelGrid(blockSize, blockNumber)
    for j in range(-blockNumber / 2, blockNumber / 2):
        for i in range(-blockNumber / 2, blockNumber / 2):
            canvas.drawPixel(i, j)
            
def test2(height, width):
    height, width = width, height
    canvas = PixelGrid(width, height)
    canvas.drawPixel(int(width / 3), int(height / 3))
    canvas.drawPixel(0, 0)
    canvas.fillArea(int(width / 3), int(height / 3), int(2 * width / 3), int(2 * height / 3))
    canvas.fillArea(0, 0, width, height)
    canvas.moveBlock(int(width / 4), int(height / 4), int(width / 2), int(height / 2), int(width / 4), int(height / 4))
    canvas.rotateRow(int(width / 2), 5)
    canvas.rotateColumn(int(width / 2), 5)

#test(4, 250)
#test2(18, 32)