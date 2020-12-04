import utility # my own utility.pl file
import re # re.split
import operator # eq, gt, lt

# Parse 'Sue 1: goldfish: 9, cars: 0, samoyeds: 9'
class Aunt:
	comparators = {
		'cats': operator.gt,
		'trees': operator.gt,
		'pomeranians': operator.lt,
		'goldfish': operator.lt}

	def __init__(self, auntDescription):
		# Parse 'Sue 29: vizslas: 6, pomeranians: 3, akitas: 6'
		token = re.split(': |, ', auntDescription)
		self.name = token[0]
		self.things = {token[i]: int(token[i + 1]) for i in range(1, len(token), 2)}

	def __str__(self):
		return self.name + ': ' + self.things.__str__()

	def match(self, other, comparators = {}):
		return all(t not in other.things or comparators.get(t, operator.eq)(v, other.things[t]) \
				for t, v in self.things.items())

# Display info message
print("Give a list of aunt descriptions:\n")
auntDescriptions = utility.readInputList()
clue = 'Sue Clue: children: 3, cats: 7, samoyeds: 2, pomeranians: 3, akitas: 0, vizslas: 0, goldfish: 5, trees: 3, cars: 2, perfumes: 1'
realSue = Aunt(clue)

# Display results
aunts = [Aunt(description) for description in auntDescriptions]
matchingAunts = [aunt for aunt in aunts if aunt.match(realSue)]
matchingAunts2 = [aunt for aunt in aunts if aunt.match(realSue, Aunt.comparators)]

print(realSue)
print(f'Match 1: {[aunt.__str__() for aunt in matchingAunts]}')
print(f'Match 2: {[aunt.__str__() for aunt in matchingAunts2]}')