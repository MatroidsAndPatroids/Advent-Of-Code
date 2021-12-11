import utility # my own utility.pl file (readInputList, SimpleTimer)
import re # split
import pandas as pd # DataFrame

# Argument positions for parsing
positionInToken = {
    'swap position'     : (2, 5, True, True),
    'swap letter'       : (2, 5, False, False),
    'rotate left'       : (2, None, True, None),
    'rotate right'      : (2, None, True, None),
    'rotate based'      : (6, None, False, None),
    'reverse positions' : (2, 4, True, True),
    'move position'     : (2, 5, True, True)
    }

# Swap positions in a string
def swapPositions(string, pos1, pos2):
    charList = list(string)
    charList[pos1], charList[pos2] = charList[pos2], charList[pos1]
    return ''.join(charList)

# Move character at pos1 to pos2
def movePosition(string, pos1, pos2):
    letter = string[pos1]
    charList = list(string)
    del charList[pos1]
    charList.insert(pos2, letter)
    return ''.join(charList)

reverse = lambda string : string[::-1]
rotateBased = lambda pwd, c : (int(4<=pwd.find(c)) + 1 + pwd.find(c)) % len(pwd)

# Name - operation table
jumpTable = {
    'swap position'     : lambda pwd, x, y : swapPositions(pwd, x, y),
    'swap letter'       : lambda pwd, a, b : pwd.replace(a, '-').replace(b, a).replace('-', b),
    'rotate left'       : lambda pwd, x, _ : pwd[x:] + pwd[:x],
    'rotate right'      : lambda pwd, x, _ : jumpTable['rotate left'](pwd, -x, _),
    'rotate based'      : lambda pwd, c, _ : jumpTable['rotate right'](pwd, rotateBased(pwd, c), _),
    'reverse positions' : lambda pwd, x, y : pwd[:x] + reverse(pwd[x:y+1]) + pwd[y+1:],
    'move position'     : lambda pwd, x, y : movePosition(pwd, x, y)
    }

# Try rotating for i=0..N (N=len(pwd)) and test if it reverses the 'rotate based' operation
# Note: this does not work if N is odd, due to ambiguity
def reversedRotateBased(pwd, c):
    for i in range(len(pwd)):
        reversedRotated = reversedJumpTable['rotate left'](pwd, i, None)
        if jumpTable['rotate based'](reversedRotated, c, None) == pwd:
            return reversedRotated
    assert(False)
    return None

# Reverse operations
reversedJumpTable = jumpTable.copy()
reversedJumpTable['rotate left'] = jumpTable['rotate right']
reversedJumpTable['rotate right'] = jumpTable['rotate left']
reversedJumpTable['rotate based'] = lambda pwd, c, _ : reversedRotateBased(pwd, c)
reversedJumpTable['move position'] = lambda pwd, x, y : jumpTable['move position'](pwd, y, x)

# Parse input line and perform the operation
def perform(password, operation, part2):
    tokens = operation.split(' ')
    operator = ' '.join(tokens[0:2])

    xPos, yPos, xInt, yInt = positionInToken[operator]
    x = int(tokens[xPos]) if xInt else tokens[xPos]
    y = int(tokens[yPos]) if yInt else tokens[yPos] if yPos else None

    table = reversedJumpTable if part2 else jumpTable
    password = table[operator](password, x, y)
        
    #print(password, operator, x, y)
    return password

# Perform operations line by line (for part 2 in reversed order)
def parseData():
    terabyte = lambda string : int(string.strip('T'))
    percentage = lambda string : int(string.strip('%'))
    converters = {'Size' : terabyte, 'Used' : terabyte, 'Avail' : terabyte, 'Use%' : percentage}
    pattern = '^/dev/grid/node-x|-y'
    
    df = pd.read_csv('1622.txt', header=1, delim_whitespace=True, converters=converters)
    getI = lambda row, i : int(re.split(pattern, row['Filesystem'])[i])
    df['x'] = df.apply(lambda row : getI(row, 1), axis=1)
    df['y'] = df.apply(lambda row : getI(row, 2), axis=1)
    print(df)

    viable = lambda df, row : len(df[0 < row['Used'] <= df.Avail]) - int(0 < row['Used'] <= row['Avail'])
    #viable = lambda df, row : print(len(df[0 < row['Used'] <= df.Avail]))
    df['viable'] = df.apply(lambda row : viable(df, row), axis=1)#WTFWTFWTFWTFWTFWTFWTFWTFXXXXXXXXXXXFFFFFFFFQQQQQQ
    print(df['viable'].sum())
    return df

#def viablePairs(df):
    

# Display info message
print("\nList of operations:")
diskUsageData = parseData()
print(diskUsageData)

# Display results
#print(f'{scramble("abcdefgh", operations) = }')
#assert scramble('gbhafcde', operations, part2=True) == 'abcdefgh'
#print(f'{scramble("fbgdceah", operations, part2=True) = }')

