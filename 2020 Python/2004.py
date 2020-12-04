import utility # my own utility.pl file
import re # match

# Jump table for part2: key, value -> isValid (True or False)
# There is no 'cid' in jumpTable, because jumpTable will return True by default
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
# Passports may contain more lines and are separated by empty lines.
# A passport is valid if,
# Part 1: contains all the relevant fields: byr iyr eyr hgt hcl ecl pid
# Part 2: same as Part 1, plus all the relevant fields have the required properties
def countValidPassports(passports, part2 = False):
    passports += [''] # add temporary extra line break
    numValid = 0
    
    defaultPassport = 'byr iyr eyr hgt hcl ecl pid'.split() # no 'cid' here either
    currentPassport = defaultPassport.copy() # start a new passport
    validityCheck = jumpTable if part2 else {}
    
    for line in passports:
        # eg. line = 'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd'
        tokens = line.split()
        
        if not tokens: # empty line
            if not currentPassport: # all relevant keys were included
                numValid += 1
            currentPassport = defaultPassport.copy() # start a new passport
        
        else: # line has fields
            for field in tokens:
                # eg. field = 'hgt:181cm'
                key, value = field.split(':')
                
                # Check if key is relevant and value is valid or has no rule to check
                if (key in currentPassport
                        and (key not in validityCheck or validityCheck[key](value))):
                    currentPassport.remove(key) # remove relevant keys one by one
    
    del passports[-1] # remove temporary exta line break
    return numValid



# Check test cases

twoValidPassports = [
    'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd',
    'byr:1937 iyr:2017 cid:147 hgt:183cm',
    '',
    'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884',
    'hcl:#cfa07d byr:1929',
    '',
    'hcl:#ae17e1 iyr:2013',
    'eyr:2024',
    'ecl:brn pid:760753108 byr:1931',
    'hgt:179cm',
    '',
    'hcl:#cfa07d eyr:2025 pid:166559648',
    'iyr:2011 ecl:brn hgt:59in']

fourInvalidPassports = [
    'eyr:1972 cid:100',
    'hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926',
    '',
    'iyr:2019',
    'hcl:#602927 eyr:1967 hgt:170cm',
    'ecl:grn pid:012533040 byr:1946',
    '',
    'hcl:dab227 iyr:2012',
    'ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277',
    '',
    'hgt:59cm ecl:zzz',
    'eyr:2038 hcl:74454a iyr:2023',
    'pid:3556412378 byr:2007']

fourValidPassports = [
    'pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980',
    'hcl:#623a2f',
    '',
    'eyr:2029 ecl:blu cid:129 byr:1989',
    'iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm',
    '',
    'hcl:#888785',
    'hgt:164cm byr:2001 iyr:2015 cid:88',
    'pid:545766238 ecl:hzl',
    'eyr:2022',
    '',
    'iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719']

assert countValidPassports(twoValidPassports) == 2
assert countValidPassports(fourInvalidPassports, part2 = True) == 0
assert countValidPassports(fourValidPassports, part2 = True) == 4



# Display info message
print("Give passport batch file:\n")
passports = utility.readInputList()

# Display results
print(f'{countValidPassports(passports) = }')
print(f'{countValidPassports(passports, part2 = True) = }')