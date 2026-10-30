#Tic-Tac-Toe Game
# Human = X
# Computer = O

board = [' ' for _ in range(9)]


def display_board():
    print()
    print(" ", board[0], "|", board[1], "|", board[2])
    print("---+---+---")
    print(" ", board[3], "|", board[4], "|", board[5])
    print("---+---+---")
    print(" ", board[6], "|", board[7], "|", board[8])
    print()


def check_winner(player):
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == player and board[b] == player and board[c] == player:
            return True

    return False

def board_full():
    return ' ' not in board


def computer_move():
    # First try to win
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'

            if check_winner('O'):
                return

            board[i] = ' '

    # Then block the human
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'

            if check_winner('X'):
                board[i] = 'O'
                return

            board[i] = ' '

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            return


print("TIC-TAC-TOE")
print("Human = X")
print("Computer = O")

while True:

    display_board()

    # Human move
    while True:
        try:
            position = int(input("Enter your position (1-9): "))

            if position < 1 or position > 9:
                print("Enter a number between 1 and 9.")
            elif board[position - 1] != ' ':
                print("Position already occupied.")
            else:
                board[position - 1] = 'X'
                break

        except ValueError:
            print("Please enter a valid number.")

    if check_winner('X'):
        display_board()
        print("Human wins!")
        break

    if board_full():
        display_board()
        print("Game Draw!")
        break

    # Computer move
    computer_move()

    print("Computer made its move.")

    if check_winner('O'):
        display_board()
        print("Computer wins!")
        break

    if board_full():
        display_board()
        print("Game Draw!")
        break