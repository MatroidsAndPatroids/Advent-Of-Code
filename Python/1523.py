import utility # my own utility.pl file

class Computer:
	def __init__(self, instructionList):
		self.instructionList = instructionList
		self.reset()

	def reset(self, startA = 0, startB = 0):
		self.registers = {'a' : startA, 'b' : startB}
		self.currentInstruction = 0

	def __str__(self):
		if 0 <= self.currentInstruction < len(self.instructionList):
			return f'{self.currentInstruction}: {self.instructionList[self.currentInstruction]} {self.registers}'
		return f'{self.currentInstruction}: NAN {self.registers}'

	def execute(self, startA = 0, startB = 0):
		self.reset(startA, startB)

		while 0 <= self.currentInstruction < len(self.instructionList):
			instruction = self.instructionList[self.currentInstruction].replace(',', '').split(' ')
			command = instruction[0]
			argument = instruction[1]
			increment = 1
			print(f'{self} {instruction}')

			if command == 'hlf':
				self.registers[argument] >>= 1
			elif command == 'tpl':
				self.registers[argument] *= 3
			elif command == 'inc':
				self.registers[argument] += 1
			elif command == 'jmp':
				increment = int(argument)
			elif command == 'jie':
				if self.registers[argument] % 2 == 0:
					increment = int(instruction[2])
			elif command == 'jio':
				if self.registers[argument] == 1:
					increment = int(instruction[2])
			else:
				break

			self.currentInstruction += increment

		print(f'{self}')
		return self

smallExample = [
	'inc a',
	'jio a, +2',
	'tpl a',
	'inc a']

assert Computer(smallExample).execute(0, 0).registers['a'] == 2

# Display info message
print("\nGive a list of computer instructions:\n")

inputStringList = utility.readInputList()
computer = Computer(inputStringList).execute(0, 0)
print('\n' * 10)
computer.execute(1, 0)
# Display results
#print(computer.execute())

