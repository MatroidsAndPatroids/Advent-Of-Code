import utility # my own utility.pl file
import math # ceil
import sympy.ntheory.modular # crt or chinese reminder theorem

# Simulates the instructions
def shuttleBus(instructions, part2 = False):
    start = int(instructions[0])
    
    conv = lambda token: (0 if token == 'x' else int(token))
    buses = list(map(conv, instructions[1].split(',')))
    
    if part2:
        modulus = []
        right = []
        for i in range(len(buses)):
            # collect buses (all prime numbers!) and their indices times (-1)
            if buses[i] != 0:
                modulus += [buses[i]]
                right += [-i]

        solution = sympy.ntheory.modular.crt(modulus, right)
        print(solution)
        return solution[0]
    
    earliest = []
    mini = 1000000000
    b = -1
    index = -1
    for bus in buses:
        if bus != 0:
            val = bus * math.ceil(start / bus)
            earliest += [val]
            if val < mini:
                mini = val
                index = buses.index(bus)
                b = bus
    
    
    print(start, mini, index, b)
    return b * (mini - start)

# Check test cases
smallExample = [
    '939',
    '7,13,x,x,59,x,31,19']
assert shuttleBus(smallExample) == 295
assert shuttleBus(smallExample, part2 = True) == 1068781

# Display info message
print("Give a list of ship/waypoint movement instructions:\n")
instructions = utility.readInputList()

# Display results
print(f'{shuttleBus(instructions) = }')
print(f'{shuttleBus(instructions, part2 = True) = }')