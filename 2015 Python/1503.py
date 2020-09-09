import utility # my own utility.pl file
from collections import defaultdict

# The input should only contain 'v', '^', '<' and '>' characters
def checkInput(instructionString):
	numUp = instructionString.count('^')
	numDown = instructionString.count('v')
	numLeft = instructionString.count('<')
	numRight = instructionString.count('>')
	numOther = len(instructionString) - numUp - numDown - numLeft - numRight
	print(f"Check input: '^' = {numUp}, 'v' = {numDown}, '<' = {numLeft}, '>' = {numRight}, other = {numOther}\n")

# How many presents are at each location at the end of the delivery?
# numPlayer = 1 with Santa only and 2 with Robo-Santa included
def createPresentMap(instructionString, numPlayers):

	# position (x, y) is converted to 1000000 * x + y
	rowOffset = 1000000
	floorIncrement = {
		'>' : 1,
		'<' : -1,
		'v' : rowOffset,
		'^' : -rowOffset}

	currentLocation = [0] * numPlayers # starting position is 0 for each player
	numPresents = defaultdict(int)
	numPresents[0] = numPlayers # starting position already has #players presents
	turn = 0 # 0 = Santa's turn, 1 = Robo-Santa's

	for index, character in enumerate(instructionString):
		increment = floorIncrement.get(character, 0)
		if increment != 0:
			currentLocation[turn] += increment
			numPresents[currentLocation[turn]] += 1
			turn = (turn + 1) % numPlayers

	return numPresents

assert len(createPresentMap('>', 1)) == 2
assert len(createPresentMap('^>v<', 1)) == 4
assert len(createPresentMap('^v^v^v^v^v', 1)) == 2

assert len(createPresentMap('^v', 2)) == 3
assert len(createPresentMap('^>v<', 2)) == 3
assert len(createPresentMap('^v^v^v^v^v', 2)) == 11

# Display info message
print("\nGive a string of 'v', '^', '<' and '>' characters, where they mean go up, down, left and right respectively.\n");

instructionString = ''.join(utility.readInputList())

checkInput(instructionString)

# Display results
print(f"housesVisited = {len(createPresentMap(instructionString, 1))}, housesVisitedWithRoboSanta = {len(createPresentMap(instructionString, 2))}")

