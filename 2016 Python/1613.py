import utility # my own utility.pl file
import re # compile, match
import copy # deepcopy
import time # process_time
from networkx.algorithms.shortest_paths import astar_path
from networkx.algorithms.shortest_paths.unweighted import single_source_shortest_path


# Custom NetworkX graph object
# Implements functions for astar_path and single_source_shortest_path
class CubicleMaze:
    states = 0

    def __init__(self, seed):
        self.seed = seed
        self.adj = self
        
    def isOpenSpace(self, coordinate):
        x, y = coordinate
        if x < 0 or y < 0:
            return False
         
        hash = x*x + 3*x + 2*x*y + y + y*y
        hash += self.seed
        oneBits = bin(hash).count("1")
        return oneBits % 2 == 0
        
    def __getitem__(self, coordinate):
        CubicleMaze.states += 1
        
        x, y = coordinate
        adjacent = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        neighbours = {}
        for coord in adjacent:
            if self.isOpenSpace(coord):
                neighbours[coord] = {"weight" : 1}
        return neighbours
    
    def __contains__(self, coordinate):
        return self.isOpenSpace(coordinate)
    
    def is_directed(self):
        return False
    
    def is_multigraph(self):
        return False
    
    # Plot path on maze for debug
    def plotPath(self, xMax, yMax, path):
        firstLine = ' \t'
        for x in range(xMax):
            firstLine += str(x % 10)
            
        print(firstLine)
        for y in range(yMax):
            line = str(y) + '\t'
            for x in range(xMax):
                #line += 'O' if (x, y) in path.keys() else '.' if self.isOpenSpace((x, y)) else '#'
                line += '#' if not self.isOpenSpace((x, y)) else 'O' if (x, y) in path else '.'
            print(line)

# Custom Timer object, prints out infos upon destruction
class PathTimer:
    def __init__(self):
        CubicleMaze.states = 0
        self.begin = time.process_time()
        
    def __del__(self):
        elapsed = time.process_time() - self.begin
        states = CubicleMaze.states
        print(f'States visited: {states}, Process time: {elapsed} seconds')


def shortestPathLength(source, target, seed, part2=False):
    PT = PathTimer()
    CM = CubicleMaze(seed)
    cutoff = sum(target)
    
    if part2:
        paths = single_source_shortest_path(CM, source, cutoff=cutoff)
        path = paths.keys()
    else:
        manhattan = lambda c1, c2: abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])
        path = astar_path(CM, source, target, heuristic=manhattan, weight="weight")
        
    CM.plotPath(cutoff, cutoff, path)
    return len(path) if part2 else len(path) - 1


# Check test cases
assert shortestPathLength(source=(1, 1), target=(7, 4), seed=10) == 11

# Display info message
print("\nWhat's the officer designer's favourite number?")

# Display results
print(f'{shortestPathLength(source=(1, 1), target=(31, 39), seed=1364) = }\n')
print(f'{shortestPathLength(source=(1, 1), target=(50, 0), seed=1364, part2=True) = }\n')