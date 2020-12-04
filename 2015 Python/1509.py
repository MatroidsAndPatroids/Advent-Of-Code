import utility # my own utility.pl file

class RouteFinder:
	def __init__(self, inputList = []):
		self.locations = set()
		self.distances = {}
		
		for inputString in inputList:
			self.readDistance(inputString)

	def __str__(self):
		sortedLoc = sorted(self.locations)
		header = '\t'.join(map(lambda loc: loc[:7].rjust(7, ' '), sortedLoc))
		lines = '\n' + f"Size: {self.size()}".rjust(15, ' ') + '\t' + header
		
		for loc1 in sortedLoc:
			distances = '\t'.join(map(lambda loc2: str(self.distances.get((loc1, loc2), 0)).rjust(7, ' '), sortedLoc))
			lines += '\n' + loc1.rjust(15, ' ') + '\t' + distances
		return lines

	def size(self):
		return len(self.locations)

	# Parse distance string format: "London to Dublin = 464"
	def readDistance(self, distanceString):
		loc1, to, loc2, equals, distance = distanceString.split()
		self.locations |= {loc1, loc2}
		self.distances[loc1, loc2] = self.distances[loc2, loc1] = int(distance)

	# Find the Hamiltonian path of minimum or maximum lenght
	def findBestRoute(self, isMin):
		firstLocation = sorted(self.locations)[0]
		bestRoute = self.traverse([firstLocation], self.locations - {firstLocation}, isMin)
		print(f"{'Shortest' if isMin else 'Longest'} route ({self.cost(bestRoute)}): {bestRoute}")
		return self.cost(bestRoute)

	def cost(self, route):
		return sum(self.distances.get((route[i], route[i + 1]), 0) for i in range(len(route) - 1))

	def traverse(self, route, unvisited, isMin):
		#print(f"traverse\n\t{route}\n\t{queue}")
		if not unvisited:
			return route

		bestCost = 100000000 if isMin else -100000000
		for location in unvisited:
			finishedRoute = self.traverse(route + [location], unvisited - {location}, isMin)
			if isMin and self.cost(finishedRoute) < bestCost \
			or not isMin and self.cost(finishedRoute) > bestCost:
				bestCost = self.cost(finishedRoute)
				bestRoute = finishedRoute
		return bestRoute

if __name__ == '__main__':
	smallExample = [
		'London to Dublin = 464',
		'London to Belfast = 518',
		'Dublin to Belfast = 141']
	assert RouteFinder(smallExample).findBestRoute(isMin = True) == 605
	assert RouteFinder(smallExample).findBestRoute(isMin = False) == 982
	
	# Display info message
	print("\nGive a list of distances between locations:\n");
	inputStringList = utility.readInputList()
	
	# Display results
	finder = RouteFinder(inputStringList)
	print(finder)
	shortestRoute = finder.findBestRoute(isMin = True)
	longestRoute = finder.findBestRoute(isMin = False)
