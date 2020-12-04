import utility # my own utility.pl file
import re # split

def decompressedLength(text, part1 = True, marker = re.compile('\((\d+)x(\d+)\)')):
    # Parse 'A(2x2)BCD(2x2)EFG'
    match = marker.search(text)
    if not match:
        return len(text)

    length, multiplier = map(int, match.groups()) # find the next (##x##) part
    beginLength = match.start() # text length before (##x##)
    middle = text[match.end():match.end() + length] # replacement text after (##x##)
    end = text[match.end() + length:] # remaining text for further processing

    middleLength = length if part1 else decompressedLength(middle, part1)
    return beginLength + multiplier * middleLength + decompressedLength(end, part1)

assert decompressedLength('ADVENT') == 6
assert decompressedLength('A(1x5)BC') == 7
assert decompressedLength('(3x3)XYZ') == 9
assert decompressedLength('A(2x2)BCD(2x2)EFG') == 11
assert decompressedLength('(6x1)(1x3)A') == 6
assert decompressedLength('X(8x2)(3x3)ABCY') == 18

assert decompressedLength('(3x3)XYZ', False) == 9
assert decompressedLength('X(8x2)(3x3)ABCY', False) == 20
assert decompressedLength('(27x12)(20x12)(13x14)(7x10)(1x12)A', False) == 241920
assert decompressedLength('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN', False) == 445

# Display info message
print("Give a file in a peculiar compressed format:\n")
sequences = utility.readInputList()

# Display results
print (f"{sum(decompressedLength(seq) for seq in sequences) = }")
print (f"{sum(decompressedLength(seq, part1 = False) for seq in sequences) = }")
