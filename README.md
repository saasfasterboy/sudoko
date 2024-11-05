Sudoku Project README
Overview
This project consists of two main components: a Sudoku puzzle generator that creates Sudoku puzzles of various difficulty levels and a Sudoku solver that can solve any valid Sudoku puzzle.

Components
1. Sudoku Puzzle Generator
The Sudoku puzzle generator creates Sudoku boards and removes numbers to create puzzles with varying difficulty. It generates valid Sudoku puzzles and supports difficulty levels such as Easy, Medium, Hard, and Extreme.



2. Sudoku Solver
The Sudoku solver takes a partially filled Sudoku board and solves it using a backtracking algorithm. It can solve Sudoku puzzles of any configuration.



Installation
To run this project, ensure you have Python installed. Clone the repository and install any required libraries.

Running the Code
Generate Sudoku Puzzles
Instantiate the SudokuGenerator class, call the fill_board() method, and then use remove_numbers() to create a puzzle of the desired difficulty level.

Solve Sudoku Puzzles
Create an instance of the Solution class and call the solveSudoku() method, passing in a 2D list representing the Sudoku board.

Example
Generate an extreme Sudoku puzzle and then solve it using the respective classes.

Conclusion
This project provides a functional Sudoku puzzle generator and solver that can be extended or modified for additional features.
