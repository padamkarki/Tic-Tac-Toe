
def display_board(board):
    print('\n'*100)
    print(board[7] +"|"+ board[8] +"|"+ board[9])
    print("-----")
    print(board[4] +"|"+ board[5] +"|"+ board[6])
    print("-----")
    print(board[1] +"|"+ board[2] +"|"+ board[3])


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