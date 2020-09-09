import utility # my own utility.pl file

def appendElement(dictionary, key, element):
	if key in dictionary:
		dictionary[key].append(element)
	else:
		dictionary[key] = [element]


# Parse 'Al => ThF'
class Medicine:
	def __init__(self, replacements, molecule):
		self.molecule = molecule
		self.replacements = {}
		self.shortestPath = 0
		for replacement in replacements:
			pair = replacement.split(' => ')
			assert len(pair) == 2
			key = pair[0]
			element = pair[1]
			appendElement(self.replacements, key, element)

	def __str__(self):
		text = f'{self.molecule}\n'
		for key, value in self.replacements.items():
			text += f"{key} => [{' '.join(value)}]\n"
		return text

	def countDifferentResults(self):
		results = {}
		for key, value in self.replacements.items():
			start = self.molecule.find(key, 0)
			while start >= 0:
				for element in value:
					newMolecule = self.molecule[:start] + element + self.molecule[start + len(key):]
					if newMolecule in results:
						results[newMolecule] += 1
					else:
						results[newMolecule] = 1
				start = self.molecule.find(key, start + 1)
		return len(results)

	def shortestSubPath(self, subMolecule, pathLength):
		#print(f'{pathLength} {subMolecule}')
		if subMolecule == 'e':
			# goal reached
			self.shortestPath = pathLength
		if pathLength >= self.shortestPath:
			# solution is not optimal, prune tree
			return

		for key, value in self.replacements.items():
			for element in value:
				start = subMolecule.find(element, 0)
				while start >= 0:
					newMolecule = subMolecule[:start] + key + subMolecule[start + len(element):]
					self.shortestSubPath(newMolecule, pathLength + 1)
					start = subMolecule.find(element, start + 1)

	def shortestPathToElectron(self):
		self.shortestPath = 1000000
		self.shortestSubPath(self.molecule, 0)
		return self.shortestPath

smallExample = [
	'e => H',
	'e => O',
	'H => HO',
	'H => OH',
	'O => HH']

assert Medicine(smallExample, 'HOH').countDifferentResults() == 4
assert Medicine(smallExample, 'HOH').shortestPathToElectron() == 3
assert Medicine(smallExample, 'HOHOHO').countDifferentResults() == 7
assert Medicine(smallExample, 'HOHOHO').shortestPathToElectron() == 6

# Display info message
print("\nGive a list of molecule replacement and the molecule itself:\n")

inputStringList = utility.readInputList()
medicine = Medicine(inputStringList[:-2], inputStringList[-1])

# Display results
print(medicine)
print(medicine.countDifferentResults())
print(medicine.shortestPathToElectron())

