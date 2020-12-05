import utility # my own utility.pl file
import re # match

# The seat number is the binary version of the boarding pass, eg.
# 'BFFFBBFRRR' -> BIN 1000110111 -> DEC 567
def seatNumber(boardingPass):
    replaceTable = {"B": "1", "R": "1", "F": "0", "L": "0"}
    replaceFunction = lambda character: replaceTable[character]
    binary = ''.join(list(map(replaceFunction, boardingPass)))
    return int(binary, 2)

# Find the highest seat number in the list of boarding passes.
def highestSeatNumber(boardingPasses):
    existingSeatNumbers = list(map(seatNumber, boardingPasses))
    return max(existingSeatNumbers)

# My seat is the (only) empty seat on the plane.
# Find the set of missing numbers amongst the list of seat numbers.
def mySeatNumber(boardingPasses):
    existingSeatNumbers = list(map(seatNumber, boardingPasses))
    
    highest = highestSeatNumber(boardingPasses)
    lowest = min(existingSeatNumbers)
    allPossibleSeatNumbers = list(range(lowest, highest - 1))
    
    missingSeats = set(allPossibleSeatNumbers) - set(existingSeatNumbers)
    return missingSeats

# Check test cases
smallExample = [
    'BFFFBBFRRR',
    'FFFBBBFRRR',
    'BBFFBBFRLL']
assert highestSeatNumber(smallExample) == 820

# Display info message
print("Give boarding passes:\n")
boardingPasses = utility.readInputList()

# Display results
print(f'{highestSeatNumber(boardingPasses) = }')
print(f'{mySeatNumber(boardingPasses) = }')