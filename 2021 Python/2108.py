import utility # my own utility.py file

# Sum of output values of each seven-segment display
def outputValues(displayEntries, part2=False):
    digidict = {
        2 : 1,
        3 : 7,
        4 : 4,
        7 : 8
    }
    digit1478 = 0
    totalValue = 0
    
    for line in displayEntries:
        # Parse, turn numberToCharset into frozensets of characters
        words, digits = line.split(' | ')
        words = list(map(frozenset, map(list, words.split())))
        digits = list(map(frozenset, map(list, digits.split())))
        
        # Find segments of 1, 4, 7 and 8
        numberToCharset = {}
        for w in words:
            if len(w) in digidict.keys():
                number = digidict[len(w)]
                numberToCharset[number] = w 
        
        # Find segments of 0, 2, 3, 5, 6, and 9
        for w in words:
            if len(w) not in digidict.keys():
                number = -1
                one = len(numberToCharset[1].intersection(w))
                four = len(numberToCharset[4].intersection(w))
                
                if len(w) == 5:
                    if one == 2:
                        number = 3
                    elif four == 3:
                        number = 5
                    elif one == 1 and four == 2:
                        number = 2
                elif len(w) == 6:
                    if one == 1:
                        number = 6
                    elif four == 4:
                        number = 9
                    elif one == 2 and four == 3:
                        number = 0

                assert(number not in numberToCharset.keys())
                numberToCharset[number] = w 
        
        charsetToNumber = {}
        for number, charset in numberToCharset.items():
            charsetToNumber[charset] = number

        outputValue = 0
        for d in digits:
            if len(d) in digidict.keys():
                digit1478 += 1
            number = charsetToNumber[d]
            outputValue = 10 * outputValue + number
        totalValue += outputValue

    # Return
    value = totalValue if part2 else digit1478
    print(value)
    return value

# Verify test cases
smallExample = '''
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
'''.strip().split('\n')
assert outputValues(smallExample) == 26
assert outputValues(smallExample, part2=True) == 61229

# Display info message
print("\nGive a list of display entries:")
displayEntries = utility.readInputList()

# Display results
print (f"{outputValues(displayEntries) = }")
print (f"{outputValues(displayEntries, part2=True) = }")