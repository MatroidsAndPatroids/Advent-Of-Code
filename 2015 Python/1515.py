import utility # my own utility.pl file
import re # compile
import pandas # data frame

class Recipe(pandas.DataFrame):
	def __init__(self, ingredientDescriptions):
		# Parse 'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8'
		line_re = re.compile(r"^(?P<Name>\w+): capacity (?P<Capacity>-?\d+), durability (?P<Durability>-?\d+), flavor (?P<Flavor>-?\d+), texture (?P<Texture>-?\d+), calories (?P<Calories>-?\d+)")
		df = pandas.DataFrame()
		for line in ingredientDescriptions:
			data = line_re.match(line).groupdict()
			index = data.pop('Name')
			data = dict([key, int(value)] for key, value in data.items())
			df = df.append(pandas.DataFrame(data, [index]))
		pandas.DataFrame.__init__(self, df)
		#self.index.name = 'Name'
		
		# Add calculated columns to the Data Frame
		self['TeaSpoon'] = 0
	
	# Print a nice little total row at the end
	def __str__(self):
		lastRow = self.TeaSpoon.dot(self)
		lastRow.name = f'Score = {self.totalScore()}'
		lastRow.TeaSpoon = sum(self.TeaSpoon)
		return self.append(lastRow).__str__()

	def divisions(self, remainingIngredients, remainingTeaSpoons = 100):
	    if remainingIngredients == 1:
	        yield [remainingTeaSpoons]
	    else:
	        for tsp in range(0, remainingTeaSpoons + 1):
	            for right in self.divisions(remainingIngredients - 1, remainingTeaSpoons - tsp):
	                yield [tsp] + right
	                
	def totalScore(self):
		score = max(0, self.Capacity.dot(self.TeaSpoon))
		score *= max(0, self.Durability.dot(self.TeaSpoon))
		score *= max(0, self.Flavor.dot(self.TeaSpoon))
		score *= max(0, self.Texture.dot(self.TeaSpoon))
		return score
	
	def findBestCookie(self, teaSpoonTarget = 100, calorieTarget = None):
		ingredients = len(self.index)
		bestScore = -1
		bestRecipe = []
		for division in self.divisions(ingredients):
			self.TeaSpoon = division
			if calorieTarget != None and self.Calories.dot(self.TeaSpoon) != calorieTarget:
				continue
			if bestScore < self.totalScore():
				bestScore = self.totalScore()
				bestRecipe = division
		self.TeaSpoon = bestRecipe
		return self

smallExample = [
	'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
	'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3']
assert Recipe(smallExample).findBestCookie(100).totalScore() == 62842880
assert Recipe(smallExample).findBestCookie(100, 500).totalScore() == 57600000

# Display info message
print("Give a list of ingredient descriptions:\n");
ingredientDescriptions = utility.readInputList()

# Display results
print(Recipe(ingredientDescriptions).findBestCookie(100))
print(Recipe(ingredientDescriptions).findBestCookie(100, 500))
