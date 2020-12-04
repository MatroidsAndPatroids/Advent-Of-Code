import utility # my own utility.pl file

# A set of wires each with a lower case identifier and a signal provided by a gate.
class Circuit:
	operator = {
		'AND':    lambda x, y: x & y, # bitwise AND
		'OR':     lambda x, y: x | y, # bitwise OR
		'NOT':    lambda x, y: ~y & 0xFFFF,  # bitwise inversion, only one actual operand
		'LSHIFT': lambda x, y: (x << y) & 0xFFFF, # left-shift
		'RSHIFT': lambda x, y: x >> y, # right-shift
		'537':     lambda x, y: y}  # direct assignment, only one actual operand (537 looks like the word SET)

	def __init__(self, instructionList):
		self.wireValue = {} 
		for instruction in instructionList:
			# 'dd RSHIFT 2 -> de' string becomes {'de': 'dd RSHIFT 2'} in the dictionary
			expression, targetWire = instruction.split(' -> ')
			self.wireValue[targetWire] = expression

	def __str__(self):
		lines = ''
		for wireId, value in self.wireValue:
			lines += f'{wireId} -> {value}\n'
		return lines

	# Calculate and return the value of a given wire identified by its ID
	def getValue(self, wireId):
		# For integer or integer string just return as integer
		if wireId.isnumeric():
			return int(wireId)
		
		paddedExpression = '537 537 ' + str(self.wireValue[wireId])
		# 'dd RSHIFT 2' -> ['537', '537', 'dd', 'RSHIFT','2'], and 'dd' -> ['537', '537', '537', '537', 'dd']
		wireId1, gate, wireId2 = paddedExpression.split()[-3:]
		value = self.operator[gate](self.getValue(wireId1), self.getValue(wireId2))
		
		# overwrite the dictionary expression with its calculated value
		self.wireValue[wireId] = value
		return value

smallExample = [
	'123 -> x',
	'456 -> y',
	'x AND y -> d',
	'x OR y -> e',
	'x LSHIFT 2 -> f',
	'y RSHIFT 2 -> g',
	'NOT x -> h',
	'NOT y -> i']
smallCircuit = Circuit(smallExample)

assert smallCircuit.getValue('d') == 72
assert smallCircuit.getValue('e') == 507
assert smallCircuit.getValue('f') == 492
assert smallCircuit.getValue('g') == 114
assert smallCircuit.getValue('h') == 65412
assert smallCircuit.getValue('i') == 65079
assert smallCircuit.getValue('x') == 123
assert smallCircuit.getValue('y') == 456

# Display info message
print("Give a list of wiring instructions:\n");
expressionList = utility.readInputList()

# Display results
valueOfWireA = Circuit(expressionList).getValue('a')
Circuit2 = Circuit(expressionList)
Circuit2.wireValue['b'] = valueOfWireA
valueOfWireA2 = Circuit2.getValue('a')
print (f'{valueOfWireA = }, {valueOfWireA2 = }')

