import utility # my own utility.pl file
import re # compile, search, findall

# A string is nice if it has all three of these properties
# 1. it contains at least 3 vowels (aeiou only)
# 2. it contains at least on letter that appears twice in a row
# 3. it does not contain any of the forbidden strings (ab, cd, pq, xy)
def isNice1(text):
	vowel_re = re.compile(r"[aeiou]")
	dup_re = re.compile(r"(.)\1")
	exclude_re = re.compile(r"(ab|cd|pq|xy)")
	
	numberOfVowels = len(vowel_re.findall(text))
	numberOfPairs = len(dup_re.findall(text))
	numberOfForbidden = len(exclude_re.findall(text))
	return numberOfVowels >= 3 and numberOfPairs >= 1 and numberOfForbidden == 0

assert isNice1('ugknbfddgicrmopn')
assert isNice1('aaa')
assert not isNice1('jchzalrnumimnmhp')
assert not isNice1('haegwjzuvuyypxyu')
assert not isNice1('dvszwmarrgswjxmb')

# From now on a string is nice if it has all two of these properties
# 1. it contains a pair of any two letters that appears at least twice in the string without overlapping
# 2. it contains at least one letter which repeats with exactly one letter between them
def isNice2(text):
	dup_pair_re = re.compile(r"(..).*\1")
	repeat_re = re.compile(r"(.).\1")
	
	numberOfRepeatingPairs = len(dup_pair_re.findall(text))
	numberOfRepeatingLetters = len(repeat_re.findall(text))
	return numberOfRepeatingPairs >= 1 and numberOfRepeatingLetters >= 1

assert isNice2('qjhvhtzxzqqjkmpb')
assert isNice2('xxyxx')
assert not isNice2('uurcxstgmygtbstg')
assert not isNice2('ieodomkazucvgmuy')
assert not isNice2('aaa')
assert isNice2('aaaa')

# Display info message
print("Give a list of strings for which we find the nice ones, which are not naughty.\n");
textList = utility.readInputList()

# Display results
numOfNiceStrings = sum(map(isNice1, textList))
numOfNewNiceStrings = sum(map(isNice2, textList))
print (f'{numOfNiceStrings = }, {numOfNewNiceStrings = }')