import utility # my own utility.pl file
import re # finditer, subn

class Medicine:
	def __init__(self, replacements, startingMolecule):
		self.startingMolecule = startingMolecule
		self.replacements = []
		self.reversed = []
		self.shortestPath = 0
		for replacement in replacements:
			# Parse 'Al => ThF'
			inputMolecule, outputMolecule = replacement.split(' => ')
			self.replacements.append((inputMolecule, outputMolecule))
			self.reversed.append((outputMolecule, inputMolecule))
		# order by the greatest reduction first
		self.reversed.sort(key = lambda a: len(a[1]) - len(a[0]))

	def __str__(self):
		return f'{self.startingMolecule}\n{self.replacements}'

	def replaceAll(self, molecules, replacements, target = 'e'):
		results = set()
		for molecule in molecules:
			for input, output in replacements:
				if output == target:
					if input == molecule:
						return {target}
				else:
					for match in re.finditer(input, molecule):
						results.add(molecule[:match.start()] + output + molecule[match.end():])
		return results
	
	def distinctMoleculesAfterOneReplacement(self):
		return len(self.replaceAll({self.startingMolecule}, self.replacements, target = None))
	
	def shortestPathTo(self, target = 'e'):
		currentMolecule = self.startingMolecule
		steps = 0
		foundReplacement = True
		while foundReplacement:
			if currentMolecule == target:
				return steps
			foundReplacement = False
			for input, output in self.reversed:
				if input in currentMolecule:
					# Greedily replace with the highest order replacement possible
					currentMolecule, newSteps = re.subn(input, output, currentMolecule)
					#print(f'{newSteps} x {input} -> {output}')
					steps += newSteps
					foundReplacement = True
					break
		return -1

smallExample = [
	'e => H',
	'e => O',
	'H => HO',
	'H => OH',
	'O => HH']
assert Medicine(smallExample, 'HOH').distinctMoleculesAfterOneReplacement() == 4
assert Medicine(smallExample, 'HOHOHO').distinctMoleculesAfterOneReplacement() == 7
assert Medicine(smallExample, 'HOH').shortestPathTo("e") == 3
assert Medicine(smallExample, 'HOHOHO').shortestPathTo("e") == 6

# Display info message
print("Give a list of molecule replacement and the molecule itself:\n")
replacements = utility.readInputList()
startingMolecule = replacements.pop()
replacements.pop() # pop emtpy line between the dictionary and the starting molecule

# Display results
medicine = Medicine(replacements, startingMolecule)
print(f'{medicine.distinctMoleculesAfterOneReplacement() = }')
print(f'{medicine.shortestPathTo("e") = }')
