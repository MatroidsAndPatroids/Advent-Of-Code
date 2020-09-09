import utility # my own utility.pl file

# Count the beginning/ending quotes, and \", \\, \x escape characters
def countEscapeCharacters(inputString):
	if not inputString:
		return 0
	shortString = inputString.replace('\\\\', '_').replace('\\\"', '_')
	octagonals = shortString.count('\\x')
	return len(inputString) - len(shortString) + 3 * octagonals + 2

assert countEscapeCharacters('""') == 2
assert countEscapeCharacters('"abc"') == 2
assert countEscapeCharacters('"aaa\\"aaa"') == 3
assert countEscapeCharacters('"\\x27"') == 5

# Encode the string once again with escape characters and find how much the length increased
def countNewEscapeCharactersAfterIncrease(inputString):
	if not inputString:
		return 0
	return inputString.count('"') + inputString.count('\\') + 2

assert countNewEscapeCharactersAfterIncrease('""') == 4
assert countNewEscapeCharactersAfterIncrease('"abc"') == 4
assert countNewEscapeCharactersAfterIncrease('"aaa\\"aaa"') == 6
assert countNewEscapeCharactersAfterIncrease('"\\x27"') == 5

# Display info message
print("\nGive a list of strings with escape characters:\n");

inputStringList = utility.readInputList()

"""
# Debugging
for inputString in inputStringList:
	count = countEscapeCharacters(inputString)
	countNew = countNewEscapeCharactersAfterIncrease(inputString)
	print(f'{count}\t{countNew}\t{inputString}')
"""

sumOfEscapeCharacters = sum(countEscapeCharacters(inputString) for inputString in inputStringList)
sumOfNewEscapeCharactersAfterIncrease = sum(countNewEscapeCharactersAfterIncrease(inputString) for inputString in inputStringList)

# Display results
print (f'sumOfEscapeCharacters = {sumOfEscapeCharacters}, sumOfNewEscapeCharactersAfterIncrease = {sumOfNewEscapeCharactersAfterIncrease}')

