import utility # my own utility.pl file
import re # split

def decimalToBinary(num): 
    binary = []
    if num > 1: 
        binary += decimalToBinary(num // 2)
    return binary + [str(num % 2)]

def maskToDecimal(mask):
    value = 0
    for i in range(len(mask)):
        value *= 2
        if mask[i] == '1':
            value += 1
        #print(i, mask[i], value)
        
    #print(value, mask)
    return value

def merge(mask, num):
    merged = mask.copy()
    for i in range(len(num)):
        #print(i, len(num), num)
        if merged[len(merged) - i - 1] == 'X':
            merged[len(merged) - i - 1] = num[len(num) - i - 1]
    return merged

def mergeAddress(mask, num):
    merged = num.copy()
    for i in range(len(num)):
        #print(i, len(num), num)
        maskVal = mask[len(mask) - i - 1] 
        if maskVal == '1' or maskVal == 'X':
            merged[len(merged) - i - 1] = maskVal
    return merged

def recur(merged, mlist):
    changed = False
    for i in range(len(merged)):
        if merged[i] == 'X':
            changed = True
            m1 = merged.copy()
            m1[i] = '0'
            recur(m1, mlist)
            m2 = merged.copy()
            m2[i] = '1'
            recur(m2, mlist)
            break
    if not changed:
        mlist += [merged]

def getAddresses(mask, mem):
    addresses = []
    memBits = decimalToBinary(mem)
    # Could not solve under 2.5 hours because I forgot padding here!!! Fuck me :P 
    memBits = ['0'] * 36 + memBits
    memBits = memBits[-36:]
    merged = mergeAddress(mask, memBits)
    recur(merged, addresses)

    #print('getAddresses', merged, mask)
    #print(addresses)
    return addresses

# Simulates the instructions
def emulatePortInitialization(instructions, part2 = False):
    memory = {}
    mask = []

    for ins in instructions:
        #print(ins)
        tokens = ins.split(' = ')
        
        op = tokens[0]
        val = tokens[1]
        
        if op == 'mask':
            mask = list(val)
            #print('newmask', ''.join(mask))
        else:
            tokens = re.split('\[|\]', op)
            mem = int(tokens[1])
            
            if part2:
                addresses = getAddresses(mask, mem)
                valueToWrite = int(val)
                #print(mem, len(addresses), valueToWrite)
                #print(''.join(mask), len(addresses), mem, valueToWrite)
                #print(''.join(decimalToBinary(mem)).rjust(36), mem)
                for address in addresses:
                    a = maskToDecimal(address)
                    memory[a] = valueToWrite
                    #print(''.join(address).rjust(36), a, valueToWrite)
            else:
                binary = decimalToBinary(int(val))
                valueToWrite = maskToDecimal(merge(mask, binary))
                memory[mem] = valueToWrite
                #print(val, binary, memory[mem])
    
    #print(memory)
    ret = sum(memory.values())
    #print(ret)
    return ret

'''
def writeMemory(memory, mask, mem, value):
    index = mask.find('X')
    if index < 0:
        #memory[mem] = value
        return
    
    writeMemory(memory, mask, mem, value)

# Simulates the instructions
def memoryAddressDecoder(instructions, part2 = False):
    memory = {}
    mask = ''
    s = 0
    
    for ins in instructions:
        #print(ins)
        tokens = ins.split(' = ')
        
        op = tokens[0]
        value = tokens[1]
        
        if op == 'mask':
            mask = value
            #print('newmask', ''.join(mask))
        else:
            tokens = re.split('\[|\]', op)
            mem = int(tokens[1])
            writeMemory(mask, mem, value)
            
            if part2:
                addresses = getAddresses(mask, mem)
                valueToWrite = int(value)
                #print(mem, len(addresses), valueToWrite)
                #print(''.join(mask), len(addresses), mem, valueToWrite)
                #print(''.join(decimalToBinary(mem)).rjust(36), mem)
                for address in addresses:
                    a = maskToDecimal(address)
                    memory[a] = valueToWrite
                    s += valueToWrite
                    print(''.join(address).rjust(36), a, valueToWrite)
            else:
                binary = decimalToBinary(int(value))
                valueToWrite = maskToDecimal(merge(mask, binary))
                memory[mem] = valueToWrite
                print(value, binary, memory[mem])
    
    #print(memory)
    ret = sum(memory.values())

    print(s)
    
    print(ret)
    return ret      
'''
# Check test cases
smallExample = """
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
""".strip().split('\n')
smallExample2 = """
mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
""".strip().split('\n')
first15Lines = """
mask = 11100XX0000X1101X1010100X1010001XX0X
mem[24196] = 465592
mem[17683] = 909049
mem[28999] = 20912603
mem[22864] = 7675
mem[55357] = 6401
mem[47006] = 1087112
mask = 111X000100XX1X01X1X10X01X11101100010
mem[22535] = 42768
mem[3804] = 1432484
mem[5475] = 5972
mem[24585] = 484096364
mem[56009] = 206637948
mem[30917] = 630
mem[28325] = 1467510
""".strip().split('\n')
assert emulatePortInitialization(smallExample) == 165
#assert emulatePortInitialization(smallExample, part2 = True) == 404
assert emulatePortInitialization(smallExample2, part2 = True) == 208
#assert emulatePortInitialization(smallExample + smallExample2, part2 = True) == 208 + 404
#assert emulatePortInitialization(smallExample2 + smallExample, part2 = True) == 208 + 404
assert emulatePortInitialization(first15Lines, part2 = True) == 183570298368

# Display info message
print("Give the instructions for the Port Computer System Initialization Program:\n")
instructions = utility.readInputList()

# Display results
print(f'{emulatePortInitialization(instructions) = }')
print(f'{emulatePortInitialization(instructions, part2 = True) = }')