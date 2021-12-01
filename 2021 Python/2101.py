import utility # my own utility.py file
import numpy as np

smallExample ="""
199
200
208
210
200
207
240
269
260
263""".strip().split('\n')

def depthIncreaseRate(data, part2 = False):
    overlap = 3 if part2 else 1
    data = np.array(list(map(int, data)))
    
    return sum(data[overlap:] - data[:-overlap] > 0)

assert(depthIncreaseRate(smallExample) == 7)
assert(depthIncreaseRate(smallExample, True) == 5)

# Display info message
print("Give sonar sweep readings:\n");
depthMeasurements = utility.readInputList()

# Display results
print (f'{depthIncreaseRate(depthMeasurements) = }')
print (f'{depthIncreaseRate(depthMeasurements, part2 = True) = }')