import utility # my own utility.pl file

# First part of the message will be validated after the given rule.
# Return possible indices from which we can continue with the rest of the rules.
def getIndices(message, rulebook, ruleText, index = 0, depth = 0):
    possibleIndices = set()
    debugMsg = message[:index] + '>' + message[index:]
    debugMsg = f'{str(index).rjust(2)}/{len(message)} {debugMsg} {"|" * depth}{ruleText}'
#     print(debugMsg)
    
    if index not in range(len(message)):
        # either -1 or past the message
        possibleIndices = set()
    elif '"' in ruleText:
        # '"a"' format
        character = ruleText[1]
        possibleIndices = {index + 1} if message[index] == character else set()
    elif ' | ' in ruleText:
        # '9 14 | 10 1' format
        sides = ruleText.split(' | ')
        possibleIndices = set()
        
        for side in sides:
            # Try each side independently, collect next indices from both of them
            newIndices = getIndices(message, rulebook, side, index, depth + 1)
            possibleIndices = possibleIndices.union(newIndices)
    else:
        # '42 31' format
        #rules = list(map(int, ruleText.split()))
        rules = ruleText.split()
        possibleIndices = {index}
        
        for ruleNum in rules:
            if not possibleIndices:
                break
            # Try every rule in the list in order, collect next indices after the last one
            newRule = rulebook[ruleNum]
            newIndices = set()
            
            for i in possibleIndices:
                # Try each possible index with the current rule, collect next indices
                additionalIndices = getIndices(message, rulebook, newRule, i, depth + 1)
                newIndices = newIndices.union(additionalIndices)
                
            possibleIndices = newIndices
            
#     print(debugMsg, 'END:', possibleIndices)
    return possibleIndices

# A message is valid if it obeys rule 0 and all its sub-rules in the rulebook.
def isValid(message, rulebook, ruleNumber):
    i = getIndices(message, rulebook, rulebook[str(ruleNumber)])
#     print(message, len(message), 'in', i, '=', len(message) in i)
    return len(message) in i

# Count the number of valid messages.
# The input consists of a validation rule set and a list of messages.
def countValid(instructions, part2 = False):
    rulebook = {}
    receivedMessages = []
    
    for line in instructions:
        if not line:
            continue
        elif ': ' in line:
            # '1: 2 3 | 3 2' format
            ruleNumber, ruleText = line.split(': ')
            rulebook[ruleNumber] = ruleText
        else:
            # 'bababa' format
            receivedMessages += [line]
    
    if part2:
        rulebook['8'] = '42 | 42 8'
        rulebook['11'] = '42 31 | 42 11 31'
    
#     print(rulebook)
#     print(receivedMessages)
    func = lambda message: int(isValid(message, rulebook, 0))
    count = sum(map(func, receivedMessages))
    print(count)
    return count

# Check test cases
smallExample = """
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb
""".strip().split('\n')
largeExample = """
42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba
""".strip().split('\n')
assert countValid(smallExample) == 2
assert countValid(largeExample) == 3
assert countValid(smallExample, part2 = True) == 2
assert countValid(largeExample, part2 = True) == 12

# Display info message
print("Give a set of validation rules and a list of messages:\n")
instructions = utility.readInputList()

# Display results
print(f'{countValid(instructions) = }')
print(f'{countValid(instructions, part2 = True) = }')