import utility # my own utility.pl file
import hashlib # md5 implementation

# Generate the MD5 hash of an input string and convert it to string 
def generateMd5Hash(secretKey):
	return hashlib.md5(secretKey.encode()).hexdigest()

# Find Santa the lowest positive number that appended to the key
# produces a hash starting with a given prefix 
def findLowestNumberMatchingThePrefix(secretKey, prefix):
	adventCoin = 0
	while not generateMd5Hash(secretKey + str(adventCoin)).startswith(prefix):
		adventCoin += 1
		
	md5Hash = generateMd5Hash(secretKey + str(adventCoin))
	print(f"{secretKey = }, {adventCoin = }, {md5Hash = }, {prefix = }")
	return adventCoin

assert findLowestNumberMatchingThePrefix('abcdef', '00000') == 609043
assert findLowestNumberMatchingThePrefix('pqrstuv', '00000') == 1048970

# Display info message
print("\nGive Secret Key to find the lowest number postfix for which the md5 hash has a 1-6 zero prefix\n");
secretKey = utility.readInputList(joinedWith = '')

# Display results
findLowestNumberMatchingThePrefix(secretKey, '')
findLowestNumberMatchingThePrefix(secretKey, '0')
findLowestNumberMatchingThePrefix(secretKey, '00')
findLowestNumberMatchingThePrefix(secretKey, '000')
findLowestNumberMatchingThePrefix(secretKey, '0000')
findLowestNumberMatchingThePrefix(secretKey, '00000')
findLowestNumberMatchingThePrefix(secretKey, '000000')
