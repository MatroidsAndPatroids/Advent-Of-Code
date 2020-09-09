import utility # my own utility.pl file

def numberOfVowels(inputString, vowels = 'aeiou'):
	return sum(inputString.count(vowel) for vowel in vowels)

def twiceInARow(inputString):
	previousCharacter = ''
	for character in inputString:
		if character == previousCharacter:
			return True
		previousCharacter = character
	return False

def containForbidden(inputString, forbiddens = ["ab", "cd", "pq", "xy"]):
	return any(forbidden in inputString for forbidden in forbiddens)

# A string is nice if it has all three of these properties
# 1. it contains at least 3 vowels (aeiou only)
# 2. it contains at least on letter that appears twice in a row
# 3. it does not contain any of the forbidden strings (ab, cd, pq, xy)
def isNice(inputString):
	return numberOfVowels(inputString) >= 3 and twiceInARow(inputString) and not containForbidden(inputString)

assert isNice('ugknbfddgicrmopn')
assert isNice('aaa')
assert not isNice('jchzalrnumimnmhp')
assert not isNice('haegwjzuvuyypxyu')
assert not isNice('dvszwmarrgswjxmb')

def letterPairTwice(inputString):
	previousCharacter = ''
	for character in inputString:
		if previousCharacter:
			letterPairCount = inputString.count(previousCharacter + character)
			if letterPairCount >= 2:
				#print(f'{inputString} {previousCharacter + character} x {letterPairCount}')
				return True
		previousCharacter = character
	return False

def oneLetterBetweenSameTwoLetters(inputString):
	previousCharacter = ''
	characterBeforePrevious = ''
	for character in inputString:
		if character == characterBeforePrevious:
			#print(f'{inputString} {characterBeforePrevious + previousCharacter + character}')
			return True
		characterBeforePrevious = previousCharacter
		previousCharacter = character
	return False

# From now on a string is nice if it has all two of these properties
# 1. it contains a pair of any two letters that appears at least twice in the string without overlapping
# 2. it contains at least one letter which repeats with exactly one letter between them
def isNiceNew(inputString):
	return letterPairTwice(inputString) & oneLetterBetweenSameTwoLetters(inputString)

assert isNiceNew('qjhvhtzxzqqjkmpb')
assert isNiceNew('xxyxx')
assert not isNiceNew('uurcxstgmygtbstg')
assert not isNiceNew('ieodomkazucvgmuy')
assert not isNiceNew('aaa')
assert isNiceNew('aaaa')

# Display info message
print("\nGive a list of strings for which we find the nice ones, which are not naughty.\n");

inputStringList = utility.readInputList()

numOfNiceStrings = sum(isNice(s) for s in inputStringList)
numOfNewNiceStrings = sum(isNiceNew(s) for s in inputStringList)

# Display results
print (f'numOfNiceStrings = {numOfNiceStrings}')
print (f'numOfNewNiceStrings = {numOfNewNiceStrings}')

