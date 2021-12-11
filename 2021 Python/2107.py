import utility # my own utility.py file

# Actually I've solved this one with brute force in MS Excel
# Then I've found this explicit solution

# Lowest amount of fuel for all crabs to reach the same position
def lowestFuel(crabPositions, part2=False):
    # Parse
    crabPositions = list(map(int, crabPositions[0].split(',')))
    crabPositions.sort()
    
    # Calculate lowest fuels
    median = crabPositions[len(crabPositions)//2]
    fuel1 = lambda pos: sum(abs(crab - pos) for crab in crabPositions)
    
    average = sum(crabPositions) // len(crabPositions)
    fuel2 = lambda pos : sum(abs(crab - pos) * (abs(crab - pos) + 1) // 2 for crab in crabPositions)

    # Return
    value = min(fuel2(average), fuel2(average + 1)) if part2 else fuel1(median)
    print(value)
    return value

# Verify test cases
smallExample = '''
16,1,2,0,4,2,7,1,2,14
'''.strip().split('\n')
assert lowestFuel(smallExample) == 37
assert lowestFuel(smallExample, part2=True) == 168

# Display info message
print("\nGive crab horizontal positions:")
crabPositions = utility.readInputList()

# Display results
print (f"{lowestFuel(crabPositions) = }")
print (f"{lowestFuel(crabPositions, part2=True) = }")