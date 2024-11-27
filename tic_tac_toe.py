import math
def create_board():
    return [[' ' for i in range(3)] for i in range(3)]

def print_board(board):
    for row in board:
        print('|'.join(row))
        print(5*'-')

def is_moves_left(board):
    for row in board:
        if ' ' in row:
            return True
    return False

def evaluate(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return -10 if row[0] == 'X' else 10
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return -10 if board[0][col] == 'X' else 10
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return -10 if board[0][0] == 'X' else 10
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return -10 if board[0][2] == 'X' else 10
    
    return 0

def minimax(board,depth,is_maximizing):
    score = evaluate(board)

    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if not is_moves_left(board):
        return 0
    
    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = max(best, minimax(board,depth+1,False))
                    board[i][j] = ' '
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best = min(best,minimax(board,depth+1,True))
                    board[i][j] = ' '
        return best

def best_move(board):
    best = -math.inf
    move = (-1,-1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board,0,False)
                board[i][j] = ' '
                if score > best:
                    move = (i,j)
                    best = score
    return move

def play_area():
    board = create_board()
    print_board(board)
    while True:
        print("Your move: ")
        i,j = map(int,input().split())
        if board[i][j] != ' ':
            print("The position is already occupied. Please re-enter a valid move")
            continue
        board[i][j] = 'X'
        print_board(board)
        if evaluate(board) == -10:
            print("You win!!")
            break
        if not is_moves_left(board):
            print("It's a Draw")
            break
        
        print("AI's move:")
        ai_move = best_move(board)
        
        board[ai_move[0]][ai_move[1]] = 'O'

        print_board(board)

        if evaluate(board) == 10:
            print("AI wins!!")
            break
        if not is_moves_left(board):
            print("It's a draw")
            break

play_area()