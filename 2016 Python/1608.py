import utility # my own utility.pl file
import turtlegrid # my own turtle grid drawing SquareGrid.py file
import re # split

class LittleScreen(turtlegrid.PixelGrid):
    def execute(self, instructions):
        # Parse 'rect 1x1' or 'rotate row y=0 by 5'
        re_instruction = re.compile('(rect|rotate row y|rotate column x)(?:=|(?: ))(\d+)(?: by |(?:x))(\d+)')
        jumpTable = {
            'rect': lambda x, y: self.fillArea(0, 0, y, x),
            'rotate row y': lambda y, delta: self.rotateRow(y, delta),
            'rotate column x': lambda x, delta: self.rotateColumn(x, delta)}
    
        for line in instructions:
            command, arg1, arg2 = re_instruction.match(line).groups()
            jumpTable[command](int(arg1), int(arg2))
        
        return self

smallExample = [
    'rect 3x2',
    'rotate column x=1 by 1',
    'rotate row y=0 by 4',
    'rotate column x=1 by 1']
assert LittleScreen(width = 7, height = 3).execute(smallExample).numPixels() == 6

# Display info message
print("Give a list of ligth switching instructions:\n")
instructions = utility.readInputList()

# Display results
print (f"{LittleScreen(width = 50, height = 6).execute(instructions).numPixels() = }")