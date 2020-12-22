import utility # my own utility.pl file

jumpTable = {
    'N': lambda val: (0, val, 0),
    'S': lambda val: (0, -val, 0),
    'E': lambda val: (val, 0, 0),
    'W': lambda val: (-val, 0, 0),
    'L': lambda val: (0, 0, val),
    'R': lambda val: (0, 0, -val),
    'F': lambda val: (0, 0, 0)}

dirTable = {
    0  : 'E',
    90 : 'N',
    180: 'W',
    270: 'S'}

rotTable = {
    0  : lambda x, y: (x, y),
    90 : lambda x, y: (-y, x),
    180: lambda x, y: (-x, -y),
    270: lambda x, y: (y, -x)}

# Simulates the instructions
def emulate(instructions, part2 = False):
    sol = 0
    
    for line in instructions:
        op = line[0]
        val = int(line[1:])

    print(sol)
    return sol if part2 else sol

# Check test cases
smallExample = """
F10
N3
F7
R90
F11
""".strip().split('\n')
assert emulate(smallExample) == 25
assert emulate(smallExample, part2 = True) == 286

# Display info message
print("Give a list of ship/waypoint movement instructions:\n")
instructions = utility.readInputList()

# Display results
print(f'{emulate(instructions) = }')
print(f'{emulate(instructions, part2 = True) = }')