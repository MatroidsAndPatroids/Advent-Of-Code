import utility # my own utility.pl file
import re # split

# Parses input line and checks if a password is valid according to the given rules
# eg. line = '1-3 a: abcde'
# Part1: valid if the lettercount in the password is between the given numbers
# Part2: valid if either letter position contains the given letter, but not both
def isValid(line, part2 = False):
    tokens = re.split('-|: | ', line)
    
    min = int(tokens[0])
    max = int(tokens[1])
    letter = tokens[2]
    password = tokens[3]
    
    if part2:
       return (password[min - 1] == letter) != (password[max - 1] == letter)
    
    return min <= password.count(letter) <= max

# Number of valid passwords in the list  
def sumValidPasswords(passwordList, part2 = False):
    func = lambda line: int(isValid(line, part2) == True)
    return sum(list(map(func, passwordList)))
    
# Check test cases
smallExample = [
    '1-3 a: abcde',
    '1-3 b: cdefg',
    '2-9 c: ccccccccc']
assert sumValidPasswords(smallExample) == 2
assert sumValidPasswords(smallExample, part2 = True) == 1

# Display info message
print("Rule - password list:\n")
passwordList = utility.readInputList()

# Display results
print(f'{sumValidPasswords(passwordList) = }')
print(f'{sumValidPasswords(passwordList, part2 = True) = }')