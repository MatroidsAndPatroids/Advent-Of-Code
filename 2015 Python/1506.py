import utility # my own utility.pl file
import re # match
import numpy # zeros, slice, clip

class LigthBulbGrid:
	jumpTable1 = {
		'turn on' : (lambda state: 1),
		'turn off' : (lambda state: 0),
		'toggle' : (lambda state: 1 - state)}
	jumpTable2 = {
		'turn on' : (lambda state: state + 1),
		'turn off' : (lambda state: state - 1),
		'toggle' : (lambda state: state + 2)}

	def __init__(self, height, width):
		self.height = height
		self.width = width
		self.grid = numpy.zeros((height, width), dtype = int)

	def lightsOn(self):
		return self.grid.sum()

	# Parse 'turn on 489,959 through 759,964'
	def execute(self, instructions, part2 = False):
		for line in instructions:
			jumpTable = LigthBulbGrid.jumpTable2 if part2 else LigthBulbGrid.jumpTable1
			
			match = re.match("(toggle|turn on|turn off) (\d+),(\d+) through (\d+),(\d+)", line)
			action = match.group(1)
			i1, j1, i2, j2 = map(int, match.group(2, 3, 4, 5))
			assert 0 <= i1 <= i2 < self.height
			assert 0 <= j1 <= j2 < self.width
			
			t = slice(i1, i2 + 1), slice(j1, j2 + 1)
			self.grid[t] = jumpTable[action](self.grid[t])
			self.grid.clip(min = 0)
		return self

if __name__ == '__main__':	
	assert LigthBulbGrid(1000, 1000).execute(['turn on 0,0 through 999,999']).lightsOn() == 1000000
	assert LigthBulbGrid(1000, 1000).execute(['toggle 0,0 through 999,0']).lightsOn() == 1000
	assert LigthBulbGrid(1000, 1000).execute(['turn on 499,499 through 500,500']).lightsOn() == 4
	
	assert LigthBulbGrid(1000, 1000).execute(['turn on 0,0 through 0,0'], True).lightsOn() == 1
	assert LigthBulbGrid(1000, 1000).execute(['toggle 0,0 through 999,999'], True).lightsOn() == 2000000
	
	# Display info message
	print("Give a list of light bulb setting instructions:\n");
	instructionList = utility.readInputList()
	
	# Display results
	numberOfBulbsOn = LigthBulbGrid(1000,1000).execute(instructionList).lightsOn()
	totalBrightness = LigthBulbGrid(1000,1000).execute(instructionList, True).lightsOn()
	print (f'{numberOfBulbsOn = }, {totalBrightness = }')
