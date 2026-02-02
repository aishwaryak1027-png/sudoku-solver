# main.py
# -------------------------------------------------
# Main file for running the Sudoku Solver project.
# Provides menu-based interaction for the user.
# -------------------------------------------------

import time
from solver import solve, print_board
from boards import easy_board, medium_board, hard_board
from sudoku_input import get_user_board


def main_menu():
    print("\n====== SUDOKU SOLVER MENU ======")
    print("1. Use predefined Sudoku board")
    print("2. Enter custom Sudoku board")
    print("3. Exit")
    print("================================")


while True:
    main_menu()
    choice = input("Enter your choice (1/2/3): ")

    # OPTION 1: Predefined boards
    if choice == "1":
        print("\nChoose difficulty:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")

        diff = input("Enter 1/2/3: ")

        if diff == "1":
            board = easy_board
        elif diff == "2":
            board = medium_board
        elif diff == "3":
            board = hard_board
        else:
            print("❌ Invalid difficulty choice")
            continue

    # OPTION 2: User input board
    elif choice == "2":
        board = get_user_board()

    # OPTION 3: Exit
    elif choice == "3":
        print("👋 Exiting Sudoku Solver. Thank you!")
        break

    else:
        print("❌ Invalid menu choice")
        continue

    # Show unsolved board
    print("\n📌 Unsolved Sudoku:\n")
    print_board(board)

    print("\n⏳ Solving...\n")
    time.sleep(1)

    # Solve and show result
    if solve(board):
        print("✅ Sudoku Solved Successfully!\n")
        print_board(board)
    else:
        print("❌ No solution exists for this Sudoku")
