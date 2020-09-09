import utility # my own utility.pl file
import re

def value(text):
	if len(text) == 0:
		return 0

	start = 1 if text[0] == '-' else 0
	if text[start:].isnumeric():
		return int(text)
	return 0

# Find the closest open bracket which is not closed yet either forward or backwards
def findBracket(text, start, open, close, isForward):
	count = 0
	end = len(text) if isForward else -1
	increment = 1 if isForward else -1
	
	for i in range(start, end, increment):
		if text[i] == open:
			count += 1
		if text[i] == close:
			count -= 1
		if isForward and count == -1 or not isForward and count == 1:
			return i
	return -1

def obliterate(jsonString, property):
	start = 0
	index = jsonString.find(property, start)
	while index >= 0:
		leftSquare = findBracket(jsonString, index, '[', ']', False)
		leftCurly = findBracket(jsonString, index, '{', '}', False)
		rightCurly = findBracket(jsonString, index, '{', '}', True)

		if leftSquare < leftCurly:
			assert leftCurly < rightCurly
			jsonString = jsonString[:leftCurly] + jsonString[rightCurly + 1:]
			start = leftCurly
		else:
			start = index + 1
		index = jsonString.find(property, start)
	print(jsonString)
	return jsonString

def sumNumbers(jsonString):
	splitJson = re.split('\[|\]|\{|\}|:|,', jsonString)
	return sum(value(text) for text in splitJson)

assert sumNumbers('[1,2,3]') == 6
assert sumNumbers('{"a":2,"b":4}') == 6
assert sumNumbers('[[[3]]]') == 3
assert sumNumbers('{"a":{"b":4},"c":-1}') == 3
assert sumNumbers('{"a":[-1,1]}') == 0
assert sumNumbers('[-1,{"a":1}]') == 0
assert sumNumbers('[]') == 0
assert sumNumbers('{}') == 0

assert sumNumbers(obliterate('[1,2,3]', 'red')) == 6
assert sumNumbers(obliterate('[1,{"c":"red","b":2},3]', 'red')) == 4
assert sumNumbers(obliterate('{"d":"red","e":[1,2,3,4],"f":5}', 'red')) == 0
assert sumNumbers(obliterate('{{"d":8},"e":[1,2,3,4],"d":"red","e":[1,2,3,4],{"f":5}}', 'red')) == 0
assert sumNumbers(obliterate('[1,"red",5]', 'red')) == 6

# Display info message
print("\nGive a list of strings with escape characters:\n");

jsonString = utility.readInputList()[0]
sumNum = sumNumbers(jsonString)
newJsonString = obliterate(jsonString, 'red')
newSum = sumNumbers(newJsonString)

# Display results
print (f'sumNum = {sumNum}, newSum = {newSum}')
