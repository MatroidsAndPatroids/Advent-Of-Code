import utility # my own utility.pl file
import numpy # array

def isTriangle(sides):
    a, b, c = sorted(sides)
    return a + b > c

assert(not isTriangle([10, 25, 5]))

def countTriangles(triangles):
    return sum(isTriangle(triangle) for triangle in triangles)

def countTrianglesVertically(triangles):
    return sum(isTriangle(triangles[i:i+3, j]) for j in range(3) for i in range(0, len(triangles) - 2, 3))

# Display info message
print("Give a list of triangle side lengths:\n");
triangles = numpy.array([list(map(int, line.split())) for line in utility.readInputList()])

# Display results
print (f'{countTriangles(triangles) = }')
print (f'{countTrianglesVertically(triangles) = }')