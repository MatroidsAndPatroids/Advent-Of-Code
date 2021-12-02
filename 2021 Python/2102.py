import utility # my own utility.pl file

def posi(data):
    h = 0
    d = 0
    aim = 0
    
    for l in data:
        a = l.split()
        num = int(a[1])
        if a[0] == 'forward':
            h += num
            d += aim * num
        elif a[0] == 'down':
            #d += num
            aim += num
        elif a[0] == 'up':
            #d -= num
            aim -= num
    print(h, d)
    return h * d
    

smallExample = '''
forward 5
down 5
forward 8
up 3
down 8
forward 2'''.strip().split('\n')

assert(posi(smallExample) == 900)


# Display info message
print("Give a list of course plan instructions:\n");
instructionList = utility.readInputList()

# Display results
print (f'{posi(instructionList) = }')
