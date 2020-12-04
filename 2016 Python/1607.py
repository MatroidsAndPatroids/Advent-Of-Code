import utility # my own utility.pl file
import re # split

# Does the text include an ABBA (Autonomous Bridge Bypass Annotation)?
def autonomousBridgeBypassAnnotation(text):
    #abba = re.compile(r'([a-z])((?!\1)[a-z])\2\1')
    return any(text[i] == text[i + 3] != text[i + 1] == text[i + 2] for i in range(len(text) - 3))

# Does the IPv7 address support TLS (transport-layer snooping)?
def transportLayerSnooping(IPv7):
    tokens = re.split('\[|\]', IPv7)
    supernetSequences, hypernetSequences = tokens[::2], tokens[1::2]
    return any(autonomousBridgeBypassAnnotation(token) for token in supernetSequences) \
        and all(not autonomousBridgeBypassAnnotation(token) for token in hypernetSequences)

assert transportLayerSnooping('abba[mnop]qrst')
assert not transportLayerSnooping('abcd[bddb]xyyx')
assert not transportLayerSnooping('aaaa[qwer]tyui')
assert transportLayerSnooping('ioxxoj[asdfgh]zxcvbn')

# Return the list of reversed ABAs  (Area-Broadcast Accessor) into BABs (Byte Allocation Block)
def potentialByteAllocationBlocks(text):
    #aba = re.compile(r'([a-z])((?!\1)[a-z])\1')
    return [text[i + 1] + text[i] + text[i + 1] for i in range(len(text) - 2) if text[i] == text[i + 2] != text[i + 1]]

# Does the IPv7 address support SSL (super-secret listening)?
def superSecretListening(IPv7):
    tokens = re.split('\[|\]', IPv7)
    supernetSequences, hypernetSequences = tokens[::2], tokens[1::2]
    # Collect all ABAs (Area-Broadcast Accessor) inside the supernet sequences and reverse them to BABs
    babCollection = [bab for token in supernetSequences for bab in potentialByteAllocationBlocks(token)]
    # Check if there is a corresponing BAB (Byte Allocation Block) in the hypernet sequences
    return any(bab in token for bab in babCollection for token in hypernetSequences)

assert superSecretListening('aba[bab]xyz')
assert not superSecretListening('xyx[xyx]xyx')
assert superSecretListening('aaa[kek]eke')
assert superSecretListening('zazbz[bzb]cdb')

# Display info message
print("Give a list of IPv7 adresses:\n")
IPv7list = utility.readInputList()

# Display results
print (f"{sum(transportLayerSnooping(IPv7) for IPv7 in IPv7list) = }")
print (f"{sum(superSecretListening(IPv7) for IPv7 in IPv7list) = }")