import random
import copy


def clearScreen():
    print(chr(27) + "[2J")  # Escape sequence to clear screen


def generateBoard():
    whitelist = list(range(1, 81))
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

    # check for diagnal - top right to bottom left
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
    print(' Marked Board   |  Board Numbers')
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
    rannum = int(input("Please enter a number between 1-80: "))
    print()
    notDrawn.remove(rannum)
    return rannum


def playGame():
    notDrawn = list(range(1, 81))
    board1 = generateBoard()
    OG_BOARD1 = copy.deepcopy(board1)

    clearScreen()
    print('Enter q, then press enter to quit.\n')
    printBoard(board1, OG_BOARD1)

    while True:
        userInput = input
        clearScreen()
        if userInput == 'q':
            print('Enter q, then press enter to quit.\n')
            printBoard(board1, OG_BOARD1)
            print("Game Over")
            exit()
        else:
            curDraw = draw(notDrawn)
            found = inBoard(curDraw, board1)
            print('Enter q, then press enter to quit.\n')
            printBoard(board1, OG_BOARD1)
            if didWin(board1) == True:
                while True:
                    clearScreen()
                    print('Winner! Enter "new" to start new game. Enter "q" to quit.\n')
                    printBoard(board1, OG_BOARD1)
                    print('BINGO!!! Congratulations you have won, Last drawn number' + str(curDraw))
                    userInput = input()
                    if userInput == 'q':
                        print("Game Over")
                        return False
                    elif userInput == 'new':
                        return True
            else:
                if found == True:
                    print()
                    print("Found a match!\n\nYou're number " + str(curDraw))
                    print()
                else:
                    print()
                    print("Bad draw. No Match.\n\nYou're number " + str(curDraw))
                    print()


runGame = True
while runGame == True:
    runGame = playGame()