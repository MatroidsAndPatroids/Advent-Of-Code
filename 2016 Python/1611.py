import utility # my own utility.pl file
import re # compile, match
import copy # deepcopy
import time # process_time
from networkx.algorithms.shortest_paths import astar_path
from networkx.algorithms.shortest_paths.unweighted import bidirectional_shortest_path

# Node object for the custom NetworkX graph object
# It can calculate its own neighbour objects.
class State:
    # Punish moving down items and reward moving them up
    # This is pretty slow, so don't use it without heuristics :P
    # calcWeight1 = {(-1, 2): 1000000, (-1, 1): 10000, (1, 1): 100, (1, 2): 1}
    
    # Moving only 1 up is infinitely worse than moving 1 down!?!? Yet it's optimal.
    calcWeight = {(-1, 2): 1000000, (-1, 1): 30, (1, 1): 1000000, (1, 2): 1}
    
    def __init__(self, floor, chips, gens):
        self.floor = floor
        self.chips = chips
        self.gens = gens

    # Brief text version, used for hashing too 
    def __str__(self):
        text = str(self.floor) + '-'
        text += '|'.join((''.join(sorted(chip)) for chip in self.chips)) + '-'
        text += '|'.join((''.join(sorted(gen)) for gen in self.gens))
        return text
    
    # Hash and == are a requirement to become a key in a dictionary
    def __hash__(self):
        return hash(self.__str__())
    def __eq__(self, other):
        return hash(self) == hash(other)
    
    # Sanity check after first object creation
    def areDimensionsValid(self):
        return 0 <= self.floor < len(self.chips) == len(self.gens)
    
    # Return False in case of chip fryage on the given floor
    def areChipsSafe(self, floor):
        if not self.gens[floor]:
            return True
        return len(self.chips[floor].difference(self.gens[floor])) == 0

    # Since objects will be deep copies, this needs to run only for the first one.
    def isValid(self):
        if not self.areDimensionsValid():
            return False
        return all(self.areChipsSafe(floor) for floor in self.floors())
    
    # Range of all floors
    def floors(self):
        return range(len(self.chips))
    
    # Generate neighbouring floors
    def getNextFloors(self):
        nextFloors = [self.floor - 1, self.floor + 1]
        return [floor for floor in nextFloors if floor in self.floors()]

    # Generate moveable item pairs on current floor
    # Its currently brute force, as sanity check comes after they've been moved
    def getMoveable(self):
        fromFloor = self.floor
        gens = self.gens[fromFloor]
        chips = self.chips[fromFloor]
        
        moveable = [(set(), {g}) for g in gens]
        moveable += [(set(), {g1, g2}) for g1 in gens for g2 in gens if g1 < g2]
        moveable += [({c}, set()) for c in chips]
        moveable += [({c1, c2}, set()) for c1 in chips for c2 in chips if c1 < c2]
        moveable += [({c}, {g}) for c in chips for g in gens]
        return moveable
    
    # Move (chipset, generatorset) from current floor to target floor
    # Return if the resulting state is valid
    def move(self, items, toFloor):
        fromFloor = self.floor
        chip, gen = items
        self.chips[toFloor].update(chip)
        self.chips[fromFloor].difference_update(chip)
        self.gens[toFloor].update(gen)
        self.gens[fromFloor].difference_update(gen)
        self.floor = toFloor
        
        return self.areChipsSafe(fromFloor) and self.areChipsSafe(toFloor)
    
    # Return the list of neighbouring states
    def getNeighbours(self):
        neighbours = {}
        nextFloors = self.getNextFloors()
        moveable = self.getMoveable()
        for toFloor in nextFloors:
            for m in moveable:
                newNeighbour = copy.deepcopy(self)
                isValidMove = newNeighbour.move(m, toFloor)
                if isValidMove:
                    direction = toFloor - self.floor
                    itemCount = len(m[0]) + len(m[1])
                    weight = State.calcWeight[(direction, itemCount)]
                    neighbours[newNeighbour] = {"weight" : weight}
        return neighbours
    
    # Difference of levels is the A* heuristic
    def level(self):
        itemCount = lambda floor : len(self.chips[floor]) + len(self.gens[floor])
        # Originally I used floor * itemCount instead of 10**floor * itemCount,
        # which was exponentially slower (35,000x slower for part 2)
        #return sum(floor * itemCount(floor) for floor in self.floors())
        return sum(10**floor * itemCount(floor) for floor in self.floors())

# Custom NetworkX graph object
# Implements functions for astar_path
class RadioisotopeTestingFacility:
    states = 0
    
    def __init__(self):
        self.adj = self
    
    def __getitem__(self, state):
        RadioisotopeTestingFacility.states += 1
        return state.getNeighbours()
        
    def __contains__(self, state):
        return state.isValid()
    
    def is_directed(self):
        return False
    
    def is_multigraph(self):
        return False

# Custom Timer object, prints out infos upon destruction
class PathTimer:
    def __init__(self):
        RadioisotopeTestingFacility.states = 0
        self.begin = time.process_time()
        
    def __del__(self):
        states = RadioisotopeTestingFacility.states
        elapsed = time.process_time() - self.begin
        print(f'States visited: {states}, Process time: {elapsed} seconds')


# Parse the inputfile to get the source state
# Abbreviate each item with its 2nd letter, eg. H = Thulium, L = Plutonium, etc.
def getSourceState(instructions):
    floor = 0
    chips = []
    gens = []
    
    getAbbr = lambda text : text[1].upper()
    
    for instruction in instructions:
        # Parse 'The first floor contains a thulium generator, a thulium-compatible
        # microchip, a plutonium generator, and a strontium generator.'
        pattern = 'The |, a | a |, and a | and a |\.| contains nothing relevant.| contains'
        tokens = re.split(pattern, instruction)
        floorname = tokens[1]
        items = tokens[3:-1]

        chip = set()
        gen = set()

        for item in items:
            name, type = map(getAbbr, item.split())
            if type == 'I':
                chip.add(name)
            elif type == 'E':
                gen.add(name)
            else:
                assert(False) # unknown type

        chips.append(chip)
        gens.append(gen)

    return State(floor, chips, gens)

def getTargetState(state):
    targetFloor = state.floors()[-1]
    targetState = copy.deepcopy(state)
    
    for fromFloor in targetState.floors():
        if fromFloor != targetFloor:
            targetState.floor = fromFloor
            allItems = (targetState.chips[fromFloor], targetState.gens[fromFloor])
            targetState.move(allItems, targetFloor)

    return targetState

# Difference of the level potential function heuristics for A*, this one rocks
def levelRise(s1, s2):
    return abs(s1.level() - s2.level())

# Sum the number of floor swaps for all items and the elevator
# This heuristic has proven entirely useless :-)
def swapCount(s1, s2):
    swaps = abs(s1.floor - s2.floor)
    for d1, d2 in ((s1.chips, s2.chips), (s1.gens, s2.gens)):
        dict = {}
        for floor in s1.floors():
            for item in d1[floor]:
                dict[item] = floor
        for floor in s2.floors():
            for item in d2[floor]:
                swaps += abs(dict[item] - floor)
    return swaps

def shortestPath(instructions, part2=False, bidirectional=False):
    timer = PathTimer()
    
    RTF = RadioisotopeTestingFacility()
    source = getSourceState(instructions)
    if part2:
        # New items on floor 1:
        # An elerium generator, an elerium-compatible microchip,
        # a dilithium generator, a dilithium-compatible microchip.
        source.chips[0].update({'E', 'D'})
        source.gens[0].update({'E', 'D'})
    target = getTargetState(source)
    
    if bidirectional:
        # Ye olde bidirectional search (slow)
        path = bidirectional_shortest_path(RTF, source, target)
    else:
        path = astar_path(RTF, source, target, heuristic=levelRise, weight="weight")
    for index, state in enumerate(path):
        print(index, state)

    return path

smallExample = [
    'The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.',
    'The second floor contains a hydrogen generator.',
    'The third floor contains a lithium generator.',
    'The fourth floor contains nothing relevant.']

assert len(shortestPath(smallExample)) == 12

# Display info message
print("\nGive a floor plan file:")
instructions = utility.readInputList()

# Display results
path = shortestPath(instructions)
path = shortestPath(instructions, part2 = True)

# Timer results (bidirectional_shortest_path):
# States visited:     111, Process time:    0.03125 seconds
# States visited:   31592, Process time:   18.421875 seconds
# States visited: 2358241, Process time: 2423.328125 seconds

# Timer results (astar_path with levelRise1 heuristic and weight1):
# States visited:     85, Process time:   0.03125 seconds
# States visited:  24544, Process time:  16.234375 seconds
# States visited: 861281, Process time: 887.625 seconds

# Timer results (astar_path with weight1 only):
# States visited:    101, Process time:   0.03125 seconds
# States visited:  24744, Process time:  16.515625 seconds
# States visited: 861945, Process time: 887.34375 seconds

# Timer results (astar_path with levelRise1 heuristic only):
# States visited:      72, Process time:    0.015625 seconds
# States visited:  112336, Process time:   80.0625 seconds
# States visited: 5602114, Process time: 6874.609375 seconds (YIKES!)

# Timer results (astar_path with levelRise2 heuristic only):
# States visited:  16, Process time: 0.015625 seconds
# States visited: 102, Process time: 0.0625 seconds
# States visited: 283, Process time: 0.203125 seconds (WOW!!!)

# Timer results (astar_path with levelRise2 heuristic and weight2):
# States visited:  14, Process time: 0.015625 seconds
# States visited:  62, Process time: 0.03125 seconds
# States visited: 203, Process time: 0.125 seconds (THE BEST so far)

# Timer results (astar_path with weight2 only):
# States visited:     58, Process time:   0.015625 seconds
# States visited:   9691, Process time:   6.0 seconds
# States visited: 558456, Process time: 625.65625 seconds

# Timer results (astar_path with no heuristic, no weight):
# States visited:    345, Process time:   0.09375 seconds
# States visited: 158158, Process time: 105.140625 seconds
# Ran out of memory (>2hours, around 8GB) :)