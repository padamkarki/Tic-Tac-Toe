
def display_board(board):
    print('\n'*100)
    print(board[7] +"|"+ board[8] +"|"+ board[9])
    print("-----")
    print(board[4] +"|"+ board[5] +"|"+ board[6])
    print("-----")
    print(board[1] +"|"+ board[2] +"|"+ board[3])

# test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)

def player_input():
    return (p1,p2)