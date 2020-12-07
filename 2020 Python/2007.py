import utility # my own utility.pl file
import re # match
import collections # namedtuple

# Bag data type
Bag = collections.namedtuple('Bag', 'quantity name')

# Convert the input list line by line into a string -> list dictionary like this:
# parentName -> [Bag(quantity, name)]
def parseBags(bagList):
    bagDic = {}
    
    # eg. line = 'light red bags contain 1 bright white bag, 2 muted yellow bags.'
    for line in bagList:
        tokens = re.split(' bags contain | bag, | bags, | bags.| bag.', line)
        assert(tokens) # must not be empty
        
        # eg. parentName = 'light red'
        parentName = tokens[0]
        bagsContained = [] # list of bags contained by parentName
        
        # eg. token = '2 muted yellow'
        for token in tokens[1:]:
            if not token or token == 'no other':
                break
            quantity, name = token.split(' ', 1) # split on first space
            bagsContained += [Bag(int(quantity), name)]
        
        bagDic[parentName] = bagsContained
        
    return bagDic

# Part 1: True if bagToFind is contained by ancestorBag in bagDic
def contains(bagToFind, bagDic, ancestorBag):
    containedBags = bagDic.get(ancestorBag, [])
    
    for bag in containedBags:
        if bag.name == bagToFind:
            return True # we have reached our goal
        
    for bag in containedBags:
        # check all the ancestors for the desired bag
        if contains(bagToFind, bagDic, bag.name):
            return True
        
    return False

# Part 2: count the number of bags contained by ancestorBag
def bagCount(bagToFind, bagDic, ancestorBag):
    count = 1 # ancestorBag itself counts as 1
    containedBags = bagDic.get(ancestorBag, [])
    
    for bag in containedBags:
        if bag.name != bagToFind:
            count += bag.quantity * bagCount(bagToFind, bagDic, bag.name)
            
    #print(f'{ancestorBag = } {count = }')
    return count

# Part 1: find the number of bags containing the given bag
def numberOfBagsContaining(bagToFind, bagList):
    bagDic = parseBags(bagList)
    bagToFindIsIn = lambda bagName: int(contains(bagToFind, bagDic, bagName))
    return sum(bagToFindIsIn(bagName) for bagName in bagDic.keys())
    #return sum(list(map(func, bagDic.keys())))   

# Part 2: find the number of bags contained by the given bag with multiplicity
def numberOfBagsContainedBy(bagToFind, bagList):
    bagDic = parseBags(bagList)
    return bagCount(bagToFind, bagDic, bagToFind) - 1 # omit the starting bag

# Check test cases
smallExample = [
    'light red bags contain 1 bright white bag, 2 muted yellow bags.',
    'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
    'bright white bags contain 1 shiny gold bag.',
    'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
    'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
    'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
    'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
    'faded blue bags contain no other bags.',
    'dotted black bags contain no other bags.']
part2Example = [
    'shiny gold bags contain 2 dark red bags.',
    'dark red bags contain 2 dark orange bags.',
    'dark orange bags contain 2 dark yellow bags.',
    'dark yellow bags contain 2 dark green bags.',
    'dark green bags contain 2 dark blue bags.',
    'dark blue bags contain 2 dark violet bags.',
    'dark violet bags contain no other bags.']
assert numberOfBagsContaining('shiny gold', smallExample) == 4
assert numberOfBagsContainedBy('shiny gold', smallExample) == 32
assert numberOfBagsContainedBy('shiny gold', part2Example) == 126

# Display info message
print("Give list of bags and contents:\n")
bagList = utility.readInputList()

# Display results
print(f'{numberOfBagsContaining("shiny gold", bagList) = }')
print(f'{numberOfBagsContainedBy("shiny gold", bagList) = }')