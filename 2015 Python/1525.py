import utility # my own utility.pl file

def code(index):
	value = 20151125
	for i in range(index - 1):
		value = value * 252533 % 33554393
	return value

def index(row, col):
	diag = row + col
	return int(diag * (diag - 1) / 2) - row + 1

assert code(index(1, 1)) == 20151125
assert code(index(2, 2)) == 21629792
assert code(index(2, 6)) == 4041754
assert code(index(5, 4)) == 6899651

# Display info message
print("Give the coordinates of the code:\n")
inputStringList = utility.readInputList()

# Display results
print(f'Code = {code(index(3010, 3019))}')