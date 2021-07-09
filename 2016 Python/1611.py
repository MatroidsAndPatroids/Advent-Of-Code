import utility # my own utility.pl file
import re # compile, match
import copy # deepcopy
import time # process_time
from networkx.algorithms.shortest_paths.unweighted import bidirectional_shortest_path

# Node object for the custom NetworkX graph object
# It can calculate its own neighbour objects.
class State:
    states = 0
    
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
        neighbours = []
        nextFloors = self.getNextFloors()
        moveable = self.getMoveable()
        for toFloor in nextFloors:
            for m in moveable:
                newNeighbour = copy.deepcopy(self)
                isValidMove = newNeighbour.move(m, toFloor)
                if isValidMove:
                    neighbours.append(newNeighbour)
                    State.states += 1
        return neighbours

# Custom NetworkX graph object
# Implements only the necessary functions for bidirectional_shortest_path
class RadioisotopeTestingFacility:
    class AdjacencyWrapper:
        def __getitem__(self, state):
            return state.getNeighbours()
        
    def __init__(self):
        self.adj = RadioisotopeTestingFacility.AdjacencyWrapper()
    
    def __contains__(self, state):
        return state.isValid()
    
    def is_directed(self):
        return False

# Custom Timer object, prints out infos upon destruction
class PathTimer:
    def __init__(self):
        State.states = 0
        self.begin = time.process_time()
        
    def __del__(self):
        elapsed = time.process_time() - self.begin
        print(f'States visited: {State.states}, Process time: {elapsed} seconds')


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

def shortestPath(instructions, part2 = False):
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
    
    path = bidirectional_shortest_path(RTF, source, target)
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

# Timer results:
# States visited:      311, Process time:    0.03125 seconds
# States visited:   123455, Process time:   17.328125 seconds
# States visited: 12740306, Process time: 2377.109375 seconds