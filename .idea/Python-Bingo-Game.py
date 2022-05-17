#Timothy Leatau
#Bingo Game

def bingo_board():
    board = {
        "B": [],"I": [],"N": [],"G": [],"O": [],
        "I": [],
        "N": [],
        "G": [],
        "O": [],
    }
    min = 1
    max = 15
    for letter in board:
        board[letter] = random.sample(range(min, max), 5)
        min += 15
        max += 15
        if letter == "N":
            board[letter][2] = "X" # free space!
    return board