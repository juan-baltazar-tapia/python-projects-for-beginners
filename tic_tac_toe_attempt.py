MOVES = [[],[],[]]
LINE = '---+---+---'
board = [
  [0,0,0],
  [0,0,0],
  [0,0,0]
]
board_marks = [
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' '],
]

def get_user_input(turn, rc):
    turn = 'X' if turn % 2 == 0 else 'O'
    while True:
        print(f"Player {turn}'s turn")
        try:
            user_input = int(input(f"Enter {rc} (0-2): "))
            if user_input < 0 or user_input > 2:
                print("Invalid input")
                continue
            return user_input
        except ValueError:
            print("Invalid Input!")

def display_board(b):
    print(LINE)
    for row in b:
        print(f' {row[0]} | {row[1]} | {row[2]}')
        print(LINE)
    return

def check_for_winner(b):
    diagonal = b[0][0] + b[1][1] + b[2][2]
    diagonal_2 = b[2][0] + b[1][1] + b[0][2]
    winner = False
    if diagonal == 3 or diagonal == -3 or diagonal_2 == 3 or diagonal_2 == 3:
        winner = True
    return any(sum(r) in {3, -3} for r in b) | winner

def check_for_tie(b):
    for row in b:
        for i in row:
            if i == 0:
                return False
    return True


def main():
    turn = 0
    while True:
        while True:
            row = get_user_input(turn, 'row')
            column = get_user_input(turn, 'column')
            if board[row][column] != 0:
                print("This spot is already taken")
                continue
            break
        board[row][column] = 1 if turn % 2 == 0 else -1
        board_marks[row][column] = "X" if turn % 2 == 0 else "O"
        display_board(board_marks)
        if check_for_winner(board):
            winner = "X" if turn == turn % 2 == 1 else "O"
            print(f"{winner} has won the game!")
            break
        if check_for_tie(board):
            print("TIE!")
            break
        print("TURN", turn)
        turn += 1

if __name__ == '__main__':
    main()

