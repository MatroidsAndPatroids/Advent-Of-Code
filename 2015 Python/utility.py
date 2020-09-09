import sys
import os.path

# Retreive the input string needed for the task
#
# There are 3 possible inputs
# 1. read existing text file given in the first command line argument
# 2. use first command line argument as input (when no such text file exists)
# 3. ask keyboard input from the user (when no command line argument is given)

def readInput():

	commandLineArgumentCount = len(sys.argv)

	if commandLineArgumentCount > 1:
		inputString = sys.argv[1]
		if (os.path.isfile(inputString)):
			print(f'Command line argument is also a file. Reading {inputString}')
			inputFile = open(inputString, "r")
			inputString = inputFile.read()
		else:
			print('Command line argument is not a file, thus it becomes the input string.')
	else:
		inputString = input('No command line argument given, please enter an input string')

	print(f'Input string lenght = {len(inputString)}\n')

	return inputString

# Retreive a list of input strings needed for the task
#
# There are 3 possible inputs
# 1. read existing text file given in the first command line argument
# 2. use first command line argument as input (when no such text file exists)
# 3. ask keyboard input from the user (when no command line argument is given)

def readInputList():

	commandLineArgumentCount = len(sys.argv)

	if commandLineArgumentCount > 1:
		filename = sys.argv[1]
		if (os.path.isfile(filename)):
			print(f'First command line argument is also a file. Reading {filename}')
			inputFile = open(filename, "r")
			inputString = inputFile.read()
			inputStringList = inputString.split('\n')
		else:
			print('First command line argument is not a file, thus it becomes the input string.')
			inputStringList = sys.argv[1:]
	else:
		inputString = input('No command line argument given, please enter an input string list separated by spaces:\n')
		inputStringList = inputString.split(' ')

	# Delete last line if empty
	if inputStringList and not inputStringList[-1]:
		del inputStringList[-1]

	print(f'Input list lenght = {len(inputStringList)}\n')

	return inputStringList
