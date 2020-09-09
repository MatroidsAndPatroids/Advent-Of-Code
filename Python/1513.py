import utility # my own utility.pl file

class RouteFinder:
	def __init__(self, inputList = []):
		n = 100 # max number of locations
		self.locationCode = {}
		self.locationName = [''] * n
		self.distanceTable = [[0] * n for i in range(n)]
		
		for inputString in inputList:
			self.readDistance(inputString)

	def __str__(self):
		str = f"Size = {self.size()}\n"
		for i in range(self.size()):
			line = self.locationName[i].rjust(15, ' ')
			for j in range(self.size()):
				line += f"\t{self.distanceTable[i][j]}"
			str += line + '\n'
		return str

	def __repr__(self):
		return self.__str__()

	def size(self):
		return len(self.locationCode)

	# Location name -> location code dictionary. Creates new entry if location doesn't exist.
	def getLocationCode(self, location):
		if location not in self.locationCode:
			self.locationName[self.size()] = location
			self.locationCode[location] = self.size()
		return self.locationCode[location]

	# Parse distance string format: "London to Dublin = 464"
	def readDistance(self, distanceString):
		if not distanceString:
			return []

		distances = distanceString.split(' ')
		assert len(distances) == 11
		location1 = distances[0]
		location2 = distances[10][:-1] # last character was a dot
		distance = int(distances[3])
		if distances[2] == 'lose':
			distance = -distance

		code1 = self.getLocationCode(location1)
		code2 = self.getLocationCode(location2)
		self.distanceTable[code1][code2] += distance
		self.distanceTable[code2][code1] += distance

	# Find the Hamiltonian path of minimum or maximum lenght
	def findBestRoute(self, isMin):
		bestRoute = self.traverse([], self.locationName[0:self.size()], isMin)
		print(f"bestRoute = {bestRoute} = {self.cost(bestRoute)}")
		return self.cost(bestRoute)

	def cost(self, route):
		cost = 0
		prevLoc = route[-1]
		for location in route:
			if prevLoc:
				code1 = self.getLocationCode(location)
				code2 = self.getLocationCode(prevLoc)
				cost += self.distanceTable[code1][code2]
			prevLoc = location
		return cost

	def traverse(self, route, queue, isMin):
		#print(f"traverse\n\t{route}\n\t{queue}")
		if not queue:
			return route

		bestCost = 100000000 if isMin else -100000000
		for location in queue:
			newQueue = queue.copy()
			newQueue.remove(location)
			newRoute = self.traverse(route + [location], newQueue, isMin)
			if isMin and self.cost(newRoute) < bestCost or not isMin and self.cost(newRoute) > bestCost:
				bestCost = self.cost(newRoute)
				bestRoute = newRoute
		return bestRoute

smallExample = [
	'Alice would gain 54 happiness units by sitting next to Bob.',
	'Alice would lose 79 happiness units by sitting next to Carol.',
	'Alice would lose 2 happiness units by sitting next to David.',
	'Bob would gain 83 happiness units by sitting next to Alice.',
	'Bob would lose 7 happiness units by sitting next to Carol.',
	'Bob would lose 63 happiness units by sitting next to David.',
	'Carol would lose 62 happiness units by sitting next to Alice.',
	'Carol would gain 60 happiness units by sitting next to Bob.',
	'Carol would gain 55 happiness units by sitting next to David.',
	'David would gain 46 happiness units by sitting next to Alice.',
	'David would lose 7 happiness units by sitting next to Bob.',
	'David would gain 41 happiness units by sitting next to Carol.']

assert RouteFinder(smallExample).findBestRoute(False) == 330

# Display info message
print("\nGive a list of happiness changes between pairs of guests:\n");

inputStringList = utility.readInputList()

finder = RouteFinder(inputStringList)
print(finder)
shortestRoute = finder.findBestRoute(True)
longestRoute = finder.findBestRoute(False)

finder.readDistance('Me would gain 0 happiness units by sitting next to Alice.')
print(finder)
shortestRoute2 = finder.findBestRoute(True)
longestRoute2 = finder.findBestRoute(False)

# Display results
print (f'shortest = {shortestRoute}, longest = {longestRoute}')
print (f'shortest2 = {shortestRoute2}, longest2 = {longestRoute2}')

