import utility # my own utility.pl file

# Node class for the linked list
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

# Linked list class for storing the cups
class CupCircle:
    def __init__(self):
        self.node = {}
        self.current = None # current node
    
    def insertAfterCurrent(self, value):
        if self.current:
            # insert a new element after the current one, it will become the new current
            next = self.current.next
            self.current.next = Node(value)
            self.node[value] = self.current.next
            self.current = self.current.next
            self.current.next = next
        else:
            # the new node is the only node in the circle
            self.current = Node(value)
            self.current.next = self.current
            self.node[value] = self.current
            
    def setCurrent(self, value):
        self.current = self.node[value]
    
    def move(self):
#         print(self.subCircle(self.current.value, len(self.node)))
        size = 3
        if size not in range(len(self.node)):
            return
        
        # cut out 3 elements after the current one, collect their values
        values = set()
        last = self.current
        first = self.current.next
        for i in range(size):
            last = last.next
            values.add(last.value)
        self.current.next = last.next
        
        # calculate the destination node
        destValue = self.current.value - 1
        while True:
            if destValue == 0:
                destValue = max(self.node.keys())
            if destValue not in values:
                break
            destValue -= 1
        destNode = self.node[destValue]
        
#         print(f'{self.current.value = } {destValue = }')
        # insert first-next line after the destination node
        last.next = destNode.next
        destNode.next = first
        
        # increment current node
        self.current = self.current.next
    
    def subCircle(self, startValue, size):
        start = self.node[startValue]
        sub = []
        for i in range(size):
            start = start.next
            sub.append(start.value)
        return sub

# Simulates the instructions
def playCrabCups(instructions, part2 = False):
    cups = list(map(int, list(''.join(instructions).strip('\n'))))
    circle = CupCircle()
    for value in cups:
        circle.insertAfterCurrent(value)
    if part2:
        for value in range(max(cups) + 1, 1000000 + 1):
            circle.insertAfterCurrent(value)
    circle.setCurrent(cups[0])

    moves = 10000000 if part2 else 100
    for i in range(moves):
        circle.move()

    sol = circle.subCircle(1, len(cups) - 1) # 8 elements after 1
    sol = sol[0] * sol[1] if part2 else ''.join(map(str, sol))
    print(sol)
    return sol

# Check test cases
smallExample = """
389125467
""".strip().split('\n')
assert playCrabCups(smallExample) == '67384529'
assert playCrabCups(smallExample, part2 = True) == 149245887792

# Display info message
print("Give the order of the cups:\n")
instructions = utility.readInputList()

# Display results
print(f'{playCrabCups(instructions) = }')
print(f'{playCrabCups(instructions, part2 = True) = }')