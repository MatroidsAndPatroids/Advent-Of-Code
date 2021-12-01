import utility # my own utility.pl file

small ="""
199
200
208
210
200
207
240
269
260
263""".strip().split('\n')

def increase(data):
    count = 0
    for i in range(0, len(data)-1):
        if int(data[i+1]) - int(data[i]) > 0:
            count += 1
    return count
def increase2(data):
    count = 0
    for i in range(0, len(data)-3):
        if int(data[i+3]) - int(data[i]) > 0:
            count += 1
    return count

print(increase(small))
assert(increase(small) == 7)

print(increase2(small))
assert(increase2(small) == 5)

# Display info message
print("Give a list of instructions:\n");
instructionList = utility.readInputList()

# Display results
print (f'{increase(instructionList) = }')
print (f'{increase2(instructionList) = }')