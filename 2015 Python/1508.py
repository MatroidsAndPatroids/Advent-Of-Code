import utility # my own utility.pl file

# Count the beginning/ending quotes, and \", \\, \x## escape characters
def countEscapeCharacters(text):
	assert text[0] == text[-1] == '"'
	return len(text) - len(eval(text))

assert countEscapeCharacters('""') == 2
assert countEscapeCharacters('"abc"') == 2
assert countEscapeCharacters('"aaa\\"aaa"') == 3
assert countEscapeCharacters('"\\x27"') == 5

# Find out how much the length would increase, if we encode the string once again 
def countAdditionalEscapeCharacters(text):
	return text.count('"') + text.count('\\') + 2

assert countAdditionalEscapeCharacters('""') == 4
assert countAdditionalEscapeCharacters('"abc"') == 4
assert countAdditionalEscapeCharacters('"aaa\\"aaa"') == 6
assert countAdditionalEscapeCharacters('"\\x27"') == 5

def printDebugMessage(textList):
	for text in textList:
		count = countEscapeCharacters(text)
		countAdditional = countAdditionalEscapeCharacters(text)
		print(f'{count}\t{countAdditional}\t{text}')

# Display info message
print("Give a list of strings with escape characters:\n");
textList = utility.readInputList()
#printDebugMessage(textList)

# Display results
#numOfNiceStrings = sum(map(isNice1, textList))
sumOfEscapeCharacters = sum(map(countEscapeCharacters, textList))
sumOfAddtitionalEscapeCharacters = sum(map(countAdditionalEscapeCharacters, textList))
print (f'{sumOfEscapeCharacters = }, {sumOfAddtitionalEscapeCharacters = }')