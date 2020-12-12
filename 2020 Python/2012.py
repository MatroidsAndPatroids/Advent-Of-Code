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
def simulateShipMovement(instructions, part2 = False):
    x = 0
    y = 0
    dir = 0
    
    wx = 10
    wy = 1
    wdir = 0
    
    for ins in instructions:
        op = ins[0]
        val = int(ins[1:])
        print(f'{op = } {val = }: {x = } {y = } {dir = } {wx = } {wy = } {wdir = }')
        
        dx, dy, dd, dwx, dwy, dwd = (0, 0, 0, 0, 0, 0)
        
        if op == 'F':
            if part2:
                #rotwx, rotwy = rotTable[wdir](wx, wy)
                dx = val * wx
                dy = val * wy
            else:
                op = dirTable[dir]
        
        if part2:
            dwx, dwy, dwd = jumpTable[op](val)
        else:
            dx, dy, dd = jumpTable[op](val)
      
        x += dx
        y += dy
        wx += dwx
        wy += dwy
        dir = (dir + dd) % 360
        #wdir = (wdir + dwd) % 360
        
        if dwd % 360 > 0:
            wx, wy = rotTable[dwd % 360](wx, wy)
        
        print(f'\t\t{dx = } {dy = } {dd = } {dwx = } {dwy = } {dwd = }')

        
    print(f'{x = } {y = } {dir = }')
    return abs(x) + abs(y)

# Check test cases
smallExample = [
    'F10',
    'N3',
    'F7',
    'R90',
    'F11']
assert simulateShipMovement(smallExample) == 25
assert simulateShipMovement(smallExample, part2 = True) == 286

# Display info message
print("Give a list of ship/waypoint movement instructions:\n")
instructions = utility.readInputList()

# Display results
print(f'{simulateShipMovement(instructions) = }')
print(f'{simulateShipMovement(instructions, part2 = True) = }')