import utility # my own utility.pl file (readInputList, SimpleTimer, md5hash)
import copy # deepcopy
import time # process_time
from statistics import mean
import sys # maxsizze
from networkx.algorithms.shortest_paths import astar_path
from networkx.algorithms.dag import dag_longest_path

# Custom NetworkX graph object
# Implements functions only for astar_path and dag_longest_path
class SecureVault:
    validCoord = lambda coord: all(val in range(4) for val in coord)
    openDoor = lambda char: 'b' <= char <= 'f'
    doorOrder = 'UDLR' # up, down, left, right
    validPath = lambda path: all(char in SecureVault.doorOrder for char in path)
    replacer = lambda text, index, newVal: text[:index] + newVal + text[index+1:]
    vaultPlot = '''
#########
# | | | #
#-#-#-#-#
# | | | #
#-#-#-#-#
# | | | #
#-#-#-#-#
# | | |  
####### V
'''.strip().split('\n')[1:-1]

    def __init__(self, passcode, target, defaultWeight=1, targetWeight=1):
        self.passcode = passcode
        self.target = target
        self.defaultWeight = defaultWeight
        self.targetWeight = targetWeight
        self.states = 0
        self.timer = utility.SimpleTimer()
        
    def __getitem__(self, state):
        self.states += 1
        coord, path = state
        
        neighbours = {}
        if coord == self.target[0]:
            # Reaching target has always weight infinity (which repels longest path)
            neighbours[self.target] = {"weight" : self.targetWeight}
            return neighbours
            
        hash = utility.md5hash(self.passcode + path)
        isOpen = list(map(SecureVault.openDoor, hash[:4]))
        x, y = coord
        adjacent = [(x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)]
        for i, adj in enumerate(adjacent):
            if SecureVault.validCoord(adj) and isOpen[i]:
                newState = (adj, path + SecureVault.doorOrder[i])
                neighbours[newState] = {"weight" : self.defaultWeight}
        return neighbours
    
    def __contains__(self, state):
        coord, path = state
        return SecureVault.validCoord(coord) and SecureVault.validPath(path)
    
    def is_directed(self):
        return True
    
    def is_multigraph(self):
        return False
    
    # Plot state of maze for debug
    def plotState(self, state):
        coord, _ = state
        x, y = 2 * coord[0] - 1, 2 * coord[1] - 1 # does 2 * coord - 1 work?
        plot = SecureVault.vaultPlot
        plot[y] = SecureVault.replacer(plot[y], x, 'S')
        
        neighbours = self.__getitem__(state)
        for n in neighbours.keys():
            coordn, _ = n
            xn, yn = 2 * coordn[0] - 1, 2 * coordn[1] - 1
            xDoor, yDoor = mean([x, xn]), mean([y, yn])
            plot[yDoor] = SecureVault.replacer(plot[yDoor], xDoor, ' ') 
        
        for line in plot:
            print(line)
    
    # Print out number of states visite in the end
    def __del__(self):
        self.timer.addText(f'States visited: {self.states}, ')

# Find shortest (part1), or longest (part2) path between source and target 
def optimalPath(source, target, passcode, part2=False):
    sourceState = (source, '')
    targetState = (target, '')
    manhattan = lambda c1, c2: abs(c1[0][0] - c2[0][0]) + abs(c1[0][1] - c2[0][1])
    
    if part2:
        # Infinite targetWeight repels longest path from target node
        inf = sys.maxsize
        SV = SecureVault(passcode, targetState, defaultWeight=-1, targetWeight=inf)
        path = astar_path(SV, sourceState, targetState, heuristic=manhattan)
    else:
        SV = SecureVault(passcode, targetState)
        path = astar_path(SV, sourceState, targetState, heuristic=None)
    
    route = path[-2][1]
    return len(route) if part2 else route

# Check test cases
assert optimalPath(source=(0, 3), target=(3, 0), passcode='ihgpwlah') == 'DDRRRD'
assert optimalPath(source=(0, 3), target=(3, 0), passcode='kglvqrro') == 'DDUDRLRRUDRD'
assert optimalPath(source=(0, 3), target=(3, 0), passcode='ulqzkmiv') == 'DRURDRUDDLLDLUURRDULRLDUUDDDRR'
assert optimalPath(source=(0, 3), target=(3, 0), passcode='ihgpwlah', part2=True) == 370
assert optimalPath(source=(0, 3), target=(3, 0), passcode='kglvqrro', part2=True) == 492
assert optimalPath(source=(0, 3), target=(3, 0), passcode='ulqzkmiv', part2=True) == 830

# Display info message
print("\nWhat's your passcode?")
passcode = utility.readInputList()[0]

# Display results
print(f'{optimalPath(source=(0, 3), target=(3, 0), passcode=passcode) = }\n')
print(f'{optimalPath(source=(0, 3), target=(3, 0), passcode=passcode, part2=True) = }\n')
