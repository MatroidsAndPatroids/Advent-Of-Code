import utility # my own utility.pl file
import math #  prod

transformationTable = {
    0: lambda x, y: (x, y), # id, left side 0 <-> 4
    1: lambda x, y: (-1 - y, x), # -90, bottom side 1 <-> 5
    2: lambda x, y: (-1 - x, -1 - y), # 180, right side 2 <-> 6
    3: lambda x, y: (y, -1 - x), # 90, top side 3 <-> 7
    4: lambda x, y: (x, -1 - y), # vertical flip, right reversed
    5: lambda x, y: (y, x), # 90 vertical flip, top reversed
    6: lambda x, y: (-1 - x, y), # horizontal flip, left reversed
    7: lambda x, y: (-1 - y, -1 - x)} # -90 vertical flip, bottom reversed

def transformArray(array, transformation = 1):
    t = transformationTable[transformation]
    n = len(array)
    rotated = ['' for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            x, y = t(i, j)
            rotated[i] += array[x][y]
    
    return rotated

class Tile:
    def __init__(self, num, arr):
        self.num = num
        self.array = arr
        self.nb = {}
        
    def __str__(self):
        str = f'Tile {self.num}\n'
        for line in self.array:
            str += line + '\n'
        str += self.nb.__str__() + '\n'
        return str
    
    def side(self, i, j):
        if j == 0:
            # top or bottom
            return self.array[min(i, 0)]
        # left or right
        return [line[min(-j, 0)] for line in self.array]
    
    def compare(self, other):
        # Rotate/Flip 'other' into the correct position, if such position exists
        #print(self.num, other.num)
        for transform in range(8):
            #print(other)
            for i, j in [(0, 1), (-1, 0), (1, 0), (0, -1)]:
                if self.side(i, j) == other.side(-i, -j):
                    self.nb[(i, j)] = other
                    other.nb[(-i, -j)] = self
                    return other.num
            if other.degree() > 0:
                return None
            if transform == 3:
                other.transform(4)
            elif transform < 7:
                other.transform()
        return None
    
    def degree(self):
        return len(self.nb)
        
    def transform(self, transformation = 1):
        self.array = transformArray(self.array, transformation)

# Simulates the instructions
def emulate(instructions, part2 = False):
    # Parse input
    tiles = {}
    num = -1
    array = []
    for line in instructions:
        if not line:
            tiles[num] = Tile(num, array)
        elif 'Tile ' in line:
            num = int(line.split()[1][:-1])
            array = []
        else:
            array += [line]
    tiles[num] = Tile(num, array)

    # Find connections between tile pairs
    firstKey = next(iter(tiles))
    stack = [firstKey]
    while stack:
        currentTile = tiles[stack.pop()]
        for n, t in tiles.items():
            if n != currentTile.num and currentTile.compare(t) and t.degree() == 1:
                # we found t for the first time
                stack += [n]
        #print(currentTile)
    
    # Filter out corners
    corners = [tile for tile in tiles.values() if tile.degree() == 2]
    cornerIdProduct = math.prod(tile.num for tile in corners)
    
    # Start arranging from top left
    topLeft = [tile for tile in corners if
               all(i >= 0 and j >= 0 for i, j in tile.nb.keys())][0]
    arrangement = [[topLeft]]
    
    # Find the first column
    modified = True
    while modified:
        modified = False
        for (i, j), tile in arrangement[-1][0].nb.items():
            if i > 0:
                modified = True
                arrangement += [[tile]]
                break
    
    # Find each row
    for row in arrangement:
        modified = True
        while modified:
            modified = False
            for (i, j), tile in row[-1].nb.items():
                if j > 0:
                    modified = True
                    row += [tile]
                    break
    
    # Print ID grid for debug
    arrId = [[tile.num for tile in row] for row in arrangement]
    #print(arrId)
    
    # Assemble image
    image = []
    for row in arrangement:
        lines = [''] * 8
        for tile in row:
            for i in range(8):
                lines[i] += tile.array[8 - i][1:-1]
        image += lines
    
    # Count seamonsters
    numSeamonster = 0
    for transformation in range(8):
        for i in range(len(image) - len(seamonster)):
            for j in range(len(image[i]) - len(seamonster[0])):
                newMonster = 1
                for k in range(len(seamonster)):
                    for l in range(len(seamonster[k])):
                        if seamonster[k][l] == '#' and image[i + k][j + l] == '.':
                            newMonster = 0
                            break
                    if newMonster == 0:
                        break
                if newMonster == 1:
                    for k in range(len(seamonster)):
                        line = list(image[i + k])
                        for l in range(len(seamonster[k])):
                            if seamonster[k][l] == '#':
                                line[j + l] = 'O'
                        image[i + k] = ''.join(line)
                numSeamonster += newMonster
        if transformation == 3:
            image = transformArray(image, 4)
        elif transformation < 7:
            image = transformArray(image)
    #debug = [print(line) for line in image]
    #print(numSeamonster)
    
    # Water roughness level is the number of '#' that are not part of any seamonster
    waterRoughness = sum(line.count('#') for line in image)
    #print(waterRoughness)
    
    sol = waterRoughness if part2 else cornerIdProduct
    print(sol)
    return sol

# Check test cases
smallExample = """
Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...
""".strip().split('\n')
seamonster = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
""".strip('\n').split('\n')
assert emulate(smallExample) == 20899048083289
assert emulate(smallExample, part2 = True) == 273

# Display info message
print("Give a list of ship/waypoint movement instructions:\n")
instructions = utility.readInputList()

# Display results
print(f'{emulate(instructions) = }')
print(f'{emulate(instructions, part2 = True) = }')