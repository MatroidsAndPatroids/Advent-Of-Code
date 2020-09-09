import re
import utility # my own utility.pl file

class LigthBulbGrid:
	def __init__(self, height, width):
		self.gridList = [0] * height * width
		self.height = height
		self.width = width
		LigthBulbGrid.evaluate = {
			'turn on' : (lambda state: 1),
			'turn off' : (lambda state: 0),
			'toggle' : (lambda state: 1 - state)}
		LigthBulbGrid.evaluateNew = {
			'turn on' : (lambda state: state + 1),
			'turn off' : (lambda state: max(0, state - 1)),
			'toggle' : (lambda state: state + 2)}

	def countLightOn(self):
		return sum(self.gridList)

	def execute(self, jumpTable, command, i1, j1, i2, j2):
		assert 0 <= i1 <= i2 < self.height
		assert 0 <= j1 <= j2 < self.width
		rowSegmentLength = j2 - j1 + 1
		for index in range(i1 * self.width + j1, i2 * self.width + j1 + 1, self.width):
			# for each row update the subrow using the given command
			self.gridList[index:index+rowSegmentLength] = [jumpTable[command](value) for value in self.gridList[index:index+rowSegmentLength]]
		return self

	def executeInstruction(self, jumpTable, instructionString):
		if not instructionString:
			return self

		instructions = re.split(',| ', instructionString)
		if len(instructions) == 7:
			# concatenate ['turn', 'on'] into ['turn on']
			instructions[0:2] = [f'{instructions[0]} {instructions[1]}']
		#print(instructions)
		assert len(instructions) == 6
		
		command = instructions[0]
		i1 = int(instructions[1])
		j1 = int(instructions[2])
		i2 = int(instructions[4])
		j2 = int(instructions[5])
		self.execute(jumpTable, command, i1, j1, i2, j2)
		return self

assert LigthBulbGrid(1000, 1000).executeInstruction(LigthBulbGrid.evaluate, 'turn on 0,0 through 999,999').countLightOn() == 1000000
assert LigthBulbGrid(1000, 1000).executeInstruction(LigthBulbGrid.evaluate, 'toggle 0,0 through 999,0').countLightOn() == 1000
assert LigthBulbGrid(1000, 1000).executeInstruction(LigthBulbGrid.evaluate, 'turn on 499,499 through 500,500').countLightOn() == 4

assert LigthBulbGrid(1000, 1000).executeInstruction(LigthBulbGrid.evaluateNew, 'turn on 0,0 through 0,0').countLightOn() == 1
assert LigthBulbGrid(1000, 1000).executeInstruction(LigthBulbGrid.evaluateNew, 'toggle 0,0 through 999,999').countLightOn() == 2000000

# Display info message
print("\nGive a list of light bulb setting instructions:\n");

inputStringList = utility.readInputList()

grid = LigthBulbGrid(1000,1000)
for instruction in inputStringList:
	grid.executeInstruction(LigthBulbGrid.evaluate, instruction)

newGrid = LigthBulbGrid(1000,1000)
for instruction in inputStringList:
	newGrid.executeInstruction(LigthBulbGrid.evaluateNew, instruction)

# Display results
print (f'numOfLigthBulbsOn = {grid.countLightOn()}')
print (f'numOfLigthBulbsOnNew = {newGrid.countLightOn()}')

