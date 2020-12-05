import utility # my own utility.pl file
import re # match

def seatNumber(boardingPass, part2 = False):
    seatNumber = 0
    magnitude = 64
    
    for c in boardingPass[:-3]:
        if c == 'F':
            seatNumber += 0
        elif c == 'B':
            seatNumber += magnitude
        magnitude = int(magnitude / 2)
    
    seatNumber *= 8
    magnitude = 4
    for c in boardingPass[-3:]:
        if c == 'L':
            seatNumber += 0
        elif c == 'R':
            seatNumber += magnitude
        magnitude = int(magnitude / 2)
    
    print(f'{boardingPass[:-3] = } {boardingPass[-3:] = } {seatNumber = }') 
    return seatNumber

def highestSeat(boardingPasses, part2 = False):
    highestSeat = 0
    for bp in boardingPasses:
        sN = seatNumber(bp, part2)
        highestSeat = max(highestSeat, sN)
    return highestSeat

def mySeatNumber(boardingPasses):
    allSeats = list(range(1024))
    for bp in boardingPasses:
        sN = seatNumber(bp)
        
        if sN in allSeats:
            #del allSeats.index(sN)
            allSeats.remove(sN)
    return allSeats

# Check test cases
smallExample = [
    'BFFFBBFRRR',
    'FFFBBBFRRR',
    'BBFFBBFRLL']
assert highestSeat(smallExample) == 820

# Display info message
print("Give passport batch file:\n")
passports = utility.readInputList()

# Display results
print(f'{highestSeat(passports) = }')
print(f'{mySeatNumber(passports) = }')