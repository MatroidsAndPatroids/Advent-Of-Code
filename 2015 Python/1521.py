import utility # my own utility.pl file

# Parse 'Al => ThF'
class Item:
	def __init__(self, itemText):
		properties = itemText.split()
		self.name = properties[0]
		self.cost = int(properties[1])
		self.damage = int(properties[2])
		self.armor = int(properties[3])

	def __str__(self):
		return f"{self.name.ljust(15, ' ')}\t{self.cost}\t{self.damage}\t{self.armor}"

	def header(typeName):
		return f"{typeName.ljust(15, ' ')}\tCost\tDamage\tArmor"

class Fighter:
	def __init__(self, name, hitPoints, damage = 0, armor = 0, opponent = None):
		self.name = name
		self.hitPoints = hitPoints
		self.maxHP = hitPoints
		self.damage = damage
		self.armor = armor
		self.opponent = opponent

	def reset(self):
		self.hitPoints = self.maxHP

	def attack(self):
		self.opponent.hitPoints -= max(1, self.damage - self.opponent.armor)
		return self.opponent.hitPoints <= 0

	def __str__(self):
		return f'{self.name}: {self.hitPoints}/{self.damage}/{self.armor}'

class Shop:
	def __init__(self, itemList):
		self.items = []
		self.weaponRange = []
		self.armorRange = []
		self.ringRange = []

		currentRange = self.weaponRange
		for item in itemList:
			if 'Weapons:' in item:
				currentRange = self.weaponRange
			elif 'Armor:' in item:
				currentRange = self.armorRange
			elif 'Rings:' in item:
				currentRange = self.ringRange
			else:
				currentRange.append(len(self.items))
				self.items.append(Item(item))

	def __str__(self):
		text = f'{Item.header("Weapons:")}\n'
		for i in self.weaponRange:
			text += f'{self.items[i]}\n'
		text += f'{Item.header("Armor:")}\n'
		for i in self.armorRange:
			text += f'{self.items[i]}\n'
		text += f'{Item.header("Rings:")}\n'
		for i in self.ringRange:
			text += f'{self.items[i]}\n'
		return text


class Game:
	def __init__(self, bossHP, bossDMG, bossARM, shop):
		self.shop = shop
		self.fighters = [Fighter('Player', 100)]
		self.fighters += [Fighter('Boss', bossHP, bossDMG, bossARM, self.fighters[0])]
		self.fighters[0].opponent = self.fighters[1]

	def __str__(self):
		return f'{self.fighters[0]}\t{self.fighters[1]}'

	def simulate(self):
		for fighter in self.fighters:
			fighter.reset()

		for turn in range(100):
			for fighter in self.fighters:
				if fighter.attack():
					return fighter.name == 'Player'

	def supplyPlayer(self, itemIndexes):
		# Remove any items first
		cost = 0
		self.fighters[0].damage = 0
		self.fighters[0].armor = 0

		for i in itemIndexes:
			item = self.shop.items[i]
			self.fighters[0].damage += item.damage
			self.fighters[0].armor += item.armor
			cost += item.cost

		return cost

	def tryThemAll(self, bestCase = True):
		bestCost = 1000000 if bestCase else 0
		for w in shop.weaponRange:
			for a in shop.armorRange:
				for r1 in shop.ringRange:
					for r2 in shop.ringRange:
						if r1 < r2:
							cost = self.supplyPlayer([w, a, r1, r2])
							if bestCase and cost < bestCost and self.simulate() \
							or not bestCase and cost > bestCost and not self.simulate():
								print(f'{self}\t{cost} = {self.shop.items[w].name} + {self.shop.items[a].name} + {self.shop.items[r1].name} + {self.shop.items[r2].name}')
								bestCost = cost
		return bestCost

shopItems = [
	'Weapons:    Cost  Damage  Armor',
	'Dagger        8     4       0',
	'Shortsword   10     5       0',
	'Warhammer    25     6       0',
	'Longsword    40     7       0',
	'Greataxe     74     8       0',
	'Armor:      Cost  Damage  Armor',
	'Unarmored     0     0       0',
	'Leather      13     0       1',
	'Chainmail    31     0       2',
	'Splintmail   53     0       3',
	'Bandedmail   75     0       4',
	'Platemail   102     0       5',
	'Rings:      Cost  Damage  Armor',
	'NoRing        0     0       0',
	'NoRing        0     0       0',
	'Damage+1     25     1       0',
	'Damage+2     50     2       0',
	'Damage+3    100     3       0',
	'Defense+1    20     0       1',
	'Defense+2    40     0       2',
	'Defense+3    80     0       3']

# Display info message
print("\nLet the games begin!\n")

inputStringList = utility.readInputList()

shop = Shop(shopItems)
print(shop)
game = Game(104, 8, 1, shop)
print(game)

# Display results
print(game.tryThemAll())
print(game.tryThemAll(False))

