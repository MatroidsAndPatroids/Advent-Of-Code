import utility # my own utility.pl file
import re # match

def countValidPassports(passports):
    numValid = 0
    currentPassport = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for line in passports:
        tokens = line.split()
        if len(tokens) == 0:
            if len(currentPassport) == 0:
                numValid += 1
            currentPassport = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
            
        for field in tokens:
            key, value = field.split(':')
            if key in currentPassport:
                currentPassport.remove(key)
                
        print(f'{line = }\t{currentPassport = }')
    return numValid

def isValid(key, value):
    if key == 'byr':
        return 1920 <= int(value) <= 2002
    elif key == 'iyr':
        return 2010 <= int(value) <= 2020
    elif key == 'eyr':
        return 2020 <= int(value) <= 2030
    elif key == 'hgt':
        if value[-2:] == 'cm':
            return 150 <= int(value[:-2]) <= 193
        elif value[-2:] == 'in':
            return 59 <= int(value[:-2]) <= 76
        return False
    elif key == 'hcl':
        return re.match('^#[a-f0-9]+', value) != None
    elif key == 'ecl':
        return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif key == 'pid':
        return len(value) == 9 and re.match('^[0-9]+', value) != None
    elif key == 'cid':
        return True
    return False

def countValidPassports2(passports):
    numValid = 0
    currentPassport = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for line in passports:
        tokens = line.split()
        if len(tokens) == 0:
            if len(currentPassport) == 0:
                numValid += 1
            currentPassport = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
            
        for field in tokens:
            key, value = field.split(':')
            if not isValid(key, value):
                print(f'{key = }, {value = }, {isValid(key, value) = }')
            if key in currentPassport and isValid(key, value):
                currentPassport.remove(key)
                
        if len(currentPassport) == 0:
            print(f'{line = }\t{currentPassport = }')
    print(f'{numValid = }')
    return numValid
    
smallExample = [
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
    'iyr:2011 ecl:brn hgt:59in',
    '']

small2 = [
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
    'pid:3556412378 byr:2007',
    '']

small3 = [
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
    'iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719',
    '']

#assert countValidPassports(smallExample) == 2
#assert countValidPassports2(small2) == 0
assert countValidPassports2(small3) == 4

# Display info message
print("Give monorail instruction list:\n")
passports = utility.readInputList()
passports += ['']
print(passports)
print('STOP')

# Display results
print(f'{countValidPassports(passports) = }')
print(f'{countValidPassports2(passports) = }')