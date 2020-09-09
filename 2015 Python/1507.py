import utility # my own utility.pl file

# A single wire representing holding a value of a gate
# Each wire refers to the main wire container, which is a WireName->WireValue dictionary
class Wire:
	def __init__(self, dictionary, expression):
		Wire.maxValue = 65535
		self.dictionary = dictionary
		self.value = -1
		self.expression = expression.split(' ')
		assert len(self.expression) > 2
		self.name = self.expression[-1]
		self.expression[-2:] = []
		assert self.name not in self.dictionary
		self.dictionary[self.name] = self

	def __str__(self):
		return f"{self.name} = {self.expression} = {self.value}"

	def __repr__(self):
		return self.__str__()

	def evaluate(self, symbol):
		if symbol.isnumeric():
			val = int(symbol)
			assert 0 <= val <= Wire.maxValue
			return val
		assert symbol in self.dictionary
		return self.dictionary[symbol].getValue()

	def getValue(self):
		if self.value > -1:
			return self.value

		exprArgs = len(self.expression)
		if exprArgs == 1:
			# literal
			self.value = self.evaluate(self.expression[0])
		elif exprArgs == 2:
			# unary operator
			operator = self.expression[0]
			assert operator == 'NOT'
			arg1 = self.evaluate(self.expression[1])
			self.value = Wire.maxValue - arg1
		else:
			# binary operator
			assert exprArgs == 3
			operator = self.expression[1]
			arg1 = self.evaluate(self.expression[0])
			arg2 = self.evaluate(self.expression[2])
			if self.expression[1] == 'AND':
				self.value = arg1 & arg2
			elif self.expression[1] == 'OR':
				self.value = arg1 | arg2
			elif self.expression[1] == 'LSHIFT':
				self.value = arg1 << arg2
			elif self.expression[1] == 'RSHIFT':
				self.value = arg1 >> arg2
			else:
				assert false and "Unknown operator error"
		
		self.value %= Wire.maxValue
		return self.value

testInstructions = [
	'123 -> x',
	'456 -> y',
	'x AND y -> d',
	'x OR y -> e',
	'x LSHIFT 2 -> f',
	'y RSHIFT 2 -> g',
	'NOT x -> h',
	'NOT y -> i']

testWires = {}
for instruction in testInstructions:
	if instruction:
		Wire(testWires, instruction)

assert testWires['d'].getValue() == 72
assert testWires['e'].getValue() == 507
assert testWires['f'].getValue() == 492
assert testWires['g'].getValue() == 114
assert testWires['h'].getValue() == 65412
assert testWires['i'].getValue() == 65079
assert testWires['x'].getValue() == 123
assert testWires['y'].getValue() == 456

# Display info message
print("\nGive a list of wiring instructions:\n");

inputStringList = utility.readInputList()

Wires = {}
for instruction in inputStringList:
	if instruction:
		Wire(Wires, instruction)

# Display results
valueOfWireA = Wires["a"].getValue()

for name, wire in Wires.items():
	print(wire)

NewWires = {}
for instruction in inputStringList:
	if instruction:
		Wire(NewWires, instruction)

NewWires["b"].value = valueOfWireA

for name, wire in Wires.items():
	print(wire)

newValueOfWireA = NewWires["a"].getValue()

print('\n\n\n\n')
for name, wire in NewWires.items():
	print(wire)

print (f'wire a: {valueOfWireA}')
print (f'new wire a: {newValueOfWireA}')

