import time
import utility # my own utility.pl file
import md5 # md5 implementation file downloaded

# Generate the MD5 hash of an input string and convert it to string
def generateMd5Hash(inputString):
	return str(md5.md5_to_hex(md5.md5(inputString.encode())))

assert generateMd5Hash('abcdef609043') == '000001dbbfa3a5c83a2d506429c7b00e'
assert generateMd5Hash('pqrstuv1048970') == '000006136ef2ff3b291c85725f17325c'

# Find Santa the lowest positive number that appended to the key
# produces a hash starting with a given prefix string
def findLowestNumberWithMatchingPrefix(keyString, prefixString):

	i = 0
	while i > -1: # infinite loop, search until find one eventually
		jointMd5Hash = generateMd5Hash(keyString + str(i))
		if jointMd5Hash.startswith(prefixString):
			return i
		i += 1

	return -1

def findAnswerAndPrintResult(keyString, prefixString):
	startTime = time.time()
	lowestNumber = findLowestNumberWithMatchingPrefix(keyString, prefixString)
	elapsedTime = time.time() - startTime
	secPerMillion = elapsedTime * 1000000.0 / (lowestNumber + 1)
	print(f"key = {keyString}, prefix = {prefixString}, lowestNumber = {lowestNumber}, md5Hash = {generateMd5Hash(key + str(lowestNumber))}, elapsedTime = {elapsedTime}, secPerMillion = {secPerMillion}")

# Display info message
print("\nGive a short string of characters to find the lowest number postfix for which the md5 hash starts with 5 or 6 zeroes respectively\n");

key = ''.join(utility.readInputList())

# Display results
findAnswerAndPrintResult(key, '0')
findAnswerAndPrintResult(key, '00')
findAnswerAndPrintResult(key, '000')
findAnswerAndPrintResult(key, '0000')
findAnswerAndPrintResult(key, '00000')
findAnswerAndPrintResult(key, '000000')

