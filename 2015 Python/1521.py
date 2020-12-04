import utility # my own utility.pl file
import collections # namedtuple
import math # ceil
import itertools # procudt, combinations

class Shop:
	Item = collections.namedtuple('Item', ['name', 'cost', 'damage', 'armor'])

	def __init__(self, shopItems):
		self.weapons = []
		self.armor = []
		self.rings = []
		
		containers = {'Weapons:' : self.weapons, 'Armor:' : self.armor, 'Rings:' : self.rings}
		currentContainer = None
		for itemText in shopItems:
			# Parse 'Warhammer    25     6       0'
			name, cost, damage, armor = itemText.split()
			if name in containers:
				currentContainer = containers[name]
			else:
				currentContainer.append(self.Item(name, int(cost), int(damage), int(armor)))

	def __str__(self):
		text = ''
		for container in [self.weapons, self.armor, self.rings]:
			text += '-----------------------------\n'
			for item in container:
				text += f'{item.name.rjust(15)}\t{item.cost}/{item.damage}/{item.armor}\n'
		return text

class Game:
	def __init__(self, playerHP, bossStats, shopItems):
		self.playerHP = playerHP
		self.playerDmg = 0
		self.playerArmor = 0
		self.bossHP = int(bossStats[0].split(' ')[-1])
		self.bossDmg = int(bossStats[1].split(' ')[-1])
		self.bossArmor = int(bossStats[2].split(' ')[-1])
		self.shop = Shop(shopItems)

	def supplyPlayer(self, items):
		# reset player stats first
		self.playerDmg = 0
		self.playerArmor = 0
		cost = 0
		
		for item in items:
			self.playerDmg += item.damage
			self.playerArmor += item.armor
			cost += item.cost
		return cost
	
	# Search the tree of all combinations of items until the endgames are found
	def tryAllItems(self, cheapestWin = True):
		bestCost = 1000000 if cheapestWin else 0
		for weapon, armor, rings in itertools.product(self.shop.weapons, self.shop.armor, itertools.combinations(self.shop.rings, 2)):
			cost = self.supplyPlayer([weapon, armor, rings[0], rings[1]])
			# Calculate who wins based on the stats only
			bossHpLossPerRound = max(1, self.playerDmg - self.bossArmor)
			playerHpLossPerRound = max(1, self.bossDmg - self.playerArmor)
			rounds = math.ceil(self.playerHP / playerHpLossPerRound)
			playerWins = (self.bossHP <= bossHpLossPerRound * rounds)
			
			if cheapestWin and cost < bestCost and playerWins \
			or not cheapestWin and cost > bestCost and not playerWins:
				print(f'{cost} = {weapon.name} + {armor.name} + {rings[0].name} + {rings[1].name} = {self.playerDmg}/{self.playerArmor}')
				bestCost = cost
		return bestCost

# Display info message
print("Let the games begin!\n")
playerHP = 100
bossStats = utility.readInputList()

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

# Display results
print(f'Cheapest Victory: {Game(playerHP, bossStats, shopItems).tryAllItems()}')
print(f'Most expensive Defeat: {Game(playerHP, bossStats, shopItems).tryAllItems(False)}')

