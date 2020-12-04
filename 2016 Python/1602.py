import utility # my own utility.pl file
import cmath # complex numbers

class Keypad:
    def __init__(self, keypad, startingPosition = '5'):
        self.keypad = [line.split() for line in keypad]
        for row, line in enumerate(self.keypad):
            if line.count(startingPosition) > 0:
                self.i, self.j = row, line.index(startingPosition)
    
    def move(self, instructions):
        deltas = {'U': (0,-1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
        for move in instructions:
            (dJ, dI) = deltas[move]
            newJ = self.j + dJ
            newI = self.i + dI
            if 0 <= newI < len(self.keypad) and 0 <= newJ < len(self.keypad[newI]) and self.keypad[newI][newJ] != '0':
                (self.i, self.j) = (newI, newJ)
    
    def buttonsToPush(self, instructionList):
        buttons = ''
        for instructions in instructionList:
            self.move(instructions)
            buttons += self.keypad[self.i][self.j]
        return buttons

keypad1 = [
    '1 2 3',
    '4 5 6',
    '7 8 9']
keypad2 = [
    '0 0 1 0 0',
    '0 2 3 4 0',
    '5 6 7 8 9',
    '0 A B C 0',
    '0 0 D 0 0']
smallExample = [
    'ULL',
    'RRDDD',
    'LURDL',
    'UUUUD']
assert(Keypad(keypad1).buttonsToPush(smallExample) == '1985')
print(Keypad(keypad2).buttonsToPush(smallExample))
assert(Keypad(keypad2).buttonsToPush(smallExample) == '5DB3')

# Display info message
print("Give a list of keypad movement instructions:\n");
instructionList = utility.readInputList()

# Display results
print (f'{Keypad(keypad1).buttonsToPush(instructionList) = }')
print (f'{Keypad(keypad2).buttonsToPush(instructionList) = }')
