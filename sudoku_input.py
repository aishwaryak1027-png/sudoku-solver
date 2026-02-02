# sudoku_input.py
# Allows user to enter a custom Sudoku board

def get_user_board():
    print("\nEnter Sudoku board (use 0 for empty cells)")
    print("Enter 9 numbers per row separated by space")

    board = []

    for i in range(9):
        while True:
            row = input(f"Row {i+1}: ")
            nums = row.split()

            if len(nums) == 9 and all(n.isdigit() and 0 <= int(n) <= 9 for n in nums):
                board.append([int(n) for n in nums])
                break
            else:
                print("❌ Invalid row. Enter exactly 9 numbers (0–9).")

    return board

