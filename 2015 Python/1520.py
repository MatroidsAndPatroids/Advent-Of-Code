import utility # my own utility.pl file
import primePy.primes

# The number of elves visiting the house is the sum of the housenumber's divisors
# The sum of the divisors of a number is multiplicative, eg. s(n * m) = s(n) * s(m) iff (n, m) = 1
# This function creates a list of divisor sums for all numbers
def divisorSumListWithNoBound(maxSum):
	sumList = [0, 1, 3]
	while sumList[-1] < maxSum:
		nextNumber = len(sumList)
		p = primePy.primes.factor(nextNumber)
		nextNumber = int(nextNumber / p)
		pPowered = p
		
		while True:
			quotient, remainder = divmod(nextNumber, p)
			if remainder == 0:
				nextNumber = quotient
				pPowered *= p
			else:
				break
		if nextNumber == 1:
			# nextNumber = p^k, therefore s(p^k) = (p^(k+1) - 1) / (p - 1)
			# (this the formula for s(p^k) = 1 + p + p^2 + ... + p^k = (p^(k+1) - 1) / (p - 1))
			sumList.append(int((pPowered * p - 1) / (p - 1)))
		else:
			# nextNumber = p^k * someNumber, therefore s(p^k * someNumber) = s(p^k) * s(someNumber)
			# (since someNumber is not divisible by p anymore)
			sumList.append(sumList[pPowered] * sumList[nextNumber])
	return sumList

# The number of elves visiting the house is the sum of the housenumber's below-50 divisors
# This function creates a list of such below-50 divisors
def divisorSumList(maxSum, divisorUpperBound = None):
	if divisorUpperBound == None:
		return divisorSumListWithNoBound(maxSum)
	
	sumList = [0, 1]
	while sumList[-1] < maxSum:
		nextNumber = len(sumList)
		sumOfDivisors = 0
		for divisor in range(1, divisorUpperBound + 1):
			quotient, remainder = divmod(nextNumber, divisor)
			if remainder == 0:
				sumOfDivisors += quotient
		sumList.append(sumOfDivisors)
	return sumList

# Display info message
print("Give the minimum number of presents to be found:\n")
minPresents = int(utility.readInputList(joinedWith = ''))

# Display results
sumList = divisorSumList(int(minPresents / 10))
print(f'Presents for all houses: House {len(sumList) - 1} -> {sumList[-1] * 10} presents')
sumList = divisorSumList(int(minPresents / 11), divisorUpperBound=50)
print(f'Presents for 50 houses only: House {len(sumList) - 1} -> {sumList[-1] * 11} presents')
