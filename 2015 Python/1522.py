import utility # my own utility.pl file
import collections # namedtuple
import copy # deepcopy

class GameState:
	bestSolution = 1000000

	def __init__(self, playerHP = 50, playerMP = 500, playerArmor = 0, bossHP = 71, manaSpent = 0, effectsInPlay = {}):
		self.playerHP = playerHP
		self.playerMP = playerMP
		self.playerArmor = playerArmor
		self.bossHP = bossHP
		self.manaSpent = manaSpent
		self.effectsInPlay = effectsInPlay

	def __copy__(self):
		return GameState(self.playerHP, self.playerMP, self.playerArmor, self.bossHP, self.manaSpent, self.effectsInPlay.copy())

	def __str__(self):
		effectText = ''
		for effect, duration in self.effectsInPlay.items():
			effectText += f'{effect.name}: {duration}, '
		return f'{self.playerHP}/{self.playerMP} - {self.bossHP}, Effects: {effectText}'

	# Plays either the player's turn (if effect is given) or the boss's turn (if effect is none)
	def turn(self, playerLoss, newEffect = None): # returns the playerArmor
		# Apply damage to player
		if newEffect: # add new effect, when given
			self.playerHP -= playerLoss
			self.playerMP -= newEffect.manaCost
			self.manaSpent += newEffect.manaCost
			self.effectsInPlay[newEffect] = newEffect.startingDuration
		else:
			self.playerHP -= max(1, playerLoss - self.playerArmor)
		
		if self.playerHP <= 0:
			return False

		# Apply effects
		self.playerArmor = 0
		for effect, duration in self.effectsInPlay.items():
			self.bossHP -= effect.damage
			self.playerArmor += effect.armor
			self.playerHP += effect.heal
			self.playerMP += effect.mana
			self.effectsInPlay[effect] -= 1

		# remove expired effects
		self.effectsInPlay = {effect: duration for effect, duration in self.effectsInPlay.items() if duration > 0}
		return self.bossHP > 0 # true if the game has not ended

	# Search the tree of all combinations of effects until the endgames are found
	def tryAllEffects(self, EffectList, decay = 0):
		bossDamage = 10
		for newEffect in EffectList:
			if newEffect not in self.effectsInPlay and newEffect.manaCost <= self.playerMP:
				newState = self.__copy__()
				if newState.manaSpent >= GameState.bestSolution: # prune tree
					return newState.manaSpent
				if newState.turn(decay, newEffect) and newState.turn(bossDamage): # continue game
					GameState.bestSolution = min(GameState.bestSolution, newState.tryAllEffects(EffectList, decay))
				elif newState.playerHP > 0: # Player has won
					GameState.bestSolution = min(GameState.bestSolution, newState.manaSpent)
		return GameState.bestSolution
	
Effect = collections.namedtuple('Effect', ['name', 'manaCost', 'startingDuration', 'damage', 'armor', 'heal', 'mana'])
effects = [
	Effect('Magic Missile', 53, 1, 4, 0, 0, 0),
	Effect('Drain', 73, 1, 2, 0, 2, 0),
	Effect('Shield', 113, 6, 0, 7, 0, 0),
	Effect('Poison', 173, 6, 3, 0, 0, 0),
	Effect('Recharge', 229, 5, 0, 0, 0, 101)]

# Display info message
print("Let the games begin!\n")
bossStats = utility.readInputList()

# Display results
print(f'Total mana spent (normal): {GameState().tryAllEffects(effects)}')
GameState.bestSolution = 1000000
print(f'Total mana spent (hard): {GameState().tryAllEffects(effects, 1)}')

