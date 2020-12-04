import utility # my own utility.pl file

def countTrees(treeGrid, right = 3, down = 1):
    width = len(treeGrid[0])
    j = 0
    sumOfTrees = 0
    for i in range(0, len(treeGrid), down):
        if (treeGrid[i][j] == '#'): # tree found
            sumOfTrees += 1
        j = (j + right) % width
    return sumOfTrees

def multiplySlopes(treeGrid):
    return countTrees(treeGrid, 1, 1) * countTrees(treeGrid, 3, 1) * countTrees(treeGrid, 5, 1) * countTrees(treeGrid, 7, 1) * countTrees(treeGrid, 1, 2) 
    
smallExample = [
    '..##.......',
    '#...#...#..',
    '.#....#..#.',
    '..#.#...#.#',
    '.#...##..#.',
    '..#.##.....',
    '.#.#.#....#',
    '.#........#',
    '#.##...#...',
    '#...##....#',
    '.#..#...#.#']
assert countTrees(smallExample, right = 3, down = 1) == 7
assert multiplySlopes(smallExample) == 336

# Display info message
print("Tree list for the toboggan:\n")
treeGrid = utility.readInputList()

# Display results
print(f'{countTrees(treeGrid, right = 3, down = 1) = }')
print(f'{multiplySlopes(treeGrid) = }')
