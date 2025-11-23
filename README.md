# XO Conversational Command-Line Tic-Tac-Toe

## Introduction

This Python program simulates a simple, interactive **Tic-Tac-Toe** (Noughts and Crosses) game designed for two players on the command line. The code uses a friendly and informal tone in its output, making the classic game more engaging.

The project is an excellent demonstration of **fundamental Python programming concepts**, including: procedural programming, list manipulation, basic win condition checking, and robust input validation using `try...except` blocks. It provides a simple, self-contained example for beginners to practice game logic. 

---

## Setup Instructions

### Prerequisites

- **Python 3.x** installed on your system.

### Installation

1. Copy the full Python code into a file named `tic_tac_toe.py`.
2. Ensure the file is saved in a directory you can access via the terminal.

### Running the Game

- Open a terminal or command prompt.
- Navigate to the directory containing `tic_tac_toe.py`.
- Run the program:
    ```bash
    python tic_tac_toe.py
    ```
- Follow the on-screen prompts to place your mark on the board by typing a number from **1 to 9**.

---

## Code Details

### `tic_tac_toe.py` (Main Application File)

| Function/Variable | Description |
| :--- | :--- |
| **`board`** | A simple list of 9 elements (`[" " for _ in range(9)]`) that represents the 3x3 game board. |
| **`show_board()`** | Prints the current state of the board in a nicely formatted grid to the terminal, complete with section dividers. |
| **`did_someone_win(player)`** | Contains the core logic for checking all **8 possible winning combinations** (rows, columns, diagonals) for the given player ('X' or 'O'). |
| **`play_game()`** | The main game loop that manages turns, handles user input (1-9), validates moves (spot taken, number out of range), and breaks the loop when a win or draw occurs. |

---

## Design Highlights

* **Procedural Structure:** The code is organized into simple, clear functions for readability and ease of understanding.
* **Robust Input Validation:** Uses `try...except` to catch non-numeric input (`ValueError`) and includes checks for moves outside the 1-9 range and for selecting an occupied spot.
* **Conversational Tone:** The print statements are designed to be friendly and informal ("LETS GOOOO {turn} WINS!!! absolute legend").
* **Efficient Win Check:** All possible win states are checked efficiently in a single loop using a list of winning coordinate tuples.

---

## Future Enhancements

* Convert the game to use **Object-Oriented Programming (OOP)** with dedicated `Game` and `Player` classes.
* Implement an **AI opponent** using the **Minimax algorithm** to make the game single-player compatible
