# solver.py
# Backtracking Sudoku Solver

def find_empty(board):
    """Find an empty cell in the board (marked as 0)."""
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col  # row, col of empty cell
    return None  # no empty cells


def is_valid(board, num, pos):
    """Check if placing 'num' at position 'pos' is valid."""
    row, col = pos

    # Check row
    for c in range(9):
        if board[row][c] == num:
            return False

    # Check column
    for r in range(9):
        if board[r][col] == num:
            return False

    # Check box (3x3)
    box_x = col // 3
    box_y = row // 3

    for r in range(box_y * 3, box_y * 3 + 3):
        for c in range(box_x * 3, box_x * 3 + 3):
            if board[r][c] == num:
                return False

    return True


def solve(board):
    """Solve the Sudoku using backtracking."""
    empty = find_empty(board)
    if not empty:
        return True  # solved
    row, col = empty

    for num in range(1, 10):  # numbers 1 to 9
        if is_valid(board, num, (row, col)):
            board[row][col] = num  # try placing it

            if solve(board):  # recursive call
                return True

            board[row][col] = 0  # reset (backtrack)

    return False


def print_board(board):
    """Nicely print the sudoku board."""
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - -")

        for col in range(9):
            if col % 3 == 0 and col != 0:
                print(" | ", end="")

            print(board[row][col], end=" ")
        print()
