import utility # my own utility.pl file

# Parse 'Sue 1: goldfish: 9, cars: 0, samoyeds: 9'
class Aunt:
	def __init__(self, descriptionString):
		self.things = {}
		list = descriptionString.split(' ')
		self.name = list[0] + ' ' + list[1][:-1]
		for index in range(2, len(list), 2):
			key = list[index][:-1]
			value = list[index + 1]
			if value[-1] == ',':
				value = value[:-1]
			self.things[key] = int(value)

	def __str__(self):
		text = self.name + ': '
		for key, value in self.things.items():
			text += f'{key}: {value}, '
		return text

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other):
		for key, value in self.things.items():
			if key in other.things and other.things[key] != value:
				return False
		return True

	def __ne__(self, other):
		return not self.__eq__(other)

	def __le__(self, other):
		for key, value in self.things.items():
			if key in other.things:
				if key == 'cats' or key == 'trees':
					if other.things[key] >= value:
						return False
				elif key == 'pomeranians' or key == 'goldfish':
					if other.things[key] <= value:
						return False
				else:
					if other.things[key] != value:
						return False
		return True

clue = 'Sue Clue: children: 3, cats: 7, samoyeds: 2, pomeranians: 3, akitas: 0, vizslas: 0, goldfish: 5, trees: 3, cars: 2, perfumes: 1'
clueAunt = Aunt(clue)
print(clueAunt)

# Display info message
print("\nGive a list of ingredient descriptions:\n")

auntList = []
descriptionList = utility.readInputList()
for description in descriptionList:
	auntList.append(Aunt(description))

matchingAunts = []
for aunt in auntList:
	if aunt == clueAunt:
		matchingAunts.append(aunt)

matchingAunts2 = []
for aunt in auntList:
	if aunt <= clueAunt:
		matchingAunts2.append(aunt)

# Display results
print('First attempt:')
for aunt in matchingAunts:
	print(aunt)

print('\nSecond attempt:')
for aunt in matchingAunts2:
	print(aunt)

