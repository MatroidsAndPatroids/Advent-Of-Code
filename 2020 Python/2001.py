import utility # my own utility.pl file
import math # prod

# Find all possible N-sums in expenseReport list, that adds up to the value of summa
def findSumsTo(expenseReport, summa):
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
                else:
                    # we went over the sum, only larger numbers are left afterwards
                    break
            
            # number of values in the partial sums are increased by one
            partialSums = newPartialSums
            
    return sumsFound

# Check test cases
smallExample = [
    1721,
    979,
    366,
    299,
    675,
    1456]
smallSums = findSumsTo(smallExample, 2020)
assert list(smallSums.keys())[0] == 514579 # first key in dictionary
assert list(smallSums.keys())[1] == 241861950 # second key

# Display info message
print("Give expense report:\n")
expenseReport = utility.readInputList()

# Display results
expenseSums = findSumsTo(expenseReport, 2020)
print(expenseSums)