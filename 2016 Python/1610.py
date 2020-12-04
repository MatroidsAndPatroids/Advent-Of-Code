import utility # my own utility.pl file
import re # compile, match

class Bin:
    def __init__(self):
        self.lowId = self.highId = ''
        self.lowVal = self.highVal = -1
        
    def addValue(self, value):
        if self.lowVal < 0:
            self.lowVal = value
        elif value < self.lowVal:
            self.highVal = self.lowVal
            self.lowVal = value
        else:
            self.highVal = value
            
    def addDestinations(self, lowId, highId):
        self.lowId = lowId
        self.highId = highId
        
    def isComplete(self):
        return self.lowVal >= 0 and self.lowId and self.highVal >= 0 and self.highId
    
    def __str__(self):
        return f'{self.lowId = }, {self.lowVal = }, {self.highId = }, {self.highVal = }'

class BalanceBots:
    # Parse 'value 61 goes to bot 209'
    re_value = re.compile('value (?P<value>\d+) goes to (?P<destination>.*)')
    # Parse 'bot 200 gives low to bot 40 and high to bot 141'
    re_instruction = re.compile('(?P<source>.*) gives low to (?P<low>.*) and high to (?P<high>.*)')
    
    def __init__(self, instructions):
        self.values = {}
        
        for instruction in instructions:
            match = re.match(BalanceBots.re_value, instruction)
            if match:
                destination = match.group('destination')
                value = int(match.group('value'))
                self.add(destination, value)
            else:
                match = re.match(BalanceBots.re_instruction, instruction)
                source = match.group('source')
                lowId = match.group('low')
                highId = match.group('high')
                self.add(source, None, lowId, highId)
                
    def __str__(self):
        return '\n'.join([key + ': ' + value.__str__() for key, value in self.values.items()])
    
    # Add value or instruction to bin id
    def add(self, id, value, lowId = None, highId = None):
        if id not in self.values.keys():
            self.values[id] = Bin()
        
        currentBin = self.values[id]    
        if value != None:
            currentBin.addValue(value)
        else:
            currentBin.addDestinations(lowId, highId)
            
        if currentBin.isComplete():
            if currentBin.lowVal == 17 and currentBin.highVal == 61:
                print(id, currentBin)
            self.add(currentBin.lowId, currentBin.lowVal)
            self.add(currentBin.highId, currentBin.highVal)
            currentBin.__init__()
            
    def value(self, id):
        return self.values[id].lowVal
    
smallExample = [
    'value 5 goes to bot 2',
    'bot 2 gives low to bot 1 and high to bot 0',
    'value 3 goes to bot 1',
    'bot 1 gives low to output 1 and high to bot 0',
    'bot 0 gives low to output 2 and high to output 0',
    'value 2 goes to bot 2']
assert BalanceBots(smallExample).value('output 0') == 5
assert BalanceBots(smallExample).value('output 1') == 2
assert BalanceBots(smallExample).value('output 2') == 3

# Display info message
print("Give a file in a peculiar compressed format:\n")
instructions = utility.readInputList()

# Display results
bb = BalanceBots(instructions)
part2 = bb.value('output 0') * bb.value('output 1') * bb.value('output 2')
print(f'{part2 = }')