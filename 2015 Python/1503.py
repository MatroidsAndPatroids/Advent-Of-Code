import utility # my own utility.pl file
from collections import defaultdict

# How many presents are at each location at the end of the delivery?
# numPlayer = 1 with Santa only and 2 with Robo-Santa included
def createPresentMap(instructions, numPlayers = 1):
	# position (x, y) is stored as a complex number x + y * j
	deltas = {'>' : 1, '<' : -1, 'v' : 1j, '^' : -1j}
	currentLocation = [0] * numPlayers # starting position is 0 for each player
	numPresents = defaultdict(complex) # forces complex number keys for the dictionary
	numPresents[0] = numPlayers # starting position already has #players presents
	turn = 0 # 0 = Santa's turn, 1 = Robo-Santa's

	for character in instructions:
		delta = deltas.get(character, 0)
		if delta != 0:
			currentLocation[turn] += delta
			numPresents[currentLocation[turn]] += 1
			turn = (turn + 1) % numPlayers

	return numPresents

assert len(createPresentMap('>', 1)) == 2
assert len(createPresentMap('^>v<', 1)) == 4
assert len(createPresentMap('^v^v^v^v^v', 1)) == 2

assert len(createPresentMap('^v', 2)) == 3
assert len(createPresentMap('^>v<', 2)) == 3
assert len(createPresentMap('^v^v^v^v^v', 2)) == 11

# Display info message
print("Give a string of 'v', '^', '<' and '>' characters, where they mean go up, down, left and right respectively.\n");
instructions = utility.readInputList(joinedWith = '')

# Display results
housesVisitedWithSantaOnly = len(createPresentMap(instructions, 1))
housesVisitedWithRoboSanta = len(createPresentMap(instructions, 2))
print(f"{housesVisitedWithSantaOnly = }, {housesVisitedWithRoboSanta = }")

