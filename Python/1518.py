import utility # my own utility.pl file
import copy # use copy.deepcopy to copy 2-dimensional lists

# Parse one integer from each line
class LightGrid:
	def __init__(self, lightList):
		self.originalGrid = [list(lightLine) for lightLine in lightList]
		self.tmpGrid = copy.deepcopy(self.originalGrid)
		self.reset()

	def __str__(self):
		text = f'Step {self.step} with {self.lightsOn()} lights on:\n'
		for lightLine in self.grid:
			text += ''.join(lightLine) + '\n'
		return text

	def reset(self):
		self.grid = copy.deepcopy(self.originalGrid)
		self.step = 0

	def iterate(self, steps = 1, withRelight = False):
		if withRelight:
			self.relightCorners()
		for step in range(steps):
			self.step += 1

			for i in range(len(self.grid)):
				for j in range(len(self.grid[i])):
					self.tmpGrid[i][j] = self.newState(i, j)

			self.grid, self.tmpGrid = self.tmpGrid, self.grid # swap grids

			if withRelight:
				self.relightCorners()

		return self

	def newState(self, i, j):
		if self.grid[i][j] == '#':
			if 2 <= self.neighboursOn(i, j) <= 3:
				return '#'
		elif self.neighboursOn(i, j) == 3:
			return '#'
		return '.'

	def neighboursOn(self, i, j):
		i1 = max(0, i - 1)
		i2 = min(len(self.grid), i + 2)
		j1 = max(0, j - 1)
		j2 = min(len(self.grid[i]), j + 2)

		count = sum(line[j1:j2].count('#') for line in self.grid[i1:i2])
		count -= self.grid[i][j].count('#')
		#for line in self.grid[i1:i2]:
		#	print(''.join(line[j1:j2]))
		#print(f'{i}, {j}, {self.grid[i][j]} -> {count}')
		return count

	def lightsOn(self):
		return sum(line.count('#') for line in self.grid)

	def relightCorners(self):
		self.grid[0][0] = '#'
		self.grid[0][-1] = '#'
		self.grid[-1][0] = '#'
		self.grid[-1][-1] = '#'

smallExample = [
	'.#.#.#',
	'...##.',
	'#....#',
	'..#...',
	'#.#..#',
	'####..']

assert LightGrid(smallExample).iterate(4).lightsOn() == 4
assert LightGrid(smallExample).iterate(5, True).lightsOn() == 17

# Display info message
print("\nGive a grid of lights ('.' means OFF, '#' means ON):\n")

inputStringList = utility.readInputList()
grid = LightGrid(inputStringList)

# Display results
print(grid.iterate(100))
grid.reset()
print(grid.iterate(100, True))

