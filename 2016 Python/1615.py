import utility # my own utility.pl file (readInputList, SimpleTimer)
import re
import sympy.ntheory.modular # crt (Chinese Reminder Theorem)

# Convert disc positions into input for the Chinese Remainder Theorem
def parseInput(discPositions):
    moduli = []
    remainders = []
    for currentDisc in discPositions:
        pattern = '^Disc #| has | positions; at time=0, it is at position |\.$'
        timeToReach, discSize, initialPosition = map(int, re.split(pattern, currentDisc)[1:-1])
        # initialPosition + timeToReach + t === 0 (mod discSize)
        moduli.append(discSize)
        remainders.append(-initialPosition - timeToReach)
    return moduli, remainders

# Minimum time to wait before we can get the capsule 
def calcWaitingTime(discPositions):
    moduli, remainders = parseInput(discPositions)
    crtSolution = sympy.ntheory.modular.crt(moduli, remainders)
    return crtSolution
    
smallExample = """
Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1.
""".strip().split('\n')
assert calcWaitingTime(smallExample)[0] == 5

# Display info message
print("\nGive disc positions:")
discPositions = utility.readInputList()

# Display results
print(f'{calcWaitingTime(discPositions) = }')
extraDisc = "Disc #7 has 11 positions; at time=0, it is at position 0."
print(f'{calcWaitingTime(discPositions + [extraDisc]) = }')