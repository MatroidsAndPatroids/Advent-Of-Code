import utility # my own utility.pl file

# Jump table: operator, value -> (accumulator delta, jump delta)
jumpTable = {
    'acc': lambda deltaAcc: (deltaAcc, 1),
    'jmp': lambda jump: (0, jump),
    'nop': lambda dummy: (0, 1)}

# Jump table for part2: oldOperator -> newOperator
replaceOperator = {
    'jmp': 'nop',
    'nop': 'jmp'}

# Simulates the instructions until the first repeat or termination.
# Returns the accelerator value in the end and a True/False value,
# whether it is an infinite loop or the execution stops normally.
# When replaceIndex is given, it will replace the operator given by it.
def simulateBootCode(instructions, replaceIndex = -1):
    accumulator = 0 # single global value
    currentIndex = 0 # current instruction to execute
    visitedIndex = set() # store all visited indexes as a set
    infiniteLoop = False # set to True if we encounter an infinite loop
    
    while currentIndex in range(len(instructions)): # while instruction is valid
        visitedIndex.add(currentIndex)
        # eg. instructions[currentIndex] = 'acc +1'
        operator, value = instructions[currentIndex].split()
        
        if replaceIndex == currentIndex: # part 2
            operator = replaceOperator.get(operator, operator)
            
        deltaAcc, jump = jumpTable[operator](int(value))
        currentIndex += jump
        accumulator += deltaAcc
        
        if currentIndex in visitedIndex: # infinite loop is found
            infiniteLoop = True
            break

    return accumulator, infiniteLoop

# Try to replace each line one by one if it solves the infinite loop problem.
# Return the accumulator value at termination for the first solution and its index.
def accumulatorValueAfterReplace(instructions):
    for index in range(len(instructions)):
        accumulator, infiniteLoop = simulateBootCode(instructions, index)
        if not infiniteLoop:
            # the instruction at index terminates with no infinite loop after replace
            return accumulator, index
     
    return -1, -1

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
assert simulateBootCode(smallExample) == (5, True)
assert accumulatorValueAfterReplace(smallExample) == (8, 7)

# Display info message
print("Give a list of instructions:\n")
instructions = utility.readInputList()

# Display results
print(f'{simulateBootCode(instructions) = }')
print(f'{accumulatorValueAfterReplace(instructions) = }')