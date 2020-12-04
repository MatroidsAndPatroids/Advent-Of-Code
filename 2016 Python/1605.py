import utility # my own utility.pl file
import hashlib # md5 implementation

# Generate the MD5 hash of an input string and convert it to string 
def generateMd5Hash(secretKey):
    return hashlib.md5(secretKey.encode()).hexdigest()

# Find Santa the lowest positive number that appended to the key
# produces a hash starting with a given prefix 
def findLowestNumberMatchingThePrefix(secretKey, prefix, count = 0):
    while not generateMd5Hash(secretKey + str(count)).startswith(prefix):
        count += 1
        
    md5Hash = generateMd5Hash(secretKey + str(count))
    #print(f"{secretKey = }, {count = }, {md5Hash = }, {prefix = }")
    return count, md5Hash

# Find the password from the 6th and 7th digits of the MD5 hashes
def password(secretKey, prefix):
    password1 = ''
    password2 = 8 * ['_']
    count = -1
    charactersFound = 0
    print(f"{'Index'.center(15, ' ')}\t{'Hash'.center(15, ' ')}\t{'Part 1'.center(8, ' ')}\t{'Part 2'.center(8, ' ')}")
    while charactersFound < 8:
        count, md5hash = findLowestNumberMatchingThePrefix(secretKey, prefix, count + 1)
        pos = md5hash[5]
        if len(password1) < 8:
            password1 += pos
        if pos.isdigit() and int(pos) < 8 and password2[int(pos)] == '_':
            charactersFound += 1
            password2[int(pos)] = md5hash[6]
        print(f"{str(count).rjust(15, ' ')}\t{md5hash[5:20].rjust(15, ' ')}\t{password1.ljust(8, '_')}\t{''.join(password2)}")
    return password1, ''.join(password2)

assert password('abc', '00000') == ('18f47a30', '05ace8e3')

# Display info message
print("Give a door ID:\n")
doorId = utility.readInputList(joinedWith = '')

# Display results
print (f"{password(doorId, '00000') = }")