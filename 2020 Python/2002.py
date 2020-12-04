import utility # my own utility.pl file
import re # split

def isValid(line):
    tokens = re.split('-|: | ', line)
    minCount = int(tokens[0]) 
    maxCount = int(tokens[1]) 
    letter = tokens[2]
    password = tokens[3] 
    occurence = password.count(letter)
    return 1 if minCount <= occurence <= maxCount else 0
    
def isValid2(line):
    tokens = re.split('-|: | ', line)
    minCount = int(tokens[0]) 
    maxCount = int(tokens[1]) 
    letter = tokens[2]
    password = tokens[3] 
    occurence = password.count(letter)
    return 1 if ((password[minCount - 1] == letter) != (password[maxCount - 1] == letter)) else 0

def sumValidPasswords(func, passwordList):
    return sum(list(map(func, passwordList)))
    
smallExample = [
    '1-3 a: abcde',
    '1-3 b: cdefg',
    '2-9 c: ccccccccc']

assert sumValidPasswords(isValid, smallExample) == 2
assert sumValidPasswords(isValid2, smallExample) == 1

# Display info message
print("Rule - password list:\n")
passwordList = utility.readInputList()

# Display results
print(f'{sumValidPasswords(isValid, passwordList) = }')
print(f'{sumValidPasswords(isValid2, passwordList) = }')