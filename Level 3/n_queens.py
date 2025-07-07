def print_board(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print("\n")

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] or \
           (col - (row - i) >= 0 and board[i][col - (row - i)]) or \
           (col + (row - i) < n and board[i][col + (row - i)]):
            return False
    return True

def solve_n_queens(board, row, n, solutions):
    if row == n:
        solutions.append([r[:] for r in board])
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens(board, row + 1, n, solutions)
            board[row][col] = 0

def n_queens(n):
    board = [[0]*n for _ in range(n)]
    solutions = []
    solve_n_queens(board, 0, n, solutions)
    print(f"Total solutions: {len(solutions)}")
    for i, sol in enumerate(solutions, 1):
        print(f"Solution #{i}:")
        print_board(sol)
        
n_queens(8)