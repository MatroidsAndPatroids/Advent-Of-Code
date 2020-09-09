import utility # my own utility.pl file
import random

# Parse 'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8'
class Ingredient:
	def __init__(self, descriptionString):
		str = descriptionString.split(' ')
		assert len(str) == 11
		self.name = str[0][:-1]
		self.capacity = int(str[2][:-1])
		self.durability = int(str[4][:-1])
		self.flavor = int(str[6][:-1])
		self.texture = int(str[8][:-1])
		self.calories = int(str[10])
		self.teaSpoons = 0

	def __str__(self):
		return f'{self.name.rjust(15)}\t{self.capacity}\t{self.durability}\t{self.flavor}\t{self.texture}\t{self.calories}\t{self.teaSpoons}'

	def __repr__(self):
		return self.__str__()

	def header():
		n = 'Name'
		return f'{n.rjust(15)}\tCapacit\tDurabil\tFlavor\tTexture\tCalorie\tTeaSpoo'

class Recipe:
	def __init__(self, descriptionStringList, maxTeaSpoons = 100):
		self.ingredients = [Ingredient(description) for description in descriptionStringList]
		self.maxTeaSpoons = maxTeaSpoons

	def __str__(self):
		text = Ingredient.header()
		for ingredient in self.ingredients:
			text += '\n' + str(ingredient)
		text += '\n' + f'{str(self.totalScore()).rjust(15)}\t{self.totalCapacity()}\t{self.totalDurability()}\t{self.totalFlavor()}\t{self.totalTexture()}\t{self.totalCalories()}\t{self.totalTeaSpoons()}'
		return text

	def __repr__(self):
		return self.__str__()

	def totalCapacity(self):
		return max(0, sum(i.teaSpoons * i.capacity for i in self.ingredients))

	def totalDurability(self):
		return max(0, sum(i.teaSpoons * i.durability for i in self.ingredients))

	def totalFlavor(self):
		return max(0, sum(i.teaSpoons * i.flavor for i in self.ingredients))

	def totalTexture(self):
		return max(0, sum(i.teaSpoons * i.texture for i in self.ingredients))

	def totalCalories(self):
		return max(0, sum(i.teaSpoons * i.calories for i in self.ingredients))

	def totalTeaSpoons(self):
		return sum(i.teaSpoons for i in self.ingredients)

	def totalScore(self):
		return self.totalCapacity() * self.totalDurability() * self.totalFlavor() * self.totalTexture()

	def findBestCookie(self):
		for spoon in range(100):
			bestIngredients = []
			bestValue = -1

			# Find the ingredient which increases the score the most
			for index, ingredient in enumerate(self.ingredients):
				ingredient.teaSpoons += 1
				if (bestValue < self.totalScore()):
					bestIngredients = [index]
					bestValue = self.totalScore()
				elif (bestValue == self.totalScore()):
					bestIngredients += [index]
				ingredient.teaSpoons -= 1

			# Increment one of the ingredients which increases the score the most by 1
			bestIngredient = random.choice(bestIngredients)
			self.ingredients[bestIngredient].teaSpoons += 1

			thereIsAnImprovement = True
			currentTotal = self.totalScore()
			while thereIsAnImprovement:
				thereIsAnImprovement = False
				for i in self.ingredients:
					for j in self.ingredients:
						i.teaSpoons -= 1
						j.teaSpoons += 1
						if currentTotal < self.totalScore():
							thereIsAnImprovement = True
							currentTotal = self.totalScore()
						else:
							i.teaSpoons += 1
							j.teaSpoons -= 1

		return self

	# Try every combination of sprinkles and chocolate (the other 2 are unique then)
	def findSecondBestCookie(self):
		bestIngredients = []
		bestValue = -1
		for sprinkles in range(101):
			# 400 - 8S - 7C <= 100 - C - S    / + 8S+C-400
			# -6C <= 7S - 300    / : (-6)
			# C >= 7S / 6 - 50
			# 0 <= 400 - 8S - 7C    / + 7C
			# 7C <= 400 - 8S    / : 7
			# C <= (400 - 8S) / 7
			minC = int((7 * sprinkles + 5) / 6) - 50
			maxC = int((400 - 8 * sprinkles + 5) / 7)
			for chocolate in range(minC, maxC):
				sugar = 400 - 8 * sprinkles - 7 * chocolate # guaranteened to be between 0-100
				candy = 100 - sugar - sprinkles - chocolate
				self.ingredients[0].teaSpoons = sugar
				self.ingredients[1].teaSpoons = sprinkles
				self.ingredients[2].teaSpoons = candy
				self.ingredients[3].teaSpoons = chocolate
				if bestValue < self.totalScore():
					bestValue = self.totalScore()
					bestIngredients = [sugar, sprinkles, candy, chocolate]

		for i in range(4):
			self.ingredients[i].teaSpoons = bestIngredients[i]

		return self

smallExample = [
	'Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8',
	'Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3']

assert Recipe(smallExample, 100).findBestCookie().totalScore() == 62842880

# Display info message
print("\nGive a list of ingredient descriptions:\n");

inputStringList = utility.readInputList()

# First part random gradient search finds the second best cookie 1 out of 10 times :-)
recipe = Recipe(inputStringList)
while recipe.findBestCookie().totalScore() == 0:
	recipe = Recipe(inputStringList)

recipe2 = Recipe(inputStringList).findSecondBestCookie()

# Display results
print(recipe)
print(recipe2)
