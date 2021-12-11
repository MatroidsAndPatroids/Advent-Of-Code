import utility # my own utility.pl file (readInputList, SimpleTimer)
import hashlib
import re

# MD5 hash for the one-time pad, self-iterated n times
def md5hash(salt, index, iterations):
    hash = salt + str(index)
    for _ in range(iterations):
        hash = hashlib.md5(hash.encode()).hexdigest()
    return hash

def firstRepeatingCharacters(text, num):
    atLeastNTimes = "(.)\\1{" + str(num - 1) + ",}"
    row = re.search(atLeastNTimes, text)
    return row[0][0] if row else None

assert firstRepeatingCharacters("abcdxxx", 3) == 'x'
assert firstRepeatingCharacters("xxxxxabcdqqq", 3) == 'x'
assert firstRepeatingCharacters("abxxxxxxcdqqq", 3) == 'x'

# Character => indexList dictionary
class TripletHistory:
    def __init__(self, offset):
        self.offset = offset
        self.history = {}
        
    def add(self, character, index):
        if character:
            indexList = self.history.setdefault(character, [])
            indexList.append(index)
        return self
    
    def get(self, character, index):
        indexList = self.history.get(character, [])
        for i, ind in enumerate(indexList):
            if index <= ind + self.offset:
                tmp = indexList[i:]
                del indexList[:]
                return tmp 
        return []

assert not TripletHistory(1000).add(None, -666).add(None, 1334).add('x', 100).get('x', 1101)
assert TripletHistory(1000).add('x', 98).add('x', 99).add('x', 100).add('x', 101).add('x', 102).get('x', 1100) == [100, 101, 102]

# If the md5 contains a 5-of-a-kind sequence, return all matching triplet indices
def getMatchingTripletIndices(salt, index, iterations, tripletHistory):
    md5 = md5hash(salt, index, iterations)
    triplet = firstRepeatingCharacters(md5, 3)
    quintuple = firstRepeatingCharacters(md5, 5)
    tripletIndices = tripletHistory.get(quintuple, index)
    #for ind in tripletIndices:
    #    print(salt + str(ind), md5hash(salt, ind, iterations), salt + str(index), md5)
    tripletHistory.add(triplet, index)
    return tripletIndices

# Generate indices for the one-time pad
def generateIndices(salt, numberOfKeys, iterations):
    indices = []
    tripletHistory = TripletHistory(1000)
    
    for i in range(999999999):
        if len(indices) >= numberOfKeys:
            return indices
        indices += getMatchingTripletIndices(salt, i, iterations, tripletHistory)
        
    return indices

# Which index produces the last key
def indexOfLastKey(salt, numberOfKeys, iterations=1):
    T = utility.SimpleTimer()
    indices = generateIndices(salt, numberOfKeys, iterations)
    solution = indices[numberOfKeys - 1]
    print(f'\nindexOfLastKey({salt}, {numberOfKeys}, {iterations}) = {solution}')
    return solution
    
smallExample = """
abc
""".strip().split('\n')[0]
assert indexOfLastKey(smallExample, numberOfKeys=64) == 22728
assert indexOfLastKey(smallExample, numberOfKeys=64, iterations=2017) == 22551

# Display info message
print("\nGive pre-arranged hash salt:")
salt = utility.readInputList()[0]

# Display results
print(f'{indexOfLastKey(salt, numberOfKeys=64) = }')
print(f'{indexOfLastKey(salt, numberOfKeys=64, iterations=2017) = }')