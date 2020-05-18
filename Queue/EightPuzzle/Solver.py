"""
Solver.py
class Solver, finds a solution to the initial board
"""
from typing import *
from Queue.EightPuzzle.Board import Board
from collections import deque
from Queue.MinPQ import MinPQ
from heapq import *

# initial state is the initial board, 0 moves, None previous state
# insert initial state into the priority queue
# Then, delete from the priority queue the state with the minimum priority
# insert onto the priority queue all neighboring states (those that can be reached in one move). 
# Repeat this procedure until the state dequeued is the goal state.


# A* algorithm 
# 1. GENERATE A LIST of all possible next steps 
#    towards goal from current position

# 2. STORE CHILDREN in priority queue 
#    based on distance to goal, closest first

# 3. SELECT CLOSEST child and REPEAT until goal reached or no more children 

# f(n)=g(n)+h(n)
# where,

# n = next node on the path

# g(n) = the cost of the path from the start node to n

# h(n) = a heuristic function that estimates the cost of the cheapest path from n to the goal


class Solver:
    goal = None

    class Node:
        moves = None
        board = None
        prev = None

        def __init__(self, initial):
            self.moves = 0
            self.board = initial
            self.prev = None

        def __lt__(self, other):
            pa = self.board.manhattan() + self.moves
            pb = other.board.manhattan() + other.moves
            if pa < pb:
                return -1

        def __gt__(self, other):
            pa = self.board.manhattan() + self.moves
            pb = other.board.manhattan() + other.moves
            if pa > pb:
                return 1

        def __eq__(self, other):
            pa = self.board.manhattan() + self.moves
            pb = other.board.manhattan() + other.moves
            if pa == pb:
                return 0

    def __init__(self, initial):

        pq = []
        twin_pq = []
        node = Solver.Node(initial)
        twin_node = Solver.Node(initial)
        heappush(pq, node)
        heappush(twin_pq, twin_node)

        _min = heappop(pq)
        twin_min = heappop(twin_pq)

        while not _min.board.is_goal() and not twin_min.board.is_goal():

            for b in _min.board.neighbors():
                if _min.prev is None or not b == _min.prev.board:
                    n = Solver.Node(b)
                    n.moves = _min.moves + 1
                    n.prev = _min
                    heappush(pq, n)

            for b in twin_min.board.neighbors():
                if twin_min.prev is None or not b.equals(twin_min.prev.board):
                    n = Solver.Node(b)
                    n.moves = twin_min.moves + 1
                    n.prev = twin_min
                    heappush(twin_pq, n)

            _min = heappop(pq)
            twin_min = heappop(twin_pq)

        if _min.board.is_goal():
            goal = _min
        else:
            goal = None

    def is_solvable(self):
        return self.goal is not None

    def moves(self):
        if not self.is_solvable():
            return -1
        else:
            return self.goal.moves

    def solution(self):
        if not self.is_solvable(): return None
        stack = deque()
        n = self.goal
        while n is not None:
            n = n.prev
            stack.append(n.board)
        return stack

    def __iter__(self):
        yield from self.solution()


def main():
    # 0 represents a blank square. 
    # output:
    # - a sequence of board positions that solves the puzzle in the fewest number of moves.
    # - print out the total number of moves
    # - the total number of states ever enqueued
    blocks = [[0, 1, 3], [4, 2, 5], [7, 8, 6]]
    # goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    initial = Board(blocks)
    solver = Solver(initial)
    print(solver)
    if not solver.is_solvable():
        print('Solution not possible')
    else:
        print(f'Minimum number of moves = {solver.moves()}')
        for board in solver.solution():
            print(board)


if __name__ == '__main__':
    main()

# state of the game to be the board position, the number of moves made to reach the board position, and the previous state
