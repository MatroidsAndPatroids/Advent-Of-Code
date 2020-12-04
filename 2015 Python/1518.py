import utility # my own utility.pl file
import copy # use copy.deepcopy to copy 2-dimensional lists
import numpy # array
import scipy.ndimage # ndimage.generic_filter
Lights = __import__('1506') # use the same RouteFinder class from earlier

class LightAnimate(Lights.LigthBulbGrid):
	def __init__(self, initialConfiguration):
		height = len(initialConfiguration)
		width = 0 if height == 0 else len(initialConfiguration[0])
		# Create the original LightBulbGrid object
		Lights.LigthBulbGrid.__init__(self, height, width)
		self.step = 0
		# Parse 0-1 integer from each character
		self.grid = numpy.array([[int(light == '#') for light in line] for line in initialConfiguration])
		self.tmpGrid = copy.deepcopy(self.grid)
		
	def iterate(self, steps = 1, withRelight = False):
		self.relightCorners(withRelight)
		
		for step in range(steps):
			self.step += 1
			# Apply newState on the 3x3 blocks of all elements in grid with the edge being constant zero
			self.tmpGrid = scipy.ndimage.generic_filter(self.grid, self.newState, size=3, mode='constant', cval=0)
			self.grid, self.tmpGrid = self.tmpGrid, self.grid # swap grids
			self.relightCorners(withRelight)

		return self

	def newState(self, neighbours):
		lightOn = neighbours[4] # middle of the 3x3 block
		neighboursOn = neighbours.sum() # sum of the 3x3 block
		return int(3 <= neighboursOn <= 4) if lightOn else int(neighboursOn == 3)

	def relightCorners(self, withRelight):
		if withRelight:
			self.grid[[0, 0, -1, -1], [0, -1, 0, -1]] = 1

smallExample = [
	'.#.#.#',
	'...##.',
	'#....#',
	'..#...',
	'#.#..#',
	'####..']
assert LightAnimate(smallExample).iterate(4).lightsOn() == 4
assert LightAnimate(smallExample).iterate(5, withRelight = True).lightsOn() == 17

# Display info message
print("Give a ligth grid of initial configuration ('.' means OFF, '#' means ON):\n")
inputStringList = utility.readInputList()

# Display results
print(f'Initial configuration:  {LightAnimate(inputStringList).lightsOn()}')
print(f'Ligths after 100 steps: {LightAnimate(inputStringList).iterate(100).lightsOn()}')
print(f'100 steps with relight: {LightAnimate(inputStringList).iterate(100, True).lightsOn()}')
print(f'Ligths after 1000 steps: {LightAnimate(inputStringList).iterate(1000).lightsOn()}')
print(f'1000 steps with relight: {LightAnimate(inputStringList).iterate(1000, True).lightsOn()}')
print(f'Ligths after 10000 steps: {LightAnimate(inputStringList).iterate(10000).lightsOn()}')
print(f'10000 steps with relight: {LightAnimate(inputStringList).iterate(10000, True).lightsOn()}')
