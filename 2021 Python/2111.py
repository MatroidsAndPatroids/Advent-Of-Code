import utility # my own utility.py file
import numpy as np # array



# Increase adjacent octopus energy levels 
def tryToFlash(octopuses, i, j):
    if octopuses[i][j] <= 9:
        return 0
    
    flashes = 1
    octopuses[i][j] = 0

    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            k = i + di
            l = j + dj
            if octopuses[k][l] > 0:
                octopuses[k][l] += 1
                if octopuses[k][l] > 9:
                    flashes += tryToFlash(octopuses, k, l)

    return flashes
    
# Simulate octopus energy gain, return final flash count or synchronizing step number
def energyLevel(octopuses, part2=False):
    # Parse
    table = []
    for line in octopuses:
        row = list(map(int, list(line)))
        table.append(row)

    steps = 1000000000 if part2 else 100
    octopuses = np.array(table)
    numberOfOctopuses = octopuses.size
    # Pad the array with a frame of length one, containing all -steps values
    octopuses = np.pad(octopuses, ((1, 1), (1, 1)), 'constant', constant_values=-steps)

    # Simulate
    flashCount = 0
    for step in range(steps):
        stepFlashes = 0
        octopuses += 1
        
        for i in range(1, len(octopuses) - 1):
            for j in range(1, len(octopuses[i]) - 1):
                stepFlashes += tryToFlash(octopuses, i, j)

        flashCount += stepFlashes
        if stepFlashes == numberOfOctopuses:
            # All octopuses were flashing simultaneously
            break

    # Return
    value = step + 1 if part2 else flashCount
    print(value)
    return value

# Verify test cases
smallExample = '''
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
'''.strip().split('\n')
assert energyLevel(smallExample) == 1656
assert energyLevel(smallExample, part2=True) == 195

# Display info message
print("\nGive Dumbo Octopus initial energy levels:")
octopuses = utility.readInputList()

# Display results
print (f"{energyLevel(octopuses) = }")
print (f"{energyLevel(octopuses, part2=True) = }")