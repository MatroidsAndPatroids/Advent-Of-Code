import utility # my own utility.pl file (readInputList, SimpleTimer)
from collections import OrderedDict

# Parse the input and return an ordered dictionary of ranges
def parseBlockedIps(rules, maxIpAddress):
    blackList = {}
    for line in rules:
        a, b = map(int, line.split('-'))
        blackList[a] = max(b, blackList.get(a, 0))
    
    return OrderedDict(sorted(blackList.items()))

# Convert interval list into distinct intervals (joining intervals with no gap in between)
def simplify(intervalDict, minIpAddress, maxIpAddress):
    simplifiedIntervals = OrderedDict()
    minIp = maxIpAddress
    maxIp = minIpAddress - 2
    
    for a, b in intervalDict.items():
        if a > maxIp + 1:
            if minIp <= maxIp:
                simplifiedIntervals[minIp] = maxIp
            minIp = a
            maxIp = b
        else:
            maxIp = max(maxIp, b)
    simplifiedIntervals[minIp] = maxIp
    
    return simplifiedIntervals
    
def length(simplifiedIntervals):
    return sum(b - a + 1 for a, b in simplifiedIntervals.items())

# Calculate the lowest allowed IP address (part1), or the number of allowed IPs (part2)
def firewallRules(rules, minIpAddress, maxIpAddress, part2=False):
    blacklist = parseBlockedIps(rules, maxIpAddress)
    simplifiedBlacklist = simplify(blacklist, minIpAddress, maxIpAddress)
    
    firstAllowedIp = next(iter(simplifiedBlacklist.items()))[1] + 1
    allIps = maxIpAddress - minIpAddress + 1
    allowedIps = allIps - length(simplifiedBlacklist)

    return allowedIps if part2 else firstAllowedIp

smallExample = """
5-8
0-2
4-7
""".strip().split('\n')

assert firewallRules(smallExample, minIpAddress=0, maxIpAddress=9) == 3
assert firewallRules(smallExample, minIpAddress=0, maxIpAddress=9, part2=True) == 2

# Display info message
print("\nWhich IP ranges are blocked?")
rules = utility.readInputList()

# Display results
print(f'{firewallRules(rules, minIpAddress=0, maxIpAddress=4294967295) = }')
print(f'{firewallRules(rules, minIpAddress=0, maxIpAddress=4294967295, part2=True) = }')
