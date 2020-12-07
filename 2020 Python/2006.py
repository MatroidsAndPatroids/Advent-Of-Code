import utility # my own utility.pl file

# Adds up the number of questions answered yes for each group.
# Part 1: by at least one person in the group
# Part 2: by all people in the group  
def sumOfQuestionsAnsweredYes(yesAnswers, part2 = False):
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
                groupYesAnswers = lineYesAnswers.intersection(groupYesAnswers)
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
assert sumOfQuestionsAnsweredYes(smallExample) == 11
assert sumOfQuestionsAnsweredYes(smallExample, part2 = True) == 6

# Display info message
print("Give list of yes answers for each person in each group:\n")
yesAnswers = utility.readInputList()

# Display results
print(f'{sumOfQuestionsAnsweredYes(yesAnswers) = }')
print(f'{sumOfQuestionsAnsweredYes(yesAnswers, part2 = True) = }')