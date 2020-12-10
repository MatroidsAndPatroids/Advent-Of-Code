import utility # my own utility.pl file

def joltageDifferenceProduct(joltList, difference = 3):
    jolts = list(map(int, joltList))
    jolts.sort()
    diffs = {}
    
    for i in range(1, len(jolts)):
        diff = jolts[i] - jolts[i - 1]
        value = diffs.get(diff, 0)
        diffs[diff] = value + 1

    print(diffs)
    return (diffs[1] + 1) * (diffs[3] + 1)

def differentArrangements(joltList, difference = 3):
    joltList += '0'
    jolts = list(map(int, joltList))
    jolts.sort()
    jolts += [jolts[-1] + difference]
    
    count = 1
    ones = 0
    oneTable = {0:1, 1: 1, 2: 2, 3: 4, 4: 7, 5: 13}
    
    for i in range(1, len(jolts)):
        if jolts[i] == jolts[i - 1] + 1:
            ones += 1
        else:
            count *= oneTable[ones]
            ones = 0
    
    return count

def countNumberOfArrangements(jolts, difference = 3, start = 1):
    #print(jolts)
    count = 1
    
    for i in range(start, len(jolts) - 1):
        if (jolts[i + 1] - jolts[i - 1]) <= difference:
            smallerJolts = jolts[:i] + jolts[i + 1:]
            count += countNumberOfArrangements(smallerJolts, difference, i)
            
    return count

# Check test cases
smallExample = [
    '16',
    '10',
    '15',
    '5',
    '1',
    '11',
    '7',
    '19',
    '6',
    '12',
    '4']
largeExample = [
    '28',
    '33',
    '18',
    '42',
    '31',
    '14',
    '46',
    '20',
    '48',
    '47',
    '24',
    '23',
    '49',
    '45',
    '19',
    '38',
    '39',
    '11',
    '1',
    '32',
    '25',
    '35',
    '8',
    '17',
    '7',
    '9',
    '4',
    '2',
    '34',
    '10',
    '3']
assert joltageDifferenceProduct(smallExample, 3) == 35
assert joltageDifferenceProduct(largeExample, 3) == 220

print(f'{differentArrangements(smallExample, 3) = }')
#assert differentArrangements(smallExample, 3) == 8
print(f'{differentArrangements(largeExample, 3) = }')
#assert differentArrangements(largeExample, 3) == 19208

# Display info message
print("Give list of bags and contents:\n")
bagList = utility.readInputList()

# Display results
print(f'{joltageDifferenceProduct(bagList, 3) = }')
print(f'{differentArrangements(bagList, 3) = }')