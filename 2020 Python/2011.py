import utility # my own utility.pl file
import copy # deepcopy

def seatsOccupied(row, col, seatArrangement):
    occupied = 0
    for i in range(max(0, row - 1), min(row + 2, len(seatArrangement))):
        for j in range(max(0, col - 1), min(col + 2, len(seatArrangement[i]))):
            if seatArrangement[i][j] == '#':
                occupied += 1
    #print(occupied - (seatArrangement[i][j] == '#'))
    #printIt(seatArrangement)
    return occupied # - int(seatArrangement[i][j] == '#')

def seatsOccupied2(row, col, seatArrangement):
    occupied = 0
    directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

    for deltaI, deltaJ in directions:
        newI = row + deltaI
        newJ = col + deltaJ
        while newI in range(len(seatArrangement)) and newJ in range(len(seatArrangement[newI])): 
            if seatArrangement[newI][newJ] == '#':
                occupied += 1
                break
            elif seatArrangement[newI][newJ] == 'L':
                break
            newI += deltaI
            newJ += deltaJ

    return occupied

def newState(seatArrangement, part2 = False):
    newArrangement = copy.deepcopy(seatArrangement)
    for i in range(len(seatArrangement)):
        for j in range(len(seatArrangement[i])):
            if part2:
                if seatArrangement[i][j] == '.':
                    continue
                if seatArrangement[i][j] == '#' and seatsOccupied2(i, j, seatArrangement) >= 5:
                    newArrangement[i][j] = 'L'
                elif seatArrangement[i][j] == 'L' and seatsOccupied2(i, j, seatArrangement) == 0:
                    newArrangement[i][j] = '#'
            else:
                if seatArrangement[i][j] == '.':
                    continue
                if seatArrangement[i][j] == '#' and seatsOccupied(i, j, seatArrangement) >= 5:
                    newArrangement[i][j] = 'L'
                elif seatArrangement[i][j] == 'L' and seatsOccupied(i, j, seatArrangement) == 0:
                    newArrangement[i][j] = '#'
    return newArrangement

def occupiedSeats(seatArrangement):
    occupied = 0
    for row in seatArrangement:
        for seat in row:
            if seat == '#':
                occupied += 1
    return occupied

def printIt(seatArrangement):
    for row in seatArrangement:
        print(''.join(row))
    print('')
            
def printOcc(seatArrangement):
    for row in range(len(seatArrangement)):
        line = ''
        for col in range(len(seatArrangement[row])):
            if seatArrangement[row][col] == '.':
                line += '.'
            else:
                line += str(seatsOccupied2(row, col, seatArrangement))
        print(line)
    print('')
            
def iterateUntil(seatArrangement, part2 = False):
    oldArrangement = list(map(list, seatArrangement))
    while True:
        #printIt(oldArrangement)
        #printOcc(oldArrangement)
        newArrangement = newState(oldArrangement, part2)
        if (newArrangement == oldArrangement):
            break
        oldArrangement = newArrangement
    print(occupiedSeats(oldArrangement))
    return occupiedSeats(oldArrangement)
         

# Check test cases
smallExample = [
    'L.LL.LL.LL',
    'LLLLLLL.LL',
    'L.L.L..L..',
    'LLLL.LL.LL',
    'L.LL.LL.LL',
    'L.LLLLL.LL',
    '..L.L.....',
    'LLLLLLLLLL',
    'L.LLLLLL.L',
    'L.LLLLL.LL']
smallExample2 = [
    '#.LL.L#.##',
    '#LLLLLL.L#',
    'L.L.L..L..',
    '#LLL.LL.L#',
    '#.LL.LL.LL',
    '#.LLLL#.##',
    '..L.L.....',
    '#LLLLLLLL#',
    '#.LLLLLL.L',
    '#.#LLLL.##']
assert iterateUntil(smallExample) == 37
assert iterateUntil(smallExample, part2 = True) == 26

# Display info message
print("Give a list of instructions:\n")
instructions = utility.readInputList()

# Display results
print(f'{iterateUntil(instructions) = }')
print(f'{iterateUntil(instructions, part2 = True) = }')