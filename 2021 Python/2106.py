import utility # my own utility.py file

# Simulate Lantern Fish growth
def lanternFish(initialFish, days=80):
    # Parse
    initialFish = list(map(int, initialFish[0].split(',')))
    fish = {}
    for i in range(-1, 9):
        fish[i] = 0
    for f in initialFish:
        fish[f] += 1

    # Simulate
    for d in range(days):
        for i in range(-1, 8):
            fish[i] = fish[i + 1]
        fish[8] = fish[-1]
        fish[6] += fish[-1]
        fish[-1] = 0

    # Return
    value = sum(fish.values())
    print(value)
    return value

# Verify test cases
smallExample = '''
3,4,3,1,2
'''.strip().split('\n')
assert lanternFish(smallExample, days=80) == 5934
assert lanternFish(smallExample, days=256) == 26984457539

# Display info message
print("\nGive initial fish timers:")
initialFish = utility.readInputList()

# Display results
print (f"{lanternFish(initialFish, days=80) = }")
print (f"{lanternFish(initialFish, days=256) = }")