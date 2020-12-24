import utility # my own utility.pl file

# Hexagonal layout:
#   x x x x x x x
#    x x x x x x
#   x x x x x x x
#    x x x x x x 
# Steps to directions table: 'step' -> (dx, dy)
directionTable = {
    'e':  ( 2,  0),
    'se': ( 1, -1),
    'sw': (-1, -1),
    'w':  (-2,  0),
    'nw': (-1,  1),
    'ne': ( 1,  1)}

# Number of hexagonal neighbours for tile (x, y) in the given tileset
def countNeighbours(tileset, x, y):
    return sum(int((x + dx, y + dy) in tileset) for dx, dy in directionTable.values())

# Builds the layout from the instructions and simulates the rounds.
def lobbyLayout(instructions, part2 = False):
    tileset = set()
    
    # Parse input
    for line in instructions:
        x, y = (0, 0)
        prev = ''
        for character in line:
            if character == 's' or character == 'n':
                prev = character
            else:
                step = prev + character
                dx, dy = directionTable[step]
                x += dx
                y += dy
                prev = ''
        if (x, y) in tileset:
            tileset.remove((x, y))
        else:
            tileset.add((x, y))

    initialBlacks = len(tileset)
    
    # Flip the tileset
    times = 100
    for round in range(times):
        t = set()
        for x, y in tileset:
            # Check x, y tile
            n = countNeighbours(tileset, x, y)
            if 1 <= n <= 2:
                t.add((x, y))
            # Check all neighbouring cells of tile x, y
            for dx, dy in directionTable.values():
                x2, y2 = x + dx, y + dy
                if ((x2, y2) in tileset or (x2, y2) in t):
                    continue
                n = countNeighbours(tileset, x2, y2)
                if n == 2:
                    t.add((x2, y2))
        tileset = t
    
    finalBlacks = len(tileset)
    
    solution = finalBlacks if part2 else initialBlacks 
    print(solution)
    return solution
    

# Check test cases
smallExample = """
sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew
""".strip().split('\n')
assert lobbyLayout(smallExample) == 10
assert lobbyLayout(smallExample, part2 = True) == 2208

# Display info message
print("Give a list of hexagonal step instructions:\n")
instructions = utility.readInputList()

# Display results
print(f'{lobbyLayout(instructions) = }')
print(f'{lobbyLayout(instructions, part2 = True) = }')