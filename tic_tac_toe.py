
def display_board(board):
    print('\n'*100)
    print(board[7] +"|"+ board[8] +"|"+ board[9])
    print("-----")
    print(board[4] +"|"+ board[5] +"|"+ board[6])
    print("-----")
    print(board[1] +"|"+ board[2] +"|"+ board[3])

test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)

# Takes players input and stores
def player_input():
    marker = ""
    acceptable_mark =["X","O"]

    while marker != "X" and marker != "O":
        marker = input("Please choose your marker X or O: ").upper()

        # Check Validity
        if marker not in acceptable_mark:
            print("Please choose either X or O: ")

        #Assign input to V
        p1 = marker

        if p1 == "X":
            p2 = "O"
        else:
            p2 = "X"

    return (p1,p2)

p1_marker, p2_marker = player_input()

# Assigns it to the board
def place_marker(board,marker,position):
    board[position] = marker

place_marker(test_board,'$',8)
display_board(test_board)

# Win check
def win_check(board, mark):
    # all rows
    return ((board[1] == board[2] == board[3] == mark) or
    (board[4] == board[5] == board[6] == mark) or
    (board[7] == board[8] == board[9] == mark) or
    # all col
    (board[1] == board[4] == board[7] == mark) or
    (board[2] == board[5] == board[8] == mark) or
    (board[3] == board[6] == board[9] == mark) or
    # 2 diagnols
    (board[1] == board[5] == board[9] == mark) or
    (board[7] == board[5] == board[3] == mark))

display_board(test_board)
win_check(test_board,'X')


# Choose first player turn
import random
def choose_first():
    flip = random.randint(0,1)

    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"
    

def space_check(board,position):
    return board[position] == " "

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

