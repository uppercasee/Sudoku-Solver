#!/usr/bin/env python3
### Sudoku Solver
import time

class SudokuSolver():
    def __init__(self):
        """ our puzzle is a nested list (list of lists), where each inner list is a row in our sudoku puzzle """
        self.board = [[0,6,0,1,0,4,0,5,0],
                      [0,0,8,3,0,5,6,0,0],
                      [2,0,0,0,0,0,0,0,1],
                      [8,0,0,4,0,7,0,0,6],
                      [0,0,6,0,0,0,3,0,0],
                      [7,0,0,9,0,1,0,0,4],
                      [5,0,0,0,0,0,0,0,2],
                      [0,0,7,2,0,6,9,0,0],
                      [0,4,0,5,0,8,0,7,0]]

    def printBoard(self, board):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - ")
            for j in range(9):
               if j % 3 == 0 and j != 0:
                   print("| ", end="")
               if j == 8 and board[i][j] != 0:
                   print(board[i][j])
               elif j == 8 and board[i][j] == 0:
                   print(". ")
               elif board[i][j] == 0:
                    print(". ", end="")
               else:
                   print(str(board[i][j]) + " ", end="")

    def findEmpty(self, board):
        """finds the next row, col on the puzzle that's not filled yet --> rep with 0 

        Args:
            board (list): our puzzle is a nested list (list of lists), where each inner list is a row in our sudoku puzzle

        Returns:
            int/None: row, col tuple (or (None, None) if there is none)
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return (i, j)  # row, col
        return None, None


    def isValid(self, board, guess, row, col):
        rowVals = board[row]
        if guess in rowVals:
            return False

        # colVals = [board[i][col] for i in range(9)]
        colVals = [board[i][col] for i in range(9)]
        if guess in colVals:
            return False

        rowStart = (row // 3) * 3
        colStart = (col // 3) * 3

        for r in range(rowStart, rowStart+3):
            for c in range(colStart, colStart+3):
                if board[r][c] == guess:
                    return False

        return True



    def solver(self, board):
        """solve sudoku using backtracking!
         mutates puzzle to be the solution (if solution exists)

        Args:
            board (nested list): our puzzle is a nested list (list of lists), where each inner list is a row in our sudoku puzzle

        Returns:
            bool: whether a solution exists or not
        """
        row, col = self.findEmpty(board)
        # step 1.1: if there's nowhere left, then we're done because we only allowed valid inputs
        if row is None:  # this is true if our findEmpty function returns None, None
            return True 
        # step 2: if there is a place to put a number, then make a guess between 1 and 9
        for guess in range(1, 10): # range(1, 10) is 1, 2, 3, ... 9
            # step 3: check if this is a valid guess
            if self.isValid(board, guess, row, col):
                # step 3.1: if this is a valid guess, then place it at that spot on the puzzle
                board[row][col] = guess
                # self.printBoard(board)
                # time.sleep(0.1)
                # print("\n")
                # step 4: then we recursively call our solver!
                if self.solver(board):
                    return True
            # step 5: it not valid or if nothing gets returned true, then we need to backtrack and try a new number
            board[row][col] = 0


if __name__ == "__main__":
    start = time.process_time()
    sudSol = SudokuSolver()
    print("The initial board is: ")
    sudSol.printBoard(sudSol.board)
    sudSol.solver(sudSol.board)
    print("The final board is: ")
    sudSol.printBoard(sudSol.board)
    print(f"The total time to solve the puzzle is {time.process_time() - start}")

