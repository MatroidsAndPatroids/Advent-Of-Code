import utility # my own utility.pl file
import re # match

# Jump table for part2: key, value -> isValid (True or False)
jumpTable = {
    'acc': lambda value: (value, 1),
    'jmp': lambda value: (0, value),
    'nop': lambda value: (0, 1)}

# Counts the number of valid passports in the list.
def countValidPassports(passports, part2 = False):
    accumulator = 0
    visited = {}
    currentOperation = 0
    
    while currentOperation not in visited.keys() and 0 <= currentOperation < len(passports):
        visited[currentOperation] = 1
        operator, value = passports[currentOperation].split()
        print(f'{operator = } {value = }')
        accDiff, jump = jumpTable[operator](int(value))
        currentOperation += jump
        accumulator += accDiff

    return accumulator

# Counts the number of valid passports in the list.
def countValidPassports(passports, part2 = False):
    print(passports)
    accumulator = 0
    visited = {}
    currentOperation = 0
    infiniteLoop = False
    
    while 0 <= currentOperation < len(passports):
        visited[currentOperation] = 1
        operator, value = passports[currentOperation].split()
        #print(f'{operator = } {value = }')
        accDiff, jump = jumpTable[operator](int(value))
        currentOperation += jump
        accumulator += accDiff
        
        if currentOperation in visited.keys():
            infiniteLoop = True
            break

    return accumulator, infiniteLoop

def countPart2(passports):
    for i in range(len(passports)):
        if 'jmp' in passports[i]:
            passports[i] = passports[i].replace('jmp', 'nop')
        elif 'nop' in passports[i]:
            passports[i] = passports[i].replace('nop', 'jmp')
        
        acc, infi = countValidPassports(passports)
        print(f'{passports[i] = } {acc = } {infi = }')
        if not infi:
            return acc
        
        if 'jmp' in passports[i]:
            passports[i] = passports[i].replace('jmp', 'nop')
        elif 'nop' in passports[i]:
            passports[i] = passports[i].replace('nop', 'jmp')
            
    return -1

# Check test cases
smallExample = [
    'nop +0',
    'acc +1',
    'jmp +4',
    'acc +3',
    'jmp -3',
    'acc -99',
    'acc +1',
    'jmp -4',
    'acc +6']
print(countValidPassports(smallExample))
assert countValidPassports(smallExample) == (5, True)
print(countPart2(smallExample))
assert countPart2(smallExample) == 8



# Display info message
print("Give passport batch file:\n")
passports = utility.readInputList()

# Display results
print(f'{countValidPassports(passports) = }')
print(f'{countPart2(passports) = }')