import utility # my own utility.pl file

# Simulate the memory game the Elves are playing
def memoryGame(startingNumbers, part2 = False):
    numbers = list(map(int, startingNumbers[0].split(',')))
    age = {}
    for index in range(len(numbers) - 1):
        age[numbers[index]] = index # initialize dictionary
    
    lastTurn = 30000000 if part2 else 2020
    prevNum = numbers[-1]
    
    for index in range(len(numbers) - 1, lastTurn - 1):
        currentNum = index - age[prevNum] if prevNum in age.keys() else 0
        age[prevNum] = index
        prevNum = currentNum

    print(prevNum, len(age.keys()))
    return prevNum

# Check test cases
smallExample = """
0,3,6
""".strip().split('\n')
assert memoryGame(smallExample) == 436
assert memoryGame(smallExample, part2 = True) == 175594

# Display info message
print("Give a list of startingNumbers:\n")
startingNumbers = utility.readInputList()

# Display results
print(f'{memoryGame(startingNumbers) = }')
print(f'{memoryGame(startingNumbers, part2 = True) = }')