import utility # my own utility.pl file (readInputList, SimpleTimer)
import math
import numpy as np

# Simulate the white elephant party and return the winner
def whiteElephantPartyAlgorithm(elves, part2=False):
    party = range(elves)
    if part2:
        #print(party)
        party = np.array(party)
        while elves > 1:
            halves = elves // 2
            blackList = np.array([(i + (elves + i) // 2) % elves for i in range(halves)])
            survives = np.ones(elves, dtype=bool) #[True] * elves
            for i in blackList:
                survives[i] = False
            party = np.array([party[(i + halves + 1) % elves] for i in range(elves) if survives[(i + halves + 1) % elves]])
            elves = len(party)
            #print('  ', party)
            #print('  ', party, blackList, survives)
    else:
        while elves > 1:
            parity = elves % 2
            party = party[2 * parity::2]
            elves = len(party)
   
    return party[0] + 1

# Calculate the winner of the white elephant party using a formula
def whiteElephantPartyFormula(elves, part2=False):
    if part2:
        if elves == 1:
            return 1
        log3 = math.ceil(math.log(elves, 3))
        lowerBound = 3 ** (log3 - 1)
        upperBound = 3 * lowerBound
        mean = (upperBound + lowerBound) // 2
        
        if elves <= mean:
            return elves - lowerBound
        return lowerBound + 2 * (elves - mean)
    
    log2 = math.floor(math.log(elves, 2))
    lowerBound = 2 ** log2
    return 1 + 2 * (elves - lowerBound)

# Return the winner of the white elephant party
def whiteElephantParty(elves, part2=False, formula=False):
    T = utility.SimpleTimer()
    if formula:
        return whiteElephantPartyFormula(elves, part2)
    return whiteElephantPartyAlgorithm(elves, part2)

# Assert that the WEP formula and the algorithm gives the same result
def testEmAll(maxElves):
    for elves in range(1, maxElves):
        for part2 in (False, True):
            algorithm = whiteElephantPartyAlgorithm(elves, part2)
            formula = whiteElephantPartyFormula(elves, part2)
            assert algorithm == formula

# List the winner of the WEPs from 1 to N
def printEmAllOut(maxElves, part2=False, formula=False):
    for elves in range(1, maxElves):
        print(whiteElephantPartyAlgorithm(elves, part2, formula))

assert whiteElephantParty(5) == 3
assert whiteElephantParty(5, part2=True) == 2
testEmAll(100)

# Display info message
print("\nGive initial state:")
elves = int(utility.readInputList()[0])

# Display results
print(f'{whiteElephantParty(elves) = }')
print(f'{whiteElephantParty(elves, part2=True) = }')
#printEmAllOut(10000, part2=False, formula=False)