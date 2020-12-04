import utility # my own utility.pl file
import itertools # groupby
import functools # reduce

# Say out loud the given string of digits
def lookAndSay(digits):
	return "".join([f"{len(list(group))}{digit}" for digit, group in itertools.groupby(digits)])

assert lookAndSay('1') == '11'
assert lookAndSay('11') == '21'
assert lookAndSay('21') == '1211'
assert lookAndSay('1211') == '111221'
assert lookAndSay('111221') == '312211'

# Display info message
print("Give a string of digits:\n");
inputDigits = utility.readInputList(joinedWith = '')

# Display results
iteration40 = functools.reduce(lambda prev, i: lookAndSay(prev), range(40), inputDigits)
iteration50 = functools.reduce(lambda prev, i: lookAndSay(prev), range(10), iteration40)
print(f'{inputDigits} -> 40: {len(iteration40)} -> 50: {len(iteration50)}')