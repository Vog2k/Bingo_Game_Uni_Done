
import random
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

Play = input("Press Enter to start a game")
BINGO = "Winner"

#Player_1 = input("Insert player name :")

#Player_2 = input("Insert player name :")

print("---------------------------------")

#print("Player One  :" + Player_1)
restart = "Press enter to continue or type 'B'  or  'b' for Bingo"
print()

# Below will be the game the random number generator
# Player one's board
for item in arr:
    board = random.sample(range(0, 50), 5)
    board1 = random.sample(range(0, 50), 5)
    board2 = random.sample(range(0, 50), 5)
    board3 = random.sample(range(0, 50), 5)
    board4 = random.sample(range(0, 50), 5)
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
board6 = random.sample(range(0, 50), 5)
board7 = random.sample(range(0, 50), 5)
board8 = random.sample(range(0, 50), 5)
board9 = random.sample(range(0, 50), 5)
board10 = random.sample(range(0, 50), 5)
print(board6)
print(board7)
print(board8)
print(board9)
print(board10)

print()

input("You're numbers are ! ")

print("----------------------------------")

if "BINGO" == BINGO:
    print("BINGO!")
    print("WELL DONE")
    input("To play again type 'R' or 'r'")
while True:
    num = random.randint(0, 50)
    num1 = random.randint(0, 50)
    num2 = random.randint(0, 50)
    num3 = random.randint(0, 50)
    num4 = random.randint(0, 50)
    num5 = random.randint(0, 50)
    num6 = random.randint(0, 50)
    num7 = random.randint(0, 50)
    num8 = random.randint(0, 50)
    num9 = random.randint(0, 50)
    numA = random.randint(0, 50)
    numB = random.randint(0, 50)

# print(num, + num1, num2, + num3, num4, + num5, num6, + num7, num8, + num9, numA, + numB)
    input(num, + num1, + restart)

