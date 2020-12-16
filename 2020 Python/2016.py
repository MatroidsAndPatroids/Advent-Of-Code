import utility # my own utility.pl file

def isValid(validityRanges, value):
    for r in validityRanges:
        if r[1] <= value <= r[2] or r[3] <= value <= r[4]:
            return True
    return False

def possibleField(validityRanges, nearbyTickets, column):
    possibleFields = {}
    for n in nearbyTickets:
        value = n[column]
        for r in validityRanges:
            if r[1] <= value <= r[2] or r[3] <= value <= r[4]:
                current = possibleFields.get(r[0], 0)
                possibleFields[r[0]] = current + 1
                
    possibleFields2 = []
    maximum = max(possibleFields.values())
    for key, value in possibleFields.items():
        if value == maximum:
            possibleFields2 += [key]
        
    #print(column, possibleFields2)
    return possibleFields2

# Simulates the instructions
def ticketTranslation(instructions, part2 = False):
    sol = 0
    validityRanges = []
    yourTicket = []
    nearbyTickets = []
    
    # Parse input
    state = 0
    for ins in instructions:
        if not ins:
            continue
        if ins == 'your ticket:':
            state = 1
            continue
        if ins == 'nearby tickets:':
            state = 2
            continue
        
        if state == 0:
            tokens = ins.split(':')
            name = tokens[0]
            tokens = tokens[1].split()
            lb1, ub1 = tokens[0].split('-')
            lb2, ub2 = tokens[2].split('-')
            validityRanges += [[name] + list(map(int, [lb1, ub1, lb2, ub2]))]
        elif state == 1:
            yourTicket = list(map(int, ins.split(',')))
        elif state == 2:
            nearbyTicket = list(map(int, ins.split(',')))
            nearbyTickets += [nearbyTicket]
    
    # Remove all invalid tickets and sum all invalid values
    invalids = 0
    validTickets = []
    for ticket in nearbyTickets:
        valid = True
        for value in ticket:
            if not isValid(validityRanges, value):
                invalids += value
                valid = False
        if not valid:
            validTickets += ticket
    
    # Find all candidate fields for each column
    possibles = []
    for column in range(len(yourTicket)):
        possibles += [possibleField(validityRanges, nearbyTickets, column)]
    
    # Finalize unique candidate fields by removing them from all other columns
    # Iterate until there are unique fields left  
    modified = True
    while modified:
        modified = False
        for p in possibles:
            if len(p) == 1:
                modified = True
                key = p[0]
                p += ['Done']
                for q in possibles:
                    if q[-1] != 'Done' and key in q:
                        q.remove(key)
    
    # Calculate the product of 'departure' fields on your ticket
    product = 1
    for i in range(len(yourTicket)):
        if 'departure' in possibles[i][0]:
            product *= yourTicket[i]
    
    #print(validityRanges)
    #print(yourTicket)
    #print(nearbyTickets)
    #print(possibles)

    return product if part2 else invalids

# Check test cases
smallExample = """
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
""".strip().split('\n')
assert ticketTranslation(smallExample) == 71

# Display info message
print("Give a list of instructions:\n")
instructions = utility.readInputList()

# Display results
print(f'{ticketTranslation(instructions) = }')
print(f'{ticketTranslation(instructions, part2 = True) = }')