import utility # my own utility.pl file
import re

def increment(character):
	if character == 'z':
		return 'a'
	return chr(ord(character) + 1)

def increasingLetters(password):
	maxCount = 0
	count = 1
	previousCharacter = ''
	for character in password:
		if not previousCharacter:
			x = 1
		elif character != 'a' and character == increment(previousCharacter):
			count += 1
		else:
			maxCount = max(count, maxCount)
			count = 1
		previousCharacter = character
	maxCount = max(count, maxCount)
	return maxCount

assert increasingLetters('hijklmmn') == 6
assert increasingLetters('abbceffg') == 2
assert increasingLetters('abbcegjk') == 2

def iol(password):
	return password.count('i') + password.count('o') + password.count('l')

def numPairs(password):
	count = 0
	previousCharacter = ''
	for character in password:
		if character == previousCharacter:
			count += 1
			previousCharacter = ''
		else:
			previousCharacter = character
	return count

# A password is valid if it meets all three of these requirements
# 1. includes one increasing straight of at least three letters, like abc
# 2. does not contain the letters i, o, or l
# 3. contains at least two different, non-overlapping pairs of letters, like aa
def isValid(password):
	return increasingLetters(password) >= 3 and iol(password) == 0 and numPairs(password) >= 2

assert isValid('abcdffaa')
assert isValid('ghjaabcc')

# Increment password string by character
def increasePassword(password):
	for i in range(len(password) - 1, 0, -1):
		password = password[:i] + increment(password[i]) + password[i + 1:]
		if password[i] != 'a':
			break
	return password

def findNextValid(password):
	nextPassword = increasePassword(password)
	while not isValid(nextPassword):
		nextPassword = increasePassword(nextPassword)
	return nextPassword

assert findNextValid('abcdefgh') == 'abcdffaa'
assert findNextValid('ghijklmn') == 'ghjaabcc'

# Display info message
print("\nGive a password:\n");

password = utility.readInputList()[0]
nextPassword = findNextValid(password)
nextPasswordAfterThat = findNextValid(nextPassword)

# Display results
print(f'{password} -> {nextPassword} -> {nextPasswordAfterThat}')

#cqjxjnds
#cqjxxyzz
#cqkaabcc