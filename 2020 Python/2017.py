import utility # my own utility.pl file
import copy # deepcopy
import math # floor, ceil

def print3dCube(cube):
    for square in cube:
        for line in square:
            print(''.join(line))
        print('')

def print4dCube(cubes):
    s = 0
    for cube in cubes:
        print('Cube', s)
        print3dCube(cube)
        print('')
        s += 1

def neighbours3d(cube, x, y, z):
    n = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
                for dz in [-1, 0, 1]:
                    x2 = x + dx
                    y2 = y + dy
                    z2 = z + dz
                    if (x2 in range(len(cube)) and y2 in range(len(cube[x2]))
                        and z2 in range(len(cube[x2][y2])) and cube[x2][y2][z2] == '#'):
                        n += 1
    return n
        
def neighbours4d(cubes, x, y, z, w):
    n = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
                for dz in [-1, 0, 1]:
                    for dw in [-1, 0, 1]:
                        x2 = x + dx
                        y2 = y + dy
                        z2 = z + dz
                        # RIP: here it stood w2 = w + dz and I did not notice for 1 hour
                        w2 = w + dw
                        if (x2 in range(len(cubes)) and y2 in range(len(cubes[x2]))
                            and z2 in range(len(cubes[x2][y2])) and w2 in range(len(cubes[x2][y2][z2]))
                            and cubes[x2][y2][z2][w2] == '#'):
                            n += 1
    return n

def emptyLine(dimension):
    return copy.deepcopy(['.' for k in range(dimension)])

def emptySquare(dimension):
    return copy.deepcopy([emptyLine(dimension) for k in range(dimension)])

def emptyCube(dimension):
    return copy.deepcopy([emptySquare(dimension) for k in range(dimension)])

def numberOfActiveCubes(cubes):
    return sum(sum(sum(line.count('#') for line in square) for square in cube) for cube in cubes)

# Simulates the instructions
def emulateConvayCubes(instructions, part2 = False):
    d = len(instructions)
    cubes = [[list(line) for line in instructions]] # one square in cubes
    for i in range(math.floor(d / 2)):
        cubes = [emptySquare(d)] + cubes # pad cubes with empty squares from above
    for i in range(math.ceil(d / 2) - 1):
        cubes += [emptySquare(d)] # pad cubes with empty squares from below
    
    if part2:
        cubes = [cubes]
        for i in range(math.floor(d / 2)):
            cubes = [emptyCube(d)] + cubes # pad cubes with empty cubes from 'above4d'
        for i in range(math.ceil(d / 2) - 1):
            cubes += [emptyCube(d)] # pad cubes with empty cubes from 'below4d'
    
    maxNeighbours = 0
    if part2:
        for i in range(6):
            olddim = len(cubes)
            d = len(cubes) + 2
            for x in range(len(cubes)):
                assert len(cubes[x]) == olddim
                for y in range(len(cubes[x])):
                    assert len(cubes[x][y]) == olddim
                    for z in range(len(cubes[x][y])):
                        assert len(cubes[x][y][z]) == olddim
                        cubes[x][y][z] = ['.'] + cubes[x][y][z] + ['.']
                    cubes[x][y] = [emptyLine(d)] + cubes[x][y] + [emptyLine(d)]
                cubes[x] = [emptySquare(d)] + cubes[x] + [emptySquare(d)]
            cubes = [emptyCube(d)] + cubes + [emptyCube(d)]
            # Deepcopy version
            
            newCubes = copy.deepcopy(cubes)       
            assert len(newCubes) == d
            for x in range(len(newCubes)):
                assert len(newCubes[x]) == d
                for y in range(len(newCubes[x])):
                    assert len(newCubes[x][y]) == d
                    for z in range(len(newCubes[x][y])):
                        assert len(newCubes[x][y][z]) == d
                        for w in range(len(newCubes[x][y][z])):
                            n = neighbours4d(cubes, x, y, z, w)
                            maxNeighbours = max(maxNeighbours, n)
                            if cubes[x][y][z][w] == '#' and not 3 <= n <= 4:
                                newCubes[x][y][z][w] = '.'
                            elif cubes[x][y][z][w] == '.' and n == 3:
                                newCubes[x][y][z][w] = '#'
            cubes = newCubes
            #print4dCube(cubes)
    else:
        for i in range(6):
            d = len(cubes) + 2
            for x in range(len(cubes)):
                for y in range(len(cubes[x])):
                    cubes[x][y] = ['.'] + cubes[x][y] + ['.']
                cubes[x] = [['.'] * d] + cubes[x] + [['.'] * d]
            cubes = [[['.'] * d] * d] + cubes + [[['.'] * d] * d]
            # Non-deepcopy version
    
            newCubes = copy.deepcopy(cubes)       
            assert len(newCubes) == d
            for x in range(len(newCubes)):
                assert len(newCubes[x]) == d
                for y in range(len(newCubes[x])):
                    assert len(newCubes[x][y]) == d
                    for z in range(len(newCubes[x][y])):
                        n = neighbours3d(cubes, x, y, z)
                        maxNeighbours = max(maxNeighbours, n)
                        if cubes[x][y][z] == '#' and not 3 <= n <= 4:
                            newCubes[x][y][z] = '.'
                        elif cubes[x][y][z] == '.' and n == 3:
                            newCubes[x][y][z] = '#'
            cubes = newCubes
            #print3dCube(cubes)

    if not part2:
        cubes = [cubes]
    activeCubes = numberOfActiveCubes(cubes)
    print(activeCubes, maxNeighbours)
    return activeCubes

# Check test cases
smallExample = """
.#.
..#
###
""".strip().split('\n')
assert emulateConvayCubes(smallExample) == 112
assert emulateConvayCubes(smallExample, part2 = True) == 848

# Display info message
print("Give the lines of the inner square for the Convay Cube:\n")
instructions = utility.readInputList()

# Display results
print(f'{emulateConvayCubes(instructions) = }')
print(f'{emulateConvayCubes(instructions, part2 = True) = }')