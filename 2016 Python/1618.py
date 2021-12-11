import utility # my own utility.pl file (readInputList, SimpleTimer, md5hash)
import numpy as np
from matplotlib import pyplot as plt
from scipy.ndimage import convolve1d

# Generate the floormap using scipy.ndimage.convolve1d on a 0-1 numpy array
def generateFloor(start, rows):
    kernel = np.array([1, 0, 1])
    convertToBinary = lambda tile : int(tile == '^')
    newRow = np.array(list(map(convertToBinary, start)))
    
    floor = [newRow]
    for _ in range(rows - 1):
        newRow = convolve1d(newRow, kernel, mode='constant', cval=0) % 2
        floor.append(newRow)
    return floor

# Plot safe tile frequency among the rows
def plotHistogram(safeCount, Width):
    Min = np.min(safeCount)
    Mean = np.mean(safeCount)
    Max = np.max(safeCount)
    Rows = np.size(safeCount)
    binsize = 1
    bins = np.arange(0, Width, binsize)
    
    plt.xlim([0, Width])
    plt.hist(safeCount, bins=bins, alpha=0.5)
    plt.title(f'{Min=}, {Mean=}, {Max=}, {Width=}, {Rows=}')
    plt.xlabel(f'number of safe tiles (bin size = {binsize})')
    plt.ylabel('count')
    plt.show()

# Calculate total number of safe tiles on the floor (plot histogram optionally)
def safeTiles(start, rows, plot=False):
    T = utility.SimpleTimer()
    floor = generateFloor(start, rows)
    safeCount = [np.count_nonzero(row==0) for row in floor]
    if plot:
        plotHistogram(safeCount, Width=len(start))
    return np.sum(safeCount)


# Check test cases
assert safeTiles(start='..^^.', rows=3) == 6
assert safeTiles(start='.^^.^.^^^^', rows=10) == 38

# Display info message
print("\nWhat's the starting row?")
start = utility.readInputList()[0]

# Display results
print(f'{safeTiles(start, rows=40) = }\n')
print(f'{safeTiles(start, rows=10000000) = }\n')