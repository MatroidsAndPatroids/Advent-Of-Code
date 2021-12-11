import utility # my own utility.py file
import numpy as np



def getNeighbours(i, j):
    return [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]

# Simulate Lantern Fish growth
def smokeBasin(heightmap, part2=False):
    # Parse
    heightmap = [list(map(int, list(line))) for line in heightmap]
    heightmap = np.array(heightmap)
    # Pad the height map with a frame of length one, containing all 9 values
    heightmap = np.pad(heightmap, ((1, 1), (1, 1)), 'constant', constant_values=9)

    # Part 1 - collect all the low points
    lowPoints = []
    for i in range(1, len(heightmap) - 1):
        for j in range(1, len(heightmap[i]) - 1):
            if (heightmap[i][j] < min(heightmap[k][l] for (k, l) in getNeighbours(i, j))):
                lowPoints.append((i, j))

    # Part 2 - collect all the basin sizes
    basinSizes = []
    for i, j in lowPoints:
        seen = [(i, j)]
        next = [(i, j)]
        basinSize = 1

        # DFS search
        while next:
            k, l = next.pop()
            for m, n in getNeighbours(k, l):
                if (m, n) not in seen and heightmap[k][l] < heightmap[m][n] < 9:
                    seen.append((m, n))
                    next.append((m, n))
                    basinSize += 1

        basinSizes.append(basinSize)

    # Return
    basinSizes = np.array(sorted(basinSizes))
    riskLevel = lambda ij : heightmap[ij[0]][ij[1]] + 1
    value = np.prod(basinSizes[-3:]) if part2 else sum(map(riskLevel, lowPoints))
    print(value)
    return value

# Verify test cases
smallExample = '''
2199943210
3987894921
9856789892
8767896789
9899965678
'''.strip().split('\n')
assert smokeBasin(smallExample) == 15
assert smokeBasin(smallExample, part2=True) == 1134

# Display info message
print("\nGive lava cave height map:")
heightmap = utility.readInputList()

# Display results
print (f"{smokeBasin(heightmap) = }")
print (f"{smokeBasin(heightmap, part2=True) = }")