# 🧩 Sudoku Solver – Minor Project

## 📌 Project Overview

This project is a **menu-driven Sudoku Solver** implemented using **Python**. It solves a 9×9 Sudoku puzzle using the **Backtracking algorithm**. The user can either select a predefined Sudoku board (Easy, Medium, Hard) or enter a custom Sudoku board manually.

This project is developed as a **Minor Project** and is designed to be easily extendable for a **Major Project** in the final semester.

---

## 🎯 Objectives

* To understand and implement the **Backtracking algorithm**
* To apply **modular programming** in Python
* To provide a **user-friendly, menu-based interface**
* To solve Sudoku puzzles efficiently

---

## 🛠️ Technologies Used

* **Programming Language:** Python 3
* **IDE:** Visual Studio Code
* **Concepts:** Recursion, Backtracking, Modular Programming

---

## 📂 Project Structure

```
SudokuProject/
│
├── main.py            # Main menu and program control
├── solver.py          # Sudoku solving logic (backtracking)
├── boards.py          # Predefined Sudoku boards
├── sudoku_input.py    # Custom Sudoku input from user
├── requirements.txt   # Project dependencies
└── README.md          # Project documentation
```

---

## ⚙️ How It Works

1. The user is shown a menu with options.
2. The user can:

   * Select a predefined Sudoku board
   * Enter a custom Sudoku board
   * Exit the program
3. The unsolved Sudoku is displayed.
4. The backtracking algorithm solves the puzzle.
5. The solved Sudoku is displayed.

---

## 🧠 Algorithm Used – Backtracking

* Find an empty cell in the Sudoku grid
* Try numbers from 1 to 9
* Check if the number is valid in:

  * Current row
  * Current column
  * 3×3 sub-grid
* If valid, place the number and move to the next cell
* If no number fits, backtrack and try a different number

---

## ▶️ How to Run the Project

1. Open the project folder in VS Code
2. Open the terminal
3. Run the command:

```bash
python main.py
```

---

## ✅ Features

* Menu-driven interface
* Predefined difficulty levels
* Custom Sudoku input
* Clean console output
* Modular and readable code

---

## 🔮 Future Enhancements (Major Project)

* Graphical User Interface (GUI)
* Image-based Sudoku input using OpenCV
* Timer and performance analysis
* Difficulty level detection
* Web or mobile application version

---

## 👩‍💻 Author

**Aishwarya Kannan**

---

## 📜 License

This project is for **educational purposes only**.
