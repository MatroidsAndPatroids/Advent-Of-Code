import utility # my own utility.pl file
import math # prod

class Sleigh:
	def __init__(self, weightList, numGroups):
		self.weights = [int(weight) for weight in weightList]
		self.weights.reverse()
		self.cumulative = [sum(self.weights[i] for i in range(k)) for k in range(1, 1 + self.size())]
		self.groupWeight = int(sum(weight for weight in self.weights) / numGroups)
		self.solution = []

	def __str__(self):
		return f'{self.solution}, QE = {self.solutionGroupQE()}, lastQE = {self.lastGroupQE()}'

	def QE(group):
		return math.prod(group)

	def size(self):
		return len(self.weights)

	def solutionGroupQE(self):
		if self.solution and self.solution[0]:
			return Sleigh.QE(self.solution[0])
		return -1

	def lastGroupSize(self):
		if self.solution[-1]:
			return len(self.solution[-1])
		return 1000

	def lastGroupQE(self):
		if self.solution[-1]:
			return Sleigh.QE(self.solution[-1])
		return 1000

	def findSolution(self, group, remaining, last):
		currentWeight = sum(weight for weight in group)
		if self.groupWeight < currentWeight \
		or self.lastGroupSize() < len(group) \
		or self.lastGroupSize() == len(group) and self.lastGroupQE() < Sleigh.QE(group):
			# Dead end, prune tree
			return self
		if self.groupWeight == currentWeight:
			self.solution[-1] = group
			print(self)
			return self

		for i in range(last, len(remaining)):
			r = self.findSolution(group + [remaining[i]], remaining, i + 1)

		return self

	def bestConfiguration(self):
		self.solution = []
		remaining = self.weights

		while remaining:
			self.solution.append([])
			self.findSolution([], remaining, 0)
			self.solution[-1].reverse()
			# Subtract elements or the last group from the list of remaining elements
			remaining = [weight for weight in remaining if weight not in self.solution[-1]]

		print(f'Final solution: {self}')
		return self

smallExample = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]
assert Sleigh(smallExample, 3).bestConfiguration().solutionGroupQE() == 99
assert Sleigh(smallExample, 4).bestConfiguration().solutionGroupQE() == 44

# Display info message
print("Give a list of sleigh weights:\n")
inputStringList = utility.readInputList()

# Display results
print(f'QE3 = {Sleigh(inputStringList, 3).bestConfiguration().solutionGroupQE()}')
print(f'QE4 = {Sleigh(inputStringList, 4).bestConfiguration().solutionGroupQE()}')


