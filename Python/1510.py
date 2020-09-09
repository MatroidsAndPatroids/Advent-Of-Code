import utility # my own utility.pl file

# Say out loud the given string of digits
def lookAndSay(numberString):
	say = ''
	count = 1

	for index, digit in enumerate(numberString):
		if index + 1 < len(numberString) and digit == numberString[index + 1]:
			count += 1
		else:
			say += str(count) + str(digit)
			count = 1
	#print(say)
	return say

assert lookAndSay('1') == '11'
assert lookAndSay('11') == '21'
assert lookAndSay('21') == '1211'
assert lookAndSay('1211') == '111221'
assert lookAndSay('111221') == '312211'

def lengthAfterIteration(inputDigits, numIter):
	for i in range(numIter):
		inputDigits = lookAndSay(inputDigits)
	print(f'{numIter} times length = {len(inputDigits)}')
	return len(inputDigits)

# Display info message
print("\nGive a string of digits:\n");

inputDigits = utility.readInputList()[0]

# Display results
lengthAfterIteration(inputDigits, 40)
lengthAfterIteration(inputDigits, 50)

