import random
import copy


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


"""def draw(notDrawn):
    num = notDrawn[random.randint(0, len(notDrawn) - 1)]
    notDrawn.remove(num)
    return num"""

def call(caller):
    caller = input()
    num = caller

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