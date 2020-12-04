import utility # my own utility.pl file

# Counts the number of trees in a slope.
# A slope starts from the top left corner of the grid,
# and takes 'right' steps to the right and 'down' number of steps down
# in every iteration until reaching the bottom.
def countTrees(treeGrid, right = 3, down = 1):
    width = len(treeGrid[0])
    j = 0
    sumOfTrees = 0
    for i in range(0, len(treeGrid), down):
        if (treeGrid[i][j] == '#'): # tree found
            sumOfTrees += 1
        j = (j + right) % width
    return sumOfTrees

# Multiply tree counts in random slopes together 
def multiplySlopes(treeGrid):
    T = lambda right, down: countTrees(treeGrid, right, down)
    return T(1, 1) * T(3, 1) * T(5, 1) * T(7, 1) * T(1, 2)

# Check test cases
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
