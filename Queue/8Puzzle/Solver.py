"""
Solver.py
class Solver, finds a solution to the initial board
"""
from typing import * 
from Board import Board

class Solver:

    def __init__(self, initial: Board):
        pass 

    def is_solvable(self) -> bool:
        pass 

    def moves(self) -> int:
        pass 

    def __str__(self):
        return f''


def main():
    # 0 represents a blank square. 
    # output:
        # - a sequence of board positions that solves the puzzle in the fewest number of moves. 
        # - print out the total number of moves 
        # - the total number of states ever enqueued
    initial = [[0, 1, 3], [4, 2, 5], [7, 8, 6]]
    b = Board(initial)
    s = Solver(b)

if __name__ == '__main__':
    main()

# state of the game to be the board position, the number of moves made to reach the board position, and the previous state









