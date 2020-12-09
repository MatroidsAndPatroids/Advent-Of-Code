import utility # my own utility.pl file
import math

# Find all possible N-sums in expenseReport list, that adds up to the value of summa
def findSumsTo(summa, expenseReport):
    # Use an ordered version of the expense list
    orderedReport = list(map(int, expenseReport))
    orderedReport.sort()
    
    # Collect sums found as product_of_values -> [list of elements] dictionary
    sumsFound = {}
   
    # Maintain partial sums as partial_sum -> [list of current elements] dictionary
    partialSums = {}
    for expense in orderedReport:
        if expense > summa:
            # no need to store values that are already too large
            break
        partialSums[expense] = [expense] # partial sum of one element
        
    # Search for the sums
    while partialSums: # expandable partial sum exists
        newPartialSums = {}
        for partialSum, expenses in partialSums.items():
            # each partial sum is ordered
            largestValue = expenses[-1]
            # Bug: will add value multiple times for small numbers that are duplicates
            indexOfLargest = orderedReport.index(largestValue)
            
            # only need to check values that are higher than the largest
            for expense in orderedReport[indexOfLargest + 1:]:
                increasedSum = partialSum + expense 
                if increasedSum < summa:
                    # expand the partial sum with a larger value
                    newPartialSums[increasedSum] = expenses + [expense]
                elif increasedSum == summa:
                    # found a new sum
                    newSum = expenses + [expense]
                    sumsFound[math.prod(newSum)] = newSum
                    # now we only care about sums of size 2
                    if len(newSum) == 2:
                        return True
                else:
                    # we went over the sum, only larger numbers are left afterwards
                    break
            
            # number of values in the partial sums are increased by one
            partialSums = newPartialSums
    
    return False      
    return sumsFound

# Find the first invalid number.
# A number is only valid, if it is the sum of two numbers in its preamble.
def findFirstInvalidNumber(preamble, instructions):
    numbers = list(map(int, instructions))
    
    for index in range(preamble + 1, len(numbers)):
        if not findSumsTo(numbers[index], numbers[index - preamble - 1:index]):
            print(f'{numbers[index] = } {numbers[index - preamble - 1:index] = }')
            return numbers[index]

# Find the encryption weakness.
# The smallest and largest number in a countiguous range,
# where the numbers in this range add up to the previously found invalid number.
def findEncryptionWeakness(preamble, instructions):
    doesNot = findFirstInvalidNumber(preamble, instructions)
    numbers = list(map(int, instructions))
    
    for N in range(2, len(numbers)):
        for i in range(N, len(numbers)):
            if (sum(numbers[i - N + 1:i + 1]) == doesNot):
                print(f'{doesNot = } {numbers[i - N + 1:i + 1] = }')
                maxi = max(numbers[i - N + 1:i + 1])
                mini = min(numbers[i - N + 1:i + 1])
                return mini + maxi
    
    return 0

# Check test cases
smallExample = [
    '35',
    '20',
    '15',
    '25',
    '47',
    '40',
    '62',
    '55',
    '65',
    '95',
    '102',
    '117',
    '150',
    '182',
    '127',
    '219',
    '299',
    '277',
    '309',
    '576']
assert findFirstInvalidNumber(5, smallExample) == 127
assert findEncryptionWeakness(5, smallExample) == 62

# Display info message
print("Give a list of numbers:\n")
instructions = utility.readInputList()

# Display results
print(f'{findFirstInvalidNumber(25, instructions) = }')
print(f'{findEncryptionWeakness(25, instructions) = }')