import math

# Initial empty board
board = [' ' for _ in range(9)]
player = ''
ai = ''

# Print the board
def print_board():
    print()
    for i in range(3):
        row = '|'.join(board[i * 3:(i + 1) * 3])
        print(f" {row} ")
        if i < 2:
            print("---|---|---")
    print()

# Check if a player has won
def check_winner(brd, ch):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    return any(all(brd[pos] == ch for pos in combo) for combo in win_combinations)

# Check for a draw
def is_draw(brd):
    return ' ' not in brd

# Minimax without pruning
def minimax(brd, is_maximizing):
    if check_winner(brd, ai):
        return 1
    if check_winner(brd, player):
        return -1
    if is_draw(brd):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = ai
                score = minimax(brd, False)
                brd[i] = ' '
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = player
                score = minimax(brd, True)
                brd[i] = ' '
                best_score = min(best_score, score)
        return best_score

# Determine the best move for AI
def best_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = ai
            score = minimax(board, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

# Main game loop
def play_game():
    global player, ai
    print("Welcome to Tic-Tac-Toe!")
    player = input("Choose your symbol (X or O): ").upper()

    while player not in ['X', 'O']:
        player = input("Invalid choice. Choose X or O: ").upper()

    ai = 'O' if player == 'X' else 'X'
    turn = 'X'  # X always starts

    print_board()

    while True:
        if turn == player:
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                if board[move] != ' ' or move < 0 or move > 8:
                    print("Invalid move. Try again.")
                    continue
                board[move] = player
            except (ValueError, IndexError):
                print("Please enter a number between 1 and 9.")
                continue
        else:
            print("AI is thinking...")
            move = best_move()
            board[move] = ai
            print(f"AI chose position {move + 1}")

        print_board()

        if check_winner(board, turn):
            print("You win!" if turn == player else "AI wins!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

        turn = ai if turn == player else player

if __name__ == "__main__":
    play_game()
