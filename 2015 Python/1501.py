import utility # my own utility.pl file

# The input should only contain '(' and ')' characters
def checkInput(instructionString):
	numOpenParenthesis = instructionString.count('(')
	numCloseParenthesis = instructionString.count(')')
	numOtherCharacters = len(instructionString) - numOpenParenthesis - numCloseParenthesis
	print(f"Check input: '(' = {numOpenParenthesis}, ')' = {numCloseParenthesis}, other = {numOtherCharacters}\n")

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

	floorIncrement = {
		'(' : 1,
		')' : -1}
	currentFloor = 0
	firstEnteringBasement = -1
	basement = -1

	for index, character in enumerate(instructionString):
		increment = floorIncrement.get(character, 0)
		currentFloor += increment
		if currentFloor == basement:
			firstEnteringBasement = index + 1
			break

	return firstEnteringBasement

assert firstEnteringBasement(')') == 1
assert firstEnteringBasement('()())') == 5

# Display info message
print("\nGive a string of '(' and ')' characters, where '(' means go up one floor, while ')' means go one floor down.\n");

instructionString = utility.readInputList()

checkInput(instructionString[0])

# Display results
print(f"lastFloor = {lastFloor(instructionString)}, firstEnteringBasement = {firstEnteringBasement(instructionString)}")
