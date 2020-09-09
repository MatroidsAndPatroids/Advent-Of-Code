import utility # my own utility.pl file

class GameState:
	def __init__(self, playerHP = 50, playerMP = 500, bossHP = 71, manaSpent = 0, effectsInPlay = {}):
		self.playerHP = playerHP
		self.playerMP = playerMP
		self.bossHP = bossHP
		self.manaSpent = manaSpent
		self.effectsInPlay = effectsInPlay

	def __str__(self):
		effectText = ''
		for effect, duration in self.effectsInPlay.items():
			effectText += f'{effect.name}: {duration}, '
		return f'{self.playerHP}/{self.playerMP} - {self.bossHP}, Effects: {effectText}'

	def add(self, effect):
		self.playerMP -= effect.manaCost
		self.manaSpent += effect.manaCost
		self.effectsInPlay[effect] = effect.startingDuration
		#print(f'{effect.name} -> {self}')

	def applyEffects(self): # returns the playerArmor
		playerArmor = 0
		for effect, duration in self.effectsInPlay.items():
			self.bossHP -= effect.damage
			playerArmor += effect.armor
			self.playerHP += effect.heal
			self.playerMP += effect.mana
			self.effectsInPlay[effect] -= 1

		# remove expired effects
		self.effectsInPlay = {effect:duration for effect, duration in self.effectsInPlay.items() if duration > 0}
		return playerArmor

	def simulateRound(self, effect, decay): # returns false when the game ended
		self.playerHP -= decay
		if self.playerHP <= 0:
			return False

		self.add(effect)

		playerArmor = self.applyEffects()
		if self.bossHP <= 0:
			return False

		bossDamage = 10
		self.playerHP -= max(1, bossDamage - playerArmor)
		if self.playerHP <= 0:
			return False

		playerArmor = self.applyEffects()
		if self.bossHP <= 0:
			return False

		return True

	def tryAllEffects(self, EffectList, decay = 0):
		totalManaSpent = 1000000

		for effect in EffectList:
			if effect not in self.effectsInPlay and effect.manaCost <= self.playerMP:
				newState = GameState(self.playerHP, self.playerMP, self.bossHP, self.manaSpent, self.effectsInPlay.copy())

				if newState.simulateRound(effect, decay):
					# The game did not end
					totalManaSpent = min(totalManaSpent, newState.tryAllEffects(EffectList, decay))
				elif newState.playerHP > 0:
					# Player has won
					totalManaSpent = min(totalManaSpent, newState.manaSpent)
		return totalManaSpent

class Effect:
	def __init__(self, name, manaCost, startingDuration, damage, armor, heal, mana):
		self.name = name
		self.manaCost = manaCost
		self.startingDuration = startingDuration
		self.damage = damage
		self.armor = armor
		self.heal = heal
		self.mana = mana

	def __str__(self):
		return f'{self.name}: {self.manaCost}/{self.startingDuration}/{self.damage}/{self.armor}/{self.heal}/{self.mana}'

effects = [
	Effect('Magic Missile', 53, 1, 4, 0, 0, 0),
	Effect('Drain', 73, 1, 2, 0, 2, 0),
	Effect('Shield', 113, 6, 0, 7, 0, 0),
	Effect('Poison', 173, 6, 3, 0, 0, 0),
	Effect('Recharge', 229, 5, 0, 0, 0, 101)]

# Display info message
print("\nLet the games begin!\n")

inputStringList = utility.readInputList()

for effect in effects:
	print(effect)

game = GameState()
print(f'\n{game}\n')

# Display results
manaNormal = GameState().tryAllEffects(effects)
print(f'Total mana spent (normal): {manaNormal}')
manaHard = GameState().tryAllEffects(effects, 1)
print(f'Total mana spent (hard): {manaHard}')

