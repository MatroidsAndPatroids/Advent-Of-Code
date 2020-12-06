import utility # my own utility.pl file
import re # match

# Counts the number of valid yesAnswers in the list.
def sumOfYesQuestions(yesAnswers, part2 = False):
    yesAnswers += [''] # add temporary extra line break
    
    groupYesAnswers = set() # start a new group
    sumOfYesAnswers = 0
    newGroup = True
    
    for line in yesAnswers: # each line contains the yes answers for one person
        # eg. line = 'abc'
        if not line: # empty line, finish last group
            sumOfYesAnswers += len(groupYesAnswers)
            groupYesAnswers = set() # start a new group
            newGroup = True
        
        else: # line not empty
            lineYesAnswers = set([question for question in line])
            
            if part2 and not newGroup:
                groupYesAnswers = lineYesAnswers.difference(groupYesAnswers)
            else:
                groupYesAnswers = lineYesAnswers.union(groupYesAnswers)
                newGroup = False
                
    del yesAnswers[-1] # remove temporary extra line break
    return sumOfYesAnswers

# Check test cases
smallExample = [
    'abc',
    '',
    'a',
    'b',
    'c',
    '',
    'ab',
    'ac',
    '',
    'a',
    'a',
    'a',
    'a',
    '',
    'b']
assert sumOfYesQuestions(smallExample) == 11
assert sumOfYesQuestions(smallExample, part2 = True) == 6

# Display info message
print("Give list of yes answers for each person in each group:\n")
yesAnswers = utility.readInputList()

# Display results
print(f'{sumOfYesQuestions(yesAnswers) = }')
print(f'{sumOfYesQuestions(yesAnswers, part2 = True) = }')