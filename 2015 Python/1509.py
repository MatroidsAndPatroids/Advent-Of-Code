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
		assert len(distances) == 5
		location1 = distances[0]
		location2 = distances[2]
		distance = int(distances[4])

		code1 = self.getLocationCode(location1)
		code2 = self.getLocationCode(location2)
		self.distanceTable[code1][code2] = distance
		self.distanceTable[code2][code1] = distance

	# Find the Hamiltonian path of minimum or maximum lenght
	def findBestRoute(self, isMin):
		bestRoute = self.traverse([], self.locationName[0:self.size()], isMin)
		print(f"bestRoute = {bestRoute} = {self.cost(bestRoute)}")
		return self.cost(bestRoute)

	def cost(self, route):
		cost = 0
		prevLoc = ''
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
	'London to Dublin = 464',
	'London to Belfast = 518',
	'Dublin to Belfast = 141']

assert RouteFinder(smallExample).findBestRoute(True) == 605
assert RouteFinder(smallExample).findBestRoute(False) == 982

# Display info message
print("\nGive a list of distances between locations:\n");

inputStringList = utility.readInputList()

finder = RouteFinder(inputStringList)
print(finder)
shortestRoute = finder.findBestRoute(True)
longestRoute = finder.findBestRoute(False)

# Display results
print (f'shortest = {shortestRoute}')
print (f'longest = {longestRoute}')

