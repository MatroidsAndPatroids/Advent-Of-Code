import utility # my own utility.pl file
import math # sqrt, prod

def increase(dictionary, key):
	if key in dictionary:
		dictionary[key] += 1
	else:
		dictionary[key] = 1

class Primes:
	def __init__(self):
		self.primes = [2]

	def __str__(self):
		return ' '.join(self.primes)

	def __repr__(self):
		return self.__str__()

	def findSmallestDivisor(self, number):
		root = int(math.sqrt(number))

		for n in range(self.primes[-1] + 1,root + 1):
			if self.findSmallestDivisor(n) == n:
				self.primes.append(n)

		for p in self.primes:
			if number % p == 0:
				return p
			if root <= p:
				return number
		return number

	def primeFactors(self, number):
		root = int(math.sqrt(number))

		factors = {}
		while number > 1:
			p = self.findSmallestDivisor(number)
			while number % p == 0:
				number = int(number / p)
				increase(factors, p)

		return factors

	def sumOfDivisors(self, number):
		factors = self.primeFactors(number)
		return int(math.prod((p ** (k + 1) - 1) / (p - 1) for p, k in factors.items()))

	def countPresents(self, houseNumber):
		count = 0
		for i in range(1, min(houseNumber + 1, 50)):
			if houseNumber % i == 0:
				count += int(houseNumber / i)
		return count

for n in range(10):
	print(f'{n} -> {Primes().sumOfDivisors(n)}')

print(Primes().primeFactors(3310000))
n = 2*2*3*5*7*11*13*17
print(f'{n} {Primes().sumOfDivisors(n)}')

P = Primes()
for i in range(1):
	if i % 10000 == 0:
		print(f'{i} -> {P.sumOfDivisors(i)}')
	if 3310000 < P.sumOfDivisors(i):
		print(f'{i} -> {P.sumOfDivisors(i)}')
		break

print('Presents:')
for i in range(10000000):
	limit = int(33100000 / 11)
	if i % 10000 == 0:
		print(f'{i} -> {P.countPresents(i)}')
	if limit < P.countPresents(i):
		print(f'{i} -> {P.countPresents(i)}')
		break

