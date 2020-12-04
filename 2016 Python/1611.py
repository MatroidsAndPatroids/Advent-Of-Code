import utility # my own utility.pl file
import re # compile, match

class RadioisotopeTestingFacility:
    def __init__(self, instructions):
        self.floors = {}
        self.elevator = 'first floor'
        
        for instruction in instructions:
            # Parse 'The first floor contains a thulium generator, a
            # thulium-compatible microchip, a plutonium generator, and a strontium generator.'
            tokens = re.split('The |, a | a |, and a | and a |\.| contains nothing relevant.| contains', instruction)
            floorname = tokens[1]
            items = list(map(self.convertFloorname, tokens[3:-1]))
            self.floors[floorname] = items
            
        print(self)
            
    def convertFloorname(self, floornameToken):
        words = floornameToken.split()
        return (words[0][0] + words[1][0]).upper()
                
    def __str__(self):
        text = ''
        for floorname, items in self.floors.items():
            elevator = ' E' if self.elevator == floorname else ''
            text += f'{floorname}: {items}{elevator}\n'
        return text
    
    def solutionReached(self, floorname):
        for floor, items in self.floors.items():
            if floor != floorname and items:
                return False
        return True
    
    def tryMoving(self, item1, item2, delta):
        
    
    def getToAssembly(self, floorname):
        items = self.floors[floorname]
        for i in range(len(items)):
            for j in range(i, len(items)):
                tryMoving(items[i], items[j], 1)
                tryMoving(items[i], items[j], -1)
        return 0
    
smallExample = [
    'The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.',
    'The second floor contains a hydrogen generator.',
    'The third floor contains a lithium generator.',
    'The fourth floor contains nothing relevant.']
assert RadioisotopeTestingFacility(smallExample).getToAssembly('fourth floor') == 11


# Display info message
print("Give a file in a peculiar compressed format:\n")
arrangement = utility.readInputList()

# Display results
print(f'{RadioisotopeTestingFacility(arrangement).getToAssembly("fourth floor") = }')