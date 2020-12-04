import utility # my own utility.pl file

class Monorail:      
    def __init__(self, instructions):
        self.values = {'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0}
        self.currentInstruction = 0
        
        while 0 <= self.currentInstruction < len(instructions):
            self.execute(instructions[self.currentInstruction])
        print(self)
        self.currentInstruction = 0
        self.values['c'] = 1
        while 0 <= self.currentInstruction < len(instructions):
            self.execute(instructions[self.currentInstruction])
        print(self)
                
    def __str__(self):
        return '\n'.join([key + ': ' + value.__str__() for key, value in self.values.items()])
    
    # Add value or instruction to bin id
    def execute(self, instructionString):
        # Parse input string
        instructionTokens = instructionString.split()
        #print(f'{self.currentInstruction}: {instructionTokens}')
        command = instructionTokens[0]
        op1 = instructionTokens[1]
        op2 = '' if len(instructionTokens) < 3 else instructionTokens[2]
        increment = 1
        
        # Execute given command
        if command == 'cpy':
            newValue = int(op1) if op1.isnumeric() else self.values[op1]
            self.values[op2] = newValue
        elif command == 'inc':
            self.values[op1] = self.values[op1] + 1
        elif command == 'dec':
            self.values[op1] = self.values[op1] - 1
        elif command == 'jnz':
            checkVal = int(op1) if op1.isnumeric() else self.values[op1]
            increment = int(op2) if checkVal != 0 else 1
            
        self.currentInstruction += increment
        return self
            
    def value(self, id):
        return self.values[id]
    
smallExample = [
    'cpy 41 a',
    'inc a',
    'inc a',
    'dec a',
    'jnz a 2',
    'dec a']
assert Monorail(smallExample).value('a') == 42

# Display info message
print("Give monorail instruction list:\n")
instructions = utility.readInputList()

# Display results
print(f'{Monorail(instructions).value("a") = }')