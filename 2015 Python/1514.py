import utility # my own utility.pl file
import re # compile
import pandas # data frame

class Herd(pandas.DataFrame):
	def __init__(self, reindeerDescriptions):
		# Parse 'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8'
		line_re = re.compile(r"^(?P<Name>\w+) can fly (?P<Speed>-?\d+) km.s for (?P<FlightDur>-?\d+) seconds,.* for (?P<RestDur>-?\d+) seconds.")
		df = pandas.DataFrame()
		for line in reindeerDescriptions:
			data = line_re.match(line).groupdict()
			index = data.pop('Name')
			data = dict([key, int(value)] for key, value in data.items())
			df = df.append(pandas.DataFrame(data, [index]))
		pandas.DataFrame.__init__(self, df)
		#self.index.name = 'Name'
		
		# Add calculated columns to the Data Frame
		self['Avg. Speed'] = self.Speed * self.FlightDur / (self.FlightDur + self.RestDur)
		# Current duration = 0-FlightDur when flying and (-RestDur)-(-1) while resting
		self['Duration'] = self.FlightDur
		self['Distance'] = 0
		self['Score'] = 0
	
	def race(self, travelTime):
		for i in range(travelTime):
			# Update Duration
			self.loc[self.Duration <= -self.RestDur, 'Duration'] = self.FlightDur
			self.Duration -= 1
			# Update Distance
			self.loc[self.Duration >= 0, 'Distance'] += self.Speed
			# Update Score
			self.loc[self.Distance == max(self.Distance), 'Score'] += 1
		self.Distance = pandas.to_numeric(self.Distance, downcast = 'signed')
		return self		

smallExample = [
	'Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.',
	'Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.']
smallHerd = Herd(smallExample).race(1000)
assert smallHerd.loc['Comet', 'Distance'] == 1120
assert smallHerd.loc['Dancer', 'Distance'] == 1056
assert smallHerd.loc['Comet', 'Score'] == 312
assert smallHerd.loc['Dancer', 'Score'] == 689

# Display info message
print("Give a list of reindeer descriptions:\n");
reindeerDescriptions = utility.readInputList()
travelTime = 2503

# Display results
print(Herd(reindeerDescriptions).race(travelTime))

