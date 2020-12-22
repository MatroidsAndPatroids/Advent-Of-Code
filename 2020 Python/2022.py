import utility # my own utility.pl file

# Emulate a subgame of Crab Combat and return the score.
# The score is positive if Player 1 wins, otherwise negative.
def subgameScore(hand1, hand2, part2 = False):
#     print('SubGAME starts')
    
    gameStates = set()
    
    while hand1 and hand2:
        currentState = tuple(hand1 + [-1] + hand2) # use -1 as a makeshift delimiter
        if currentState in gameStates:
            # same state happened already before, hand1 wins
            hand2 = []
            break
        
        gameStates.add(currentState)
        card1 = hand1[0]
        card2 = hand2[0]
        player1wins = card1 > card2
        
        if part2 and len(hand1) > card1 and len(hand2) > card2:
            subscore = subgameScore(hand1[1:card1 + 1], hand2[1:card2 + 1], part2)
            player1wins = subscore > 0
            
#         print(hand1, hand2)
#         print(f'Player {1 if player1wins else 2} wins with {card1}, {card2}')
        if player1wins:
            hand1 = hand1[1:] + [card1, card2]
            hand2 = hand2[1:]
        else:
            hand2 = hand2[1:] + [card2, card1]
            hand1 = hand1[1:]
            
    winner = hand1 if hand1 else hand2
    score = sum((i + 1) * winner[-(i + 1)] for i in range(len(winner)))
    score = score if hand1 else -score
#     print('SubGAME ends with score ' + str(score))
    return score


# Emulate THE GAME of Crab Combat and return the score.
# The score is positive if Player 1 wins, otherwise negative.
def emulateCrabCombat(instructions, part2 = False):
    # Parse hands
    hand1 = []
    hand2 = []
    player = 0
    for line in instructions:
        if not line:
            continue
        if 'Player ' in line:
            player += 1
            continue
        value = [int(line)]
        if player == 1:
            hand1 += value
        elif player == 2:
            hand2 += value
    
    # Play the game
    score = subgameScore(hand1, hand2, part2)
    print(score)
    return score

# Check test cases
smallExample = """
Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10
""".strip().split('\n')
infiniteExample = """
Player 1:
43
19

Player 2:
2
29
14
""".strip().split('\n')
assert emulateCrabCombat(smallExample) == -306
assert emulateCrabCombat(smallExample, part2 = True) == -291
assert emulateCrabCombat(infiniteExample, part2 = True) == 105

# Display info message
print("Give a list of ship/waypoint movement instructions:\n")
instructions = utility.readInputList()

# Display results
print(f'{emulateCrabCombat(instructions) = }')
print(f'{emulateCrabCombat(instructions, part2 = True) = }')