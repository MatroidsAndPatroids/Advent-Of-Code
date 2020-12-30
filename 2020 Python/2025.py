import utility # my own utility.pl file

def loopIt(key, rounds = 0):
    val = 1
    div = 20201227
    sub = 7 if rounds == 0 else key
    loopSize = 0
    
    if rounds == 0:
        while val != key:
            val *= sub
            val %= div
            loopSize += 1
        return loopSize
    else:
        for i in range(rounds):
            val *= sub
            val %= div
    return val

# Simulates the instructions
def emulate(instructions, part2 = False):
    card = int(instructions[0])
    door = int(instructions[1])

    cardLoop = loopIt(card)        
    doorLoop = loopIt(door)
    print(cardLoop, doorLoop)
    cardLoop = loopIt(card, doorLoop)        
    doorLoop = loopIt(door, cardLoop)
    print(cardLoop, doorLoop)

    sol = cardLoop
    print(sol)
    return sol if part2 else sol

# Check test cases
smallExample = """
5764801
17807724
""".strip().split('\n')
assert emulate(smallExample) == 14897079
assert emulate(smallExample, part2 = True) == 14897079

# Display info message
print("Give a list of ship/waypoint movement instructions:\n")
instructions = utility.readInputList()

# Display results
print(f'{emulate(instructions) = }')
print(f'{emulate(instructions, part2 = True) = }')