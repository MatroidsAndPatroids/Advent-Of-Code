import utility # my own utility.pl file

def toNumberList(password):
	return [ord(character) for character in password]

def toString(numberList):
	return ''.join([chr(number) for number in numberList])

forbidden = toNumberList('iol')
a = ord('a')
z = ord('z')

def increment(number):
	if number in forbidden:
		return number + 2
	if number == z:
		return a
	return number + 1

def next(numberList):
	for i in range(len(numberList) - 1, -1, -1):
		numberList[i] = increment(numberList[i])
		if numberList[i] != a:
			break
	return numberList

def straightThree(numberList):
	for i in range(len(numberList) - 2):
		if numberList[i] + 2 == numberList[i + 1] + 1 == numberList[i + 2]:
			return True
	return False

assert straightThree(toNumberList('hijklmmn'))
assert not straightThree(toNumberList('abbceffg'))
assert not straightThree(toNumberList('abbcegjk'))

def doublePair(numberList):
	numPair = 0
	prevWasPair = False
	for i in range(len(numberList) - 1):
		if prevWasPair:
			prevWasPair = False
			continue
		if numberList[i] == numberList[i + 1]:
			prevWasPair = True
			numPair += 1
		if numPair == 2:
			return True
	return False

assert straightThree(toNumberList('abcdffaa'))
assert doublePair(toNumberList('abcdffaa'))
assert straightThree(toNumberList('abcdffaa')) and doublePair(toNumberList('abcdffaa'))
assert straightThree(toNumberList('ghjaabcc')) and doublePair(toNumberList('ghjaabcc'))

# A password is valid if it meets all three of these requirements
# 1. includes one increasing straight of at least three letters, like abc
# 2. does not contain the letters i, o, or l
# 3. contains at least two different, non-overlapping pairs of letters, like aa
def findNextValid(password):
	# Increment first in case it was already valid
	nextNumberList = next(toNumberList(password))
	# Preprocess ('ghijklmn' becomes 'ghjaaaaa')
	for i in range(len(nextNumberList)):
		if nextNumberList[i] in forbidden:
			nextNumberList[i] += 1
			nextNumberList[i + 1:] = (len(nextNumberList) - i - 1) * [a]
			break
	while not straightThree(nextNumberList) or not doublePair(nextNumberList):
		nextNumberList = next(nextNumberList)
	return toString(nextNumberList)

assert findNextValid('abcdefgh') == 'abcdffaa'
assert findNextValid('ghijklmn') == 'ghjaabcc'

# Display info message
print("Give a password:\n");
password = utility.readInputList(joinedWith = '')

# Display results
nextPassword = findNextValid(password)
nextPasswordAfterThat = findNextValid(nextPassword)
print(f'{password} -> {nextPassword} -> {nextPasswordAfterThat}')

#cqjxjnds
#cqjxxyzz
#cqkaabcc