# BINGO Game
# By Timothy Leatau

import random
import copy
import numpy

"i definitely needed help from google with this project "


def Start():
    Welcome = input("Welcome to My Bingo game, Press enter to continue!:")
    print()
    print("Please read terms and conditions before playing.")
    print()  # Since bingo is a form of gambling I thought I would add a terms and conditions.
    print("We here at M.B.G do not condone gambling By playing Bingo\nyou agree to be bound by these terms and "
          "conditions but they do not\naffect your rights under the Consumer Rights Act 2015. ")
    print(
        "You must be over 18\nyears of age to play My Bingo Game reserves the right to require all\nparticipants to prove "
        "that they are over 18 by production of a\nrecognised photographic identity document.")
    print()
    # Little login phase
    # Asks the user to enter their age
    AGE = int(input("Please enter your Age:"))
    if AGE > 17:  # If the age is over 17 then the user will be eligible if not then the programme will end
        print()
        print("You are Eligible. ")
    else:
        print("Sorry you are not Eligible to play")
        exit()

    print()
    Go = input("Press Enter to accept and continue:")
    print()
    print("Welcome to My Bingo Game")
    print()
    print("The rules: The objective of the game is to match your drawn numbers with the numbers on you're board\n"
          "once you have successfully matched five numbers in a row, In directions of either top to bottem,"
          "left to right\nYou will achive Bingo and win a hi-5 from me "
          "or even diagonally\n")
    Enter = input("Press Enter to start a game\n")
    print("Good luck!\n")


# Escape sequence to clear screen
def Wipe():
    print(chr(27) + "[2J")


# Gerates the board in a 5x5 style
# Variables being whitelist, board, i, num
# Whitelist will be the randomly selected numbers
def generateBoard():
    whitelist = list(range(1, 81))
    board = [list(), list(), list(), list(), list()]
    for x in range(0, 5):  # Top to bottem
        for y in range(0, 5):  # left to right
            i = random.randint(0, len(whitelist) - 1)
            num = whitelist[i]
            del whitelist[i]
            board[x].append(num)
    board[2][2] = ' X'
    return board


# checks board if the board contains the drawn number
def inBoard(num, board):
    for x in range(0, 5):
        for y in range(0, 5):
            if num == board[x][y]:
                board[x][y] = ' X'
                return True
    return False


def didWin(board):
    # check for horizontal win
    for x in range(0, 5):
        count = 0
        for y in range(0, 5):
            if board[y][x] != ' X':
                break
            else:
                count += 1
        if count == 5:
            return True

    # check for vertical win
    for y in range(0, 5):
        count = 0
        for x in range(0, 5):
            if board[y][x] != ' X':
                break
            else:
                count += 1
        if count == 5:
            return True

    # check for diagonal - top left to bottom right
    count = 0
    for i in range(0, 5):
        if board[i][i] != ' X':
            break
        else:
            count += 1
    if count == 5:
        return True

    # check for diagonal - top right to bottom left
    count = 0
    for x in range(0, 5):
        if board[4 - x][x] != ' X':
            break
        else:
            count += 1
    if count == 5:
        return True

    return False


# Will print the board in the command
def printBoard(board, OG):
    print(" Crossed off   |  You're Numbers")
    for y in range(0, 5):
        ogStr = ''
        for x in range(0, 5):
            if board[x][y] != ' X':
                if int(board[x][y]) < 10:
                    print(" ", end='')
                    ogStr += ' '
            print(board[x][y], end=" ")
            ogStr += str(OG[x][y]) + ' '
        print('   ' + ogStr)


# Users entered number
def draw(notDrawn):
    rannum = int(input("Please enter a number between 1-80: "))
    print()
    notDrawn.remove(rannum)
    return rannum


def playGame():
    Start()
    notDrawn = list(range(1, 81))
    board1 = generateBoard()
    OG_BOARD1 = copy.deepcopy(board1)

    Wipe()

    printBoard(board1, OG_BOARD1)

    while True:
        userInput = input
        Wipe()
        if userInput == 'q':

            printBoard(board1, OG_BOARD1)
            print("Game Over")
            print("Thank you for playing !")
            exit()
        else:
            cur_draw = draw(notDrawn)
            found = inBoard(cur_draw, board1)

            printBoard(board1, OG_BOARD1)
            if didWin(board1) == True:
                while True:
                    Wipe()
                    print('Winner! Enter "new" to start new game. Enter "q" to quit.\n')
                    printBoard(board1, OG_BOARD1)
                    print()
                    print('BINGO!!! Congratulations you have won, Last drawn number :' + str(cur_draw))
                    userInput = input()
                    if userInput == 'q':
                        print("Game Over")
                        return False # User has won the game and has an option to start again or quit out
                    elif userInput == 'new':
                        return True
            else:
                if found == True:
                    print()
                    print("Found a match!\n\nYou're number is " + str(cur_draw))
                    print()
                else:  # Determines if the played has a matched number
                    print()
                    print("Next draw. No Match.\n\nYou're number is " + str(cur_draw))
                    print()


runGame = True
while runGame == True:
    runGame = playGame()

"""Test case: Testing that the users inputs compiles 
input: 60
expected output: Matches number on board
actual output: Matched number on board
result pass"""

"""Test case: Testing that the users inputs compiles 
input: 60
expected output: Matches number on board
actual output: Will not accept duplicate number
result fail"""

"""Test case: Testing that the users inputs compiles 
input: q
expected output: Quits once q is entered
actual output: Worked well 
result pass"""

"""Test case: Testing that the users inputs compiles 
input: 17
expected output: Declined access
actual output: Sorry not old enough
result pass"""

"""Test case: Testing that the users inputs compiles 
input: new
expected output: Will wipe the boards and reset the numbers in random
actual output: cleared numbers ready for a new input/draw number
result pass"""

"""Test case: Testing that the users inputs compiles 
input: (None)
expected output: crash
actual output: crash
result fail"""
