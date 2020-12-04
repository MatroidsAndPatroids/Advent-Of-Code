import utility # my own utility.pl file
import collections # counter

# Correct the repetition code
def errorCorrect(repetitionCode):
    commons = [collections.Counter(column).most_common() for column in zip(*repetitionCode)]
    return [''.join(c[i][0] for c in commons) for i in (0, -1)] # 0 = most common, -1 = least

smallExample = [
    'eedadn',
    'drvtee',
    'eandsr',
    'raavrd',
    'atevrs',
    'tsrnev',
    'sdttsa',
    'rasrtv',
    'nssdts',
    'ntnada',
    'svetve',
    'tesnvt',
    'vntsnd',
    'vrdear',
    'dvrsen',
    'enarar']
assert errorCorrect(smallExample) == ['easter', 'advent']

# Display info message
print("Send a message using repetition coding:\n")
repetitionCode = utility.readInputList()

# Display results
print (f"{errorCorrect(repetitionCode) = }")