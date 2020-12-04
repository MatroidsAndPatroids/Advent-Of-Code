import utility # my own utility.pl file
Router = __import__('1509') # use the same RouteFinder class from earlier

class SeatingArrangementFinder(Router.RouteFinder):
	# Parse distance string format: "Alice would gain 39 happiness units by sitting next to Mallory."
	def readDistance(self, distanceString):
		name1, would, gain, value, happiness, units, by, sitting, next, to, name2 = distanceString[:-1].split()
		self.locations |= {name1, name2}
		value = self.distances.get((name1, name2), 0) + int(value) if gain == 'gain' else -int(value)
		self.distances[name1, name2] = self.distances[name2, name1] = value

	# Now it's Hamiltonian circle
	def cost(self, route):
		return Router.RouteFinder.cost(self, route) + self.distances.get((route[0], route[-1]), 0)

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
assert SeatingArrangementFinder(smallExample).findBestRoute(False) == 330

# Display info message
print("\nGive a list of happiness changes between pairs of guests:\n");
inputStringList = utility.readInputList()

# Display results
finder = SeatingArrangementFinder(inputStringList)
finder.findBestRoute(True)
finder.findBestRoute(False)

finder.readDistance('Me would gain 0 happiness units by sitting next to Alice.')
print(finder)
finder.findBestRoute(True)
finder.findBestRoute(False)

