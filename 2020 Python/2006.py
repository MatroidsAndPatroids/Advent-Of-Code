import utility # my own utility.pl file
import re # match

# Jump table for part2: key, value -> isValid (True or False)
jumpTable = {
    'byr': lambda value: (1920 <= int(value) <= 2002),
    'iyr': lambda value: (2010 <= int(value) <= 2020),
    'eyr': lambda value: (2020 <= int(value) <= 2030),
    'hgt': lambda value: (value[-2:] == 'cm' and 150 <= int(value[:-2]) <= 193
                          or value[-2:] == 'in' and 59 <= int(value[:-2]) <= 76),
    'hcl': lambda value: (re.match('^#[a-f0-9]+', value) != None),
    'ecl': lambda value: (value in 'amb,blu,brn,gry,grn,hzl,oth'),
    'pid': lambda value: (len(value) == 9 and re.match('^[0-9]+', value))}

# Counts the number of valid passports in the list.
def countValidPassports(passports, part2 = False):
    passports += [''] # add temporary extra line break
    numValid = 0
    current = {}
    firstLine = True
    
    for line in passports:
        # eg. line = 'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd'
        tokens = line.split()
        
        if not line: # empty line
            print(current)
            numValid += len(current)
            current = {} # start a new passport
            firstLine = True
        
        else: # line has fields
            if part2:
                if not firstLine:
                    newCurrent = {}
                    for key, value in current.items():
                        if key in line:
                            newCurrent[key] = 0
                    current = newCurrent
                else:
                    for c in line:
                        # eg. field = 'hgt:181cm'
                        current[c] = 0
                    firstLine = False
            else:
                for c in line:
                    # eg. field = 'hgt:181cm'
                    current[c] = 0
    
    return numValid



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
assert countValidPassports(smallExample) == 11
print(countValidPassports(smallExample, part2 = True))
assert countValidPassports(smallExample, part2 = True) == 6



# Display info message
print("Give passport batch file:\n")
passports = utility.readInputList()

# Display results
print(f'{countValidPassports(passports) = }')
print(f'{countValidPassports(passports, part2 = True) = }')