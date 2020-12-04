import utility # my own utility.pl file

# To what floor do the instructions take Santa?
def lastFloor(instructionString):
	numOpenParenthesis = instructionString.count('(')
	numCloseParenthesis = instructionString.count(')')
	return numOpenParenthesis - numCloseParenthesis

assert lastFloor('(())') == 0
assert lastFloor('()()') == 0
assert lastFloor('(((') == 3
assert lastFloor('(()(()(') == 3
assert lastFloor('))(((((') == 3
assert lastFloor('())') == -1
assert lastFloor('))(') == -1
assert lastFloor(')))') == -3
assert lastFloor(')())())') == -3

# What is the position of the character that causes Santa to first enter the basement?
def firstEnteringBasement(instructionString):
	floorIncrement = {'(' : 1, ')' : -1}
	currentFloor = 0
	basement = -1

	for index, character in enumerate(instructionString):
		currentFloor += floorIncrement.get(character, 0) # increment with zero for non-() characters
		if currentFloor == basement:
			return index + 1 # basement is reached at this position

	return -1

assert firstEnteringBasement(')') == 1
assert firstEnteringBasement('()())') == 5

# Display info message
print("Give a string of '(' and ')' characters, where '(' means go up one floor, while ')' means go one floor down.\n");
instructionString = utility.readInputList(joinedWith = '')

# Display results
print(f"{lastFloor(instructionString) = }, {firstEnteringBasement(instructionString) = }")
