import utility # my own utility.pl file (readInputList, SimpleTimer)

# One step of a dragon curve algorithm
def dragonCurveStep(state):
    reverse = state[::-1]
    reverse = reverse.replace('0', 'x')
    reverse = reverse.replace('1', '0')
    reverse = reverse.replace('x', '1')
    return str(state) + '0' + reverse

assert dragonCurveStep('1') == '100'
assert dragonCurveStep('0') == '001'
assert dragonCurveStep('11111') == '11111000000'
assert dragonCurveStep('111100001010') == '1111000010100101011110000'

def reduceSize(data):
    even = data[0::2]
    odd = data[1::2]
    return ''.join([str(int(even[i] == odd[i])) for i in range(len(even))])

assert reduceSize('110010110100') == '110101'
assert reduceSize('110101') == '100'

# Generate a checksum for generated data that is long enough to fill the entire disk
def checksum(initialState, diskSize):
    T = utility.SimpleTimer()
    
    data = initialState
    while len(data) < diskSize:
        data = dragonCurveStep(data)
        
    checksum = data[:diskSize]
    
    while len(checksum) % 2 == 0:
        checksum = reduceSize(checksum)
    return checksum
    
assert checksum('110010110100', diskSize=12) == '100'
assert checksum('10000', diskSize=20) == '01100'

# Display info message
print("\nGive initial state:")
initialState = utility.readInputList()[0]

# Display results
print(f'{checksum(initialState, diskSize=272) = }')
print(f'{checksum(initialState, diskSize=35651584) = }')
