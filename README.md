# SudokuSolver
Implemented a puzzle-solving AI which does not need a neural network.

The solver works by using two main functions: the explicit solver and implicit solver.
The explicit solver is a naive approach to solving the sudoku puzzle, but we complement it with the implicit solver - which determines the possible values by taking the neighboring values into consideration.

The explicit solver is based on three basic functions, which determine the possible values for a given cell:
1. check_horizontal: Checks the row for possible values
2. check_vertical: Checks the column for possible values
3. check_square: Checks the square for possible values

Wrapping up these functions together in get_poss_values, we can obtain a list of possible values for any given square by taking the intersection of the return sets from our three basic functions.

The explicit solver function iterates through every square and if it is empty (the value is 0), the solver tries to fill it in. That occurs if there is only one possible value based on the functions we previously described.

The explicit solver is a great naive approach but neglects information gained from surrounding squares. When we are examining a square that, for example, has possible values of 1, 2, and 3, if each other empty square in the row could only be 1 or 2, then we know that the square we are examining MUST be 3 through the process of elimination. The implicit solver function implements this logic by assembling the possible values of one square and comparing that to the possible values of the rest of the row, column, and 3x3 square.

Using the implicit solver in concert with the explicit solver allows us to solve medium and hard puzzles in seconds.
