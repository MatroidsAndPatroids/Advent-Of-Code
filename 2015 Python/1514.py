import utility # my own utility.pl file

# Parse 'Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.'

class Reindeer:
	def __init__(self, descriptionString, travelSeconds = 0):
		str = descriptionString.split(' ')
		assert len(str) == 15
		self.name = str[0]
		self.kmPerSec = int(str[3])
		self.flySeconds = int(str[6])
		self.restSeconds = int(str[13])
		self.travelSeconds = 0
		self.flownKilometers = 0
		self.winningPoints = 0
		self.calculateFlownKilometers(travelSeconds)

	def __str__(self):
		return f'{self.name}\t{self.kmPerSec}\t{self.flySeconds}\t{self.restSeconds}\t{self.travelSeconds}\t{self.flownKilometers}\t{self.winningPoints}'

	def __repr__(self):
		return self.__str__()

	def calculateFlownKilometers(self, travelSeconds):
		self.travelSeconds = travelSeconds
		period = self.flySeconds + self.restSeconds
		numPeriods = travelSeconds // period
		lastPeriod = travelSeconds % period
		totalflySeconds = numPeriods * self.flySeconds + min(lastPeriod, self.flySeconds)
		self.flownKilometers = totalflySeconds * self.kmPerSec

	def increaseWinningPoints(self):
		self.winningPoints += 1

smallExample = [
	'Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',
	'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.']

assert Reindeer(smallExample[0], 1000).flownKilometers == 1120
assert Reindeer(smallExample[1], 1000).flownKilometers == 1056

# Display info message
print("\nGive a list of reindeer descriptions:\n");

inputStringList = utility.readInputList()

travelSeconds = 2503
Herd = [Reindeer(line, travelSeconds) for line in inputStringList]

Herd2 = [Reindeer(line, 0) for line in inputStringList]
for t in range(1, travelSeconds + 1):
	for reindeer in Herd2:
		reindeer.calculateFlownKilometers(t)
	maxDistance = max(reindeer.flownKilometers for reindeer in Herd2)
	for reindeer in Herd2:
		if reindeer.flownKilometers == maxDistance:
			reindeer.increaseWinningPoints()
		print(reindeer)

# Display results
maxDistance = max(reindeer.flownKilometers for reindeer in Herd)
for reindeer in Herd:
	if reindeer.flownKilometers == maxDistance:
		print(reindeer)

maxPoints = max(reindeer.winningPoints for reindeer in Herd)
for reindeer in Herd2:
	if reindeer.winningPoints == maxPoints:
		print(reindeer)

