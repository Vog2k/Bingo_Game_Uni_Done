import random
import copy
"""I definatly had help from google/Youtube with this one as it was super hard for me"""
"""
Welcome = input("Welcome to My Bingo game, Press enter to continue!:")
print()
print("Please read terms and conditions before playing.")
print()  # Since bingo is a form of gambling i thought i would add a terms and conditions.
print("We here at M.B.G do not condone gambling By playing Bingo\nyou agree to be bound by these terms and "
      "conditions but they do not\naffect your rights under the Consumer Rights Act 2015. ")
print(
    "You must be over 18\nyears of age to play My Bingo Game reserves the right to require all\nparticipants to prove "
    "that they are over 18 by production of a\n recognised photographic identity document.")
print()
# Little login phase
# Asks the user to enter their age
AGE = int(input("Please enter your Age:"))
if AGE > 17:  # If the age is over 17 then the user will be eligible if not then the programme will end
    print("You are Eligible ")
else:
    print("Sorry you are not Eligible to play")
    exit()

Go = input("Press Enter to accept and continue:")
print()
print("Welcome to My Bingo Game")
print()
Enter = input("Press Enter to start a game")"""


def clearScreen():
    print(chr(27) + "[2J")


def generateBoard():
    # This will be the random number generator for your board
    whitelist = list(range(1, 80))
    board = [list(), list(), list(), list(), list()]
    for x in range(0, 5):
        for y in range(0, 5):
            i = random.randint(0, len(whitelist) - 1)
            num = whitelist[i]
            del whitelist[i]
            board[x].append(num)
    board[2][2] = ' X'
    return board


# checks board if contains num
# Type in your number
def inBoard(num, board):
    for x in range(0, 5):
        for y in range(0, 5):
            if num == board[x][y]:
                board[x][y] = ' X'
                return True
    return False


# bool on if board meets win condition
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


def printBoard(board, OG):
    print("     Here is your board")
    print("Marked board   |   Unmarked board\n")
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


def draw(notDrawn):
    num = notDrawn[random.randint(0, len(notDrawn) - 1)]
    notDrawn.remove(num)
    return num


def playGame():
    notDrawn = list(range(1, 80))
    board1 = generateBoard()
    OG_BOARD1 = copy.deepcopy(board1)

    clearScreen()
    print('Enter Draw Number OR Enter q, then press enter to quit.\n')

    printBoard(board1, OG_BOARD1)

    while True:
        userInput = input()
        clearScreen()
        if userInput == 'q':
            print('Press Enter to Draw Number. Enter q, then press enter to quit.\n')
            printBoard(board1, OG_BOARD1)
            print("Game Over")
            exit()
        else:
            curDraw = draw(notDrawn)
            found = inBoard(curDraw, board1)
            print('Press Enter to Draw Number. Enter q, then press enter to quit.\n')
            printBoard(board1, OG_BOARD1)
            if didWin(board1) == True:
                while True:
                    clearScreen()
                    print('Winner! Enter "new" to start new game. Enter "q" to quit.\n')
                    printBoard(board1, OG_BOARD1)
                    print('BINGO!!! --- YOU WIN! --- Drew ' + str(curDraw))
                    userInput = input()
                    if userInput == 'q':
                        print("Game Over")
                        return False
                    elif userInput == 'new':
                        return True
            else:
                if found == True:
                    print("Found a match! " + str(curDraw))
                else:
                    print()
                    print("No match " + str(curDraw))


runGame = True
while runGame == True:
    runGame = playGame()
