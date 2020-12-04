import utility # my own utility.pl file

# Parse one integer from each line
class Eggnog:
	def __init__(self, containerList, eggnogLiters):
		self.eggnogLiters = eggnogLiters
		self.containers = sorted(list(map(int, containerList)), reverse = True)

	def __str__(self):
		s = f'{self.eggnogLiters}L eggnog in {len(self.containers)} containers: {self.containers.__str__()}\n'
		s += f'{self.numberOfDifferentSolutions = }\n{self.minimumNumberOfContainers = }, {self.differentMinimumContainers = }, '
		return s

	# Count the number of different solutions for a subtree
	def countSolutionsInSubTree(self, firstIndex, remainingLiters, numContainers):
		if remainingLiters == 0:
			if numContainers < self.minimumNumberOfContainers:
				self.minimumNumberOfContainers = numContainers
				self.differentMinimumContainers = 1
			elif numContainers == self.minimumNumberOfContainers:
				self.differentMinimumContainers += 1
			return 1
		elif remainingLiters < 0:
			return 0

		return sum(self.countSolutionsInSubTree(i + 1, remainingLiters - self.containers[i], numContainers + 1) \
				for i in range(firstIndex, len(self.containers)))

	def combinations(self):
		self.minimumNumberOfContainers = 1000000
		self.differentMinimumContainers = 0
		self.numberOfDifferentSolutions = self.countSolutionsInSubTree(0, self.eggnogLiters, 0)
		return self

smallExample = ['20', '15', '10', '5', '5']
smallEggnog = Eggnog(smallExample, 25).combinations()
assert smallEggnog.numberOfDifferentSolutions == 4
assert smallEggnog.minimumNumberOfContainers == 2
assert smallEggnog.differentMinimumContainers == 3

# Display info message
print("Give a list of container sizes in liters:\n")
containerList = utility.readInputList()

# Display results
print(Eggnog(containerList, 150).combinations())