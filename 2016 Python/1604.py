import utility # my own utility.pl file

def realSectorId(room):
    # parse 'fubrjhqlf-edvnhw-dftxlvlwlrq-803[wjvzd]'
    name, sectorId, checksum = (room[:-11].replace('-', ''), int(room[-10:-7]), room[-6:-1])
    mostCommon = sorted((-name.count(letter), letter) for letter in set(name))
    if ''.join(letter for _, letter in mostCommon[:5]) == checksum:
        return sectorId
    return 0

def decypher(room):
    name, sectorId, checksum = (room[:-11], int(room[-10:-7]), room[-6:-1])
    a = ord('a')
    numLetters = ord('z') - ord('a') + 1
    decoded = ''.join(chr((ord(letter) - a + sectorId) % numLetters + a) if letter.isalpha() else ' ' for letter in name)
    print(decoded)
    return decoded

assert(realSectorId('aaaaa-bbb-z-y-x-123[abxyz]') == 123)
assert(realSectorId('a-b-c-d-e-f-g-h-987[abcde]') == 987)
assert(realSectorId('not-a-real-room-404[oarel]') == 404)
assert(realSectorId('totally-real-room-200[decoy]') == 0)
assert(decypher('qzmt-zixmtkozy-ivhz-343[decoy]') == 'very encrypted name')

# Display info message
print("Give a list of room name, sector id, checksum triplets:\n")
rooms = utility.readInputList()

# Display results
print (f'{sum(realSectorId(room) for room in rooms) = }')
for room in rooms:
    if 'north' in decypher(room):
        print (f'{room = }, {decypher(room) = }')