import utility # my own utility.py file


def syntaxErrorScore(line):
    stack = []
    for c in line:
        if c in syntaxErrorScore.closer.keys(): # opener
            stack.append(c)
        elif c in syntaxErrorScore.closer.values(): # closer
            if not stack or c != syntaxErrorScore.closer[stack.pop()]:
                return stack, syntaxErrorScore.score[c]
        else: # unknown character
            assert(False)
    return stack, 0

syntaxErrorScore.closer = {
    '(' : ')',
    '[' : ']',
    '{' : '}',
    '<' : '>' 
    }
syntaxErrorScore.score = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137 
    }

def autoCompleteScore(stack):
    stack.reverse()
    charToPoint = lambda c : str(autoCompleteScore.point[c])
    pointsInBase5 = int(''.join(map(charToPoint, stack)), 5)
    return pointsInBase5

autoCompleteScore.point = {
    '(' : 1,
    '[' : 2,
    '{' : 3,
    '<' : 4 
    }

# Find incorrect and incomplete lines and calculate their scores
def syntaxScoring(syntaxLines, part2=False):
    # Parse
    totalSyntaxErrorScore = 0
    autocompleteScores = []
    for line in syntaxLines:
        # Part 1 - find corrupted lines
        stack, syntaxScore = syntaxErrorScore(line)
        corrupted = syntaxScore > 0
        totalSyntaxErrorScore += syntaxScore

        # Part 2 - calculate score for incomplete lines
        if not corrupted and stack:
            autocompleteScores.append(autoCompleteScore(stack))

    # Return
    autocompleteScores.sort()
    autocompleteWinner = autocompleteScores[len(autocompleteScores)//2] # median
    value = autocompleteWinner if part2 else totalSyntaxErrorScore
    print(value)
    return value

# Verify test cases
smallExample = '''
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
'''.strip().split('\n')
assert syntaxScoring(smallExample) == 26397
assert syntaxScoring(smallExample, part2=True) == 288957

# Display info message
print("\nGive syntax lines:")
syntaxLines = utility.readInputList()

# Display results
print (f"{syntaxScoring(syntaxLines) = }")
print (f"{syntaxScoring(syntaxLines, part2=True) = }")