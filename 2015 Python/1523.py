import utility # my own utility.pl file

class Computer:
	# Jump table: register, argument -> registerNew, increment
	jumpTable = {
		'hlf': lambda reg, dummy: (reg >> 1, 1),
		'tpl': lambda reg, dummy: (3 * reg, 1),
		'inc': lambda reg, dummy: (reg + 1, 1),
		'jmp': lambda reg, arg: (reg, arg),
		'jie': lambda reg, arg: (reg, arg if reg % 2 == 0 else 1),
		'jio': lambda reg, arg: (reg, arg if reg == 1 else 1)}
	
	def __init__(self, startA = 0, startB = 0):
		self.registers = {'a' : startA, 'b' : startB}
		self.currentInstruction = 0 # instruction pointer

	def __str__(self):
		return f'{self.currentInstruction = }, {self.registers = }'

	def execute(self, instructions):
		while 0 <= self.currentInstruction < len(instructions):
			# Parse 'jio a, +2'
			instruction = instructions[self.currentInstruction].replace(',', '').split(' ')
			command = instruction[0]
			register = instruction[1]
			argument = int(instruction[2]) if len(instruction) > 2 else 0
			if register not in 'ab': # jmp command has its argument at the register's place
				argument = int(register)
				register = 'a'
			# Apply the jumptable and increase the instruction pointer
			self.registers[register], increment = self.jumpTable[command](self.registers[register], argument)
			self.currentInstruction += increment
		return self

smallExample = [
	'inc a',
	'jio a, +2',
	'tpl a',
	'inc a']
assert Computer().execute(smallExample).registers['a'] == 2

# Display info message
print("Give a list of computer instructions:\n")
instructions = utility.readInputList()

# Display results
print(f'First run: {Computer().execute(instructions)}')
print(f'Second run: {Computer(1, 0).execute(instructions)}')

