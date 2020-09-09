import utility # my own utility.pl file

# Parse one integer from each line
class Eggnog:
	def __init__(self, containerList, eggnogLiters):
		self.eggnogLiters = eggnogLiters
		self.containers = []
		self.minimumNumberOfContainers = 1000000
		self.differentMinimumContainers = 0
		for container in containerList:
			assert container.isnumeric()
			self.containers.append(int(container))

	def __str__(self):
		text = f'{self.eggnogLiters} Liters of eggnog in {len(self.containers)} containers: '
		for container in self.containers:
			text += f'{container}, '
		return text

	def __repr__(self):
		return self.__str__()

	def countSubTree(self, remainingContainers, remainingLiters, numContainers):
		if remainingLiters == 0:
			if numContainers < self.minimumNumberOfContainers:
				self.minimumNumberOfContainers = numContainers
				self.differentMinimumContainers = 1
			elif numContainers == self.minimumNumberOfContainers:
				self.differentMinimumContainers += 1
			return 1
		elif remainingLiters < 0:
			return 0

		count = 0
		for index in range(len(remainingContainers)):
			newRemainingContainers = remainingContainers[index + 1:]
			newRemainingLiters = remainingLiters - remainingContainers[index]
			count += self.countSubTree(newRemainingContainers, newRemainingLiters, numContainers + 1)
		return count

	def combinations(self):
		self.minimumNumberOfContainers = 1000000
		self.differentMinimumContainers = 0
		return self.countSubTree(self.containers, self.eggnogLiters, 0)

smallExample = ['20', '15', '10', '5', '5']
eggnogExample = Eggnog(smallExample, 25)
print(eggnogExample)
assert eggnogExample.combinations() == 4
assert eggnogExample.minimumNumberOfContainers == 2
assert eggnogExample.differentMinimumContainers == 3

# Display info message
print("\nGive a list of container sizes in liters:\n")

containerList = utility.readInputList()
eggnog = Eggnog(containerList, 150)
print(eggnog)

# Display results
print(f'Number of different combinations: {eggnog.combinations()}')
print(f'Minimum number of containers: {eggnog.minimumNumberOfContainers}, {eggnog.differentMinimumContainers} times')

