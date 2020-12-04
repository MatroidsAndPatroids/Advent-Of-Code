import utility # my own utility.pl file
import numpy

# A 'present' is a rectangular cuboid represented by its 3 dimensions.
class Present:
	# Convert 1x2x3 format strings to [1,2,3] lists (aka. presents)
	def __init__(self, presentString):
		self.dimensions = sorted(list(map(int, presentString.split('x'))))
		
	def __str__(self):
		return 'x'.join(map(str, self.dimensions))

	# Tthe surface of the present plus the area of the smallest side
	def requiredWrappingPaper(self):
		dim = self.dimensions
		sideAreas = [dim[a] * dim[b] for a in range(len(dim)) for b in range(a)]
		wrappingPaper = 2 * sum(sideAreas)
		slack = min(sideAreas)
		return wrappingPaper + slack

	# Smallest perimeter plus the cubic volume
	def requiredRibbon(self):
		ribbonLength = 2 * (sum(self.dimensions) - max(self.dimensions))
		bowLength = numpy.prod(self.dimensions)
		return ribbonLength + bowLength

assert Present('2x3x4').requiredWrappingPaper() == 58
assert Present('1x1x10').requiredWrappingPaper() == 43
assert Present('2x3x4').requiredRibbon() == 34
assert Present('1x1x10').requiredRibbon() == 14

# Display info message
print("Give a list of 1x2x3 format strings representing the three dimensions of a present.\n");
inputList = utility.readInputList()

# Display results
totalRequiredWrappingPaper = sum(Present(x).requiredWrappingPaper() for x in inputList)
totalRequiredRibbon = sum(Present(x).requiredRibbon() for x in inputList)
print (f'{totalRequiredWrappingPaper = }, {totalRequiredRibbon = }')