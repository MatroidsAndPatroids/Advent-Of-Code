import utility # my own utility.py file
import numpy # sign
import re # split

# Find Hydrothermal Vent overlaps
def hydrothermalVents(data, part2=False):
    ocean = {}
    for line in data:
        # Parse
        x1, y1, x2, y2 = map(int, re.split(',| ->', line))
        delta = complex(numpy.sign(x2 - x1), numpy.sign(y2 - y1))
        start = complex(x1, y1)
        end = complex(x2, y2) + delta

        # Skip diagonal lines in part1
        if not part2 and delta.real != 0 and delta.imag != 0:
            continue

        # Simulate
        while start != end:
            ocean[start] = ocean.get(start, 0) + 1
            start += delta

    # Return
    value = sum(vents > 1 for vents in ocean.values())
    print(value)
    return value

# Verify test cases
smallExample = '''
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
'''.strip().split('\n')
assert(hydrothermalVents(smallExample) == 5)
assert(hydrothermalVents(smallExample, part2=True) == 12)

# Display info message
print("\nGive a list of hydrothermal vent line coordinates:");
lineCoordinates = utility.readInputList()

# Display results
print (f'{hydrothermalVents(lineCoordinates) = }')
print (f'{hydrothermalVents(lineCoordinates, part2=True) = }')