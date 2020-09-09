import utility # my own utility.pl file
import numpy

# A 'present' is a rectangular cuboid represented by its 3 dimensions.

# Convert 1x2x3 format strings to [1,2,3] lists (aka. presents)
def stringToPresent(presentString):
	if not presentString:
		return [0,0,0]

	dimensionStringList = presentString.split('x')
	return list(map(int, dimensionStringList))

# the surface of the present plus the area of the smallest side
def requiredWrappingPaper(present):
	sideAreaList = [x * y for x in present for y in present]
	squareList = [x * x for x in present]
	maxEdge = max(1, max(present))
	smallestSide = int(numpy.prod(present) / maxEdge)

	return sum(sideAreaList) - sum(squareList) + smallestSide

assert requiredWrappingPaper(stringToPresent('2x3x4')) == 58
assert requiredWrappingPaper(stringToPresent('1x1x10')) == 43

# smallest perimeter plus the cubic volume
def requiredRibbon(present):
	maxSide = max(present)
	ribbonLength = 2 * (sum(present) - maxSide)

	bowLength = numpy.prod(present)

	return ribbonLength + bowLength

assert requiredRibbon(stringToPresent('2x3x4')) == 34
assert requiredRibbon(stringToPresent('1x1x10')) == 14

# Display info message
print("\nGive a list of 1x2x3 format strings representing the three dimensions of a present.\n");

inputList = utility.readInputList()

presentList = [stringToPresent(x) for x in inputList]
requiredWrappingPaperList = [requiredWrappingPaper(x) for x in presentList]
requiredRibbonList = [requiredRibbon(x) for x in presentList]

print (f'totalRequiredWrappingPaper = {sum(requiredWrappingPaperList)}, totalRequiredRibbon = {sum(requiredRibbonList)}')