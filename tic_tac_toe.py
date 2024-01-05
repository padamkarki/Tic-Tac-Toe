
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

def player_choice(board):
    position = 0
    while position not in range(1,10) or not space_check(board, position):
        position = int(input("Please choose your position (1-9): "))
    return position

def replay():
    choice = input("Play again? Y or N: ").upper()
    return choice == "Y"

# MAIN PROGRAM

print("Welcome to TIC TAC TOE")

while True:
    the_board = [" "]*10
    p1_marker,p2_marker = player_input()

    turn = choose_first()
    print(turn + " will play first")

    play_game = input("Ready to play? y or n: ")
    if play_game == "y":
        game_on = True
    else:
        game_on = False

    # Game Play
    #while game_on:
    while game_on:

        # Player2's turn.
        if turn == "Player 1":
            #show board
            display_board(the_board)

            #choose position
            position = player_choice(the_board)

            #place marker on position
            place_marker(the_board, p1_marker, position)


            #check if won
            if win_check(the_board,p1_marker):
                display_board(the_board)
                print("Congrats Player 1, you won!")
                game_on = False
            else:
            #check if tie
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie Game")
                    game_on = False
            #no won, no tie, next player turn
                else:
                    turn = "Player 2"
        # Player2's turn.
        else:
            #show board
            display_board(the_board)

            #choose position
            position = player_choice(the_board)

            #place marker on position
            place_marker(the_board, p2_marker, position)



            #check if won
            if win_check(the_board,p2_marker):
                display_board(the_board)
                print("Congrats Player 2, you won!")
                game_on = False
            else:
            #check if tie
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie Game")
                    game_on = False
            #no won, no tie, next player turn
                else:
                    turn = "Player 1"

    if not replay():
        break


