import utility # my own utility.pl file

# Find matching parentheses for the ')' on the right side of the expression
def findLeft(expression):
    diff = 0
    for i in range(len(expression) - 1, -1, -1):
        # Note: the last element of expression is expected to be ')'
        if expression[i] == ')':
            diff += 1
        elif expression[i] == '(':
            diff -=1
        
        if diff == 0:
            return i
    return -1

# Translate the operator character to a function
jumpTable = {
    '+': lambda x, y: x + y,
    '*': lambda x, y: x * y}

# Caluclates the value of the expression
def result(expression, part2 = False):
    #print(expression)
    
    right = expression.rfind(')')
    while 0 < right:
        # Reduce the expression until there are no parentheses left
        left = findLeft(expression[:right + 1])
        expression = expression[:left] + str(result(expression[left + 1:right], part2)) + expression[right + 1:]
        #print(expression)
        right = expression.rfind(')')

    lastPlus = expression.rfind('+')
    lastStar = expression.rfind('*')
    opIndex = max(lastPlus, lastStar)
    opIndex = lastStar if part2 and 0 < lastStar else opIndex
    if opIndex < 0:
        return int(expression)
    
    leftValue = result(expression[:opIndex - 1], part2)
    rightValue = result(expression[opIndex + 2:], part2)
    operator = expression[opIndex]
    
    return jumpTable[operator](leftValue, rightValue)

# Sum of all the expressions
def sumOfExpressionResults(expression, part2 = False):
    resultFunction = lambda line: result(line, part2)
    return sum(map(resultFunction, expression))

# Check test cases
smallExample1 = '1 + 2 * 3 + 4 * 5 + 6'.split('\n')
smallExample2 = '1 + (2 * 3) + (4 * (5 + 6))'.split('\n')
smallExample3 = '2 * 3 + (4 * 5)'.split('\n')
smallExample4 = '5 + (8 * 3 + 9 + 3 * 4 * 3)'.split('\n')
smallExample5 = '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'.split('\n')
smallExample6 = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'.split('\n')

assert sumOfExpressionResults(smallExample1) == 71
assert sumOfExpressionResults(smallExample2) == 51
assert sumOfExpressionResults(smallExample3) == 26
assert sumOfExpressionResults(smallExample4) == 437
assert sumOfExpressionResults(smallExample5) == 12240
assert sumOfExpressionResults(smallExample6) == 13632

assert sumOfExpressionResults(smallExample1, part2 = True) == 231
assert sumOfExpressionResults(smallExample2, part2 = True) == 51
assert sumOfExpressionResults(smallExample3, part2 = True) == 46
assert sumOfExpressionResults(smallExample4, part2 = True) == 1445
assert sumOfExpressionResults(smallExample5, part2 = True) == 669060
assert sumOfExpressionResults(smallExample6, part2 = True) == 23340

# Display info message
print("Give a list of expressions:\n")
expression = utility.readInputList()

# Display results
print(f'{sumOfExpressionResults(expression) = }')
print(f'{sumOfExpressionResults(expression, part2 = True) = }')