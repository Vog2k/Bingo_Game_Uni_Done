import random

import numpy

'''
"""Welcome = input("Welcome to My Bingo game, Press enter to continue!:")
print()
print("Please read terms and conditions before playing.")
print()  # Since bingo is a form of gambling i thought i would add a terms and conditions.
print("We here at M.B.G do not condone gambling By playing Bingo Lingo you agree to be bound by these terms and "
      "conditions but they do not affect your rights under the Consumer Rights Act 2015. ")
print("You must be over 18 years of age to play My Bingo Game reserves the right to require all participants to prove "
      "that they are over 18 by production of a recognised photographic identity document.")
print()
# Little login phase
# Asks the user to enter their age
AGE = int(input("Please enter your Age:"))
if AGE > 17:  # If the age is over 17 then the user will be eligible if not then the programme will end
    print("You are Eligible ")
else:
    print("Sorry you are not Eligible to play")
    exit()

print()  # I'm not sure how to have gaps in between the words ro il just print blank spaces
print()
Go = input("Press Enter to accept and continue:")
print()
print("Welcome to My Bingo Game")
print()
Enter = input("Press Enter to start a game")
print()
print("To quit application please type 'Q' or 'q'")
'''
'''
Play = input("Press Enter to start a game")
BINGO = "Winner"

#Player_1 = input("Insert player name :")

#Player_2 = input("Insert player name :")

print("---------------------------------")

#print("Player One  :" + Player_1)
restart = "Press enter to continue or type 'B'  or  'b' for Bingo"
print()'''


thisdict = {
  "B":
}
thisdict.pop("model")
print(thisdict)

# Below will be the game the random number generator
# Player one's board

board = random.sample(range(0, 80), 5)
board1 = random.sample(range(0, 80), 5)
board2 = random.sample(range(0, 80), 5)
board3 = random.sample(range(0, 80), 5)
board4 = random.sample(range(0, 80), 5)
print(board)
print(board1)
print(board2)
print(board3)
print(board4)

print()

print("-----------------------------------")

# print("Player Two  :" + Player_2)

print()
# Player two's board
game_board = board, board1, board2, board3, board4
board6 = random.sample(range(0, 80), 5)
board7 = random.sample(range(0, 80), 5)
board8 = random.sample(range(0, 80), 5)
board9 = random.sample(range(0, 80), 5)
board10 = random.sample(range(0, 80), 5)
print(board6)
print(board7)
print(board8)
print(board9)
print(board10)

print()

print("----------------------------------")

print("You're numbers are ! ")
print("Press enter to continue or type 'B'  or  'b' for Bingo")
'''
if "BINGO" == BINGO:
    print("BINGO!")
    print("WELL DONE")
    input("To play again type 'R' or 'r'")
'''
num = random.randint(0, 80)


print(num)
'''
for i in range(5,):
    for j in range(2):
        print(board, board2, board3, board4, board1, end="")
        for i in range(1):
            for j in range(1):
                print(board2, board3, board4, board1, end="")
            for i in range(1):
                for j in range(1):
                    print(board3, board4, board1, end="")
                print()
    print()
'''
'''print(game_board)'''


# check for vertical win
'''for y in range(0, 5):
    count = 0
    for x in range(0, 5):
        if board[y][x] != ' X':
            break
        else:
            count += 1
    if count == 5:
    return True'''

# Vertical bingo

# Horizontal bingo

# Diagonal


# print(num, + num1, num2, + num3, num4, + num5, num6, + num7, num8, + num9, numA, + numB)


#Whatever number shows in print i want the bingo boards to mark out the current number
