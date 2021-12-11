import utility # my own utility.py file
import numpy # array

class Board:
    def __init__(self, matrix):
        self.matrix = matrix
        self.drawn = numpy.copy(self.matrix)
        self.drawn.fill(True)
        self.isWinner = False
        
    def drawNumber(self, number):
        self.drawn = numpy.logical_and(self.drawn, self.matrix != number)
        self.calcIsWinner()
        return self
        
    def calcIsWinner(self):
        sumCol = self.drawn.sum(axis=0)
        sumRow = self.drawn.sum(axis=1)
        self.isWinner = 0 in sumCol or 0 in sumRow
    
    def score(self):
        return sum(self.matrix[self.drawn])

def finalBingoScore(data, part2=False):
    # Parse
    numbers = []
    boards = []
    currentBoard = []
    for line in data:
        if not numbers:
            numbers = list(map(int, line.split(',')))
        elif not line:
            if currentBoard:
                boards.append(Board(numpy.array(currentBoard)))
                currentBoard = []
        else:
            row = numpy.array(list(map(int, line.split())))
            currentBoard.append(row)
    if currentBoard:
        boards.append(Board(numpy.array(currentBoard)))

    # Simulate
    winners = 0
    for number in numbers:
        for currentBoard in boards:
            if not currentBoard.isWinner and currentBoard.drawNumber(number).isWinner:
                winners += 1
            if part2 and winners == len(boards) or not part2 and winners == 1:
                # Return
                value = currentBoard.score() * number
                print(value)
                return value
    
    return -1

# Verify test cases
smallExample = '''
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
'''.strip().split('\n')
assert(finalBingoScore(smallExample) == 4512)
assert(finalBingoScore(smallExample, part2=True) == 1924)

# Display info message
print("\nGive a list of drawn numbers and table values:");
bingoSubsystem = utility.readInputList()

# Display results
print (f'{finalBingoScore(bingoSubsystem) = }')
print (f'{finalBingoScore(bingoSubsystem, part2=True) = }')