import sys # argv
import os.path # splitext, basename, isfile
import inspect # stack for finding the filename of the function caller

# Retreive a list of input strings needed for the task OR
# concatenate the list of input strings into one string, if $joinedWith is given.
#
# There are 4 possible ways to execute the function's caller script 'foo.py'
# 1. python foo.py                       (tries to read foo.txt as input, if it exists)
# 2. python foo.py                       (asks keyboard input, if foo.txt doesn't exist)
# 3. python foo.py inputfile             (tries to read inputfile as input, if it exists)
# 4. python foo.py line1 line2 ... lineN (argv[1:] becomes the input list, if line1 is not an existing file)
def readInputList(joinedWith = None):

	commandLineArgumentCount = len(sys.argv)

	if commandLineArgumentCount > 1:
		inputFileName = sys.argv[1]
	else:
		callersFileName = inspect.stack()[1].filename
		withOutExtension = str(os.path.splitext(os.path.basename(callersFileName))[0])
		inputFileName = withOutExtension + ".txt"

	if (os.path.isfile(inputFileName)):
		text = f'Reading file: {inputFileName}'
		inputFile = open(inputFileName, "r")
		inputString = inputFile.read()
		inputStringList = inputString.split('\n')
	elif commandLineArgumentCount > 1:
		text = 'First command line argument is not a file, thus it becomes the input string'
		inputStringList = sys.argv[1:]
	else:
		text = 'Given by hand'
		inputString = input('No command line argument given, please enter a list by hand, separated by spaces:\n')
		inputStringList = inputString.split(' ')

	# Delete last line if empty
	if inputStringList and not inputStringList[-1]:
		del inputStringList[-1]

	lines = len(inputStringList)
	characters = sum(len(line) for line in inputStringList)
	print(f'{text} ({lines} lines, {characters} characters)\n')

	if joinedWith == None:
		return inputStringList
	return joinedWith.join(inputStringList)