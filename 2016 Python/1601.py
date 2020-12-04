import utility # my own utility.pl file
import SquareGrid # my own turtle grid drawing SquareGrid.py file
import collections # defaultdict

class Grid:
    def __init__(self, displayOn = False):
        self.displayOn = displayOn
        self.history = collections.defaultdict(complex) # forces complex number keys for the dictionary
        self.currentLocation = 0 # Complex number
        self.history[self.currentLocation] = 1
        self.firstRevisit = None
        if displayOn:
            self.canvas = SquareGrid.SquareGrid(4, 250, 100, 50)
            x, y = self.getCoordinates()
            color = self.history[self.currentLocation]
            self.canvas.drawSquare(x, y, color)

    def __str__(self):
        text = f"Grid {self.getCoordinates()}\n"
        for location, density in self.history.items():
            text += f"({location}, {density})\n"
        return text

    # Location (complex number) -> Euclidean coordinates (x, y)
    def getCoordinates(self, location = None):
        if location == None:
            location = self.currentLocation
        return location.real, location.imag

    # Distance from coordinate 0
    def distance(self, location = None):
        x, y = self.getCoordinates(location)
        return abs(x) + abs(y)
    
    # Distance from coordinate 0
    def firstRevisitDistance(self):
        if self.firstRevisit == None:
            return -1
        return self.distance(self.firstRevisit)

    # Move along the instruction list and display movement if displayOn is true
    def move(self, instructionList):
        facing = 1j
        rotate = {'L': 1j, 'R': -1j}
        for instruction in instructionList:
            # Parse movement string formats: 'R2'
            turn = instruction[0]
            steps = int(instruction[1:])
            facing *= rotate[turn]
            
            for step in range(steps):
                self.currentLocation += facing
                
                if self.currentLocation in self.history:
                    self.history[self.currentLocation] += 1
                    if self.firstRevisit == None:
                        self.firstRevisit = self.currentLocation
                else:
                    self.history[self.currentLocation] = 1

                if self.displayOn:
                    x, y = self.getCoordinates()
                    color = self.history[self.currentLocation]
                    self.canvas.drawSquare(x, y, color)
        return self

# get some unit testing module here
assert(Grid().move(['R2', 'L3']).distance() == 5)
assert(Grid().move(['R2', 'R2', 'R2']).distance() == 2)
assert(Grid().move(['R5', 'L5', 'R5', 'R3']).distance() == 12)
assert(Grid().move(['R8', 'R4', 'R4', 'R8']).firstRevisitDistance() == 4)

# Display info message
print("Give a list of instructions:\n");
instructionList = utility.readInputList(joinedWith = '').split(', ')

# Display results
grid = Grid(True).move(instructionList)
finalDestination = grid.getCoordinates()
firstRevisit = grid.getCoordinates(grid.firstRevisit)
print (f'FinalDestination: {finalDestination}, FirstRevisit: {firstRevisit}')