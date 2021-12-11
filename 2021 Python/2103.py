import utility # my own utility.py file
import numpy # array

def listToBinary(binaryList):
    text = ''.join(map(str, binaryList))
    return int(text, 2)

assert(listToBinary([1,0,1]) == 5)

def binaryDiagnostic(diagnosticReport, part2=False):
    # Parse
    diagnosticReport = numpy.array([list(map(int, list(line))) for line in diagnosticReport])
    columns = diagnosticReport.shape[1]
    leastCommonTable = diagnosticReport.copy()
    mostCommonTable = diagnosticReport.copy()
    leastCommon = []
    mostCommon = []
    
    # Calculate
    for i in range(columns):
        currentLeastCommon = int(sum(leastCommonTable[:, i]) < leastCommonTable.shape[0] / 2)
        if leastCommonTable.shape[0] == 1:
            currentLeastCommon = leastCommonTable[0][i]
        currentMostCommon = int(sum(mostCommonTable[:, i]) >= mostCommonTable.shape[0] / 2)
        leastCommon.append(currentLeastCommon)
        mostCommon.append(currentMostCommon)

        if part2 and len(leastCommonTable) > 1:
            leastCommonTable = leastCommonTable[leastCommonTable[:, i] == currentLeastCommon, :]
        if part2 and len(mostCommonTable) > 1:
            mostCommonTable = mostCommonTable[mostCommonTable[:, i] == currentMostCommon, :]

    # Return
    print(leastCommon, mostCommon)
    value = listToBinary(leastCommon) * listToBinary(mostCommon) 
    print(value)
    return value

# Verify test cases
smallExample = '''
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
'''.strip().split('\n')
assert(binaryDiagnostic(smallExample) == 198)
assert(binaryDiagnostic(smallExample, part2=True) == 230)

# Display info message
print("\nGive Binary Diagnostic data:");
diagnosticReport = utility.readInputList()

# Display results
print (f'{binaryDiagnostic(diagnosticReport) = }')
print (f'{binaryDiagnostic(diagnosticReport, part2=True) = }')