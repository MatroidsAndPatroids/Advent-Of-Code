import utility # my own utility.pl file
import math # prod

def addUpTo(expenseReport, summa):
    #orderedReport = list(sort(map(expenseReport, int)))
    for i in range(len(expenseReport)):
        expense1 = int(expenseReport[i])
        for j in range(len(expenseReport)):
            expense2 = int(expenseReport[j])
            if i != j and expense1 + expense2 == summa:
                return [expense1, expense2]
    return []

def addUpTo3(expenseReport, summa):
    #orderedReport = list(sort(map(expenseReport, int)))
    for i in range(len(expenseReport)):
        expense1 = int(expenseReport[i])
        for j in range(len(expenseReport)):
            expense2 = int(expenseReport[j])
            for k in range(len(expenseReport)):
                expense3 = int(expenseReport[k])
                if i != j and i != k and j != k and expense1 + expense2 + expense3 == summa:
                    return [expense1, expense2, expense3]
    return []
    
smallExample = [
    1721,
    979,
    366,
    299,
    675,
    1456]
assert math.prod(addUpTo(smallExample, 2020)) == 514579
assert math.prod(addUpTo3(smallExample, 2020)) == 241861950

# Display info message
print("Give monorail instruction list:\n")
expenseReport = utility.readInputList()

# Display results
print(f'{math.prod(addUpTo(expenseReport, 2020)) = }')
print(f'{math.prod(addUpTo3(expenseReport, 2020)) = }')