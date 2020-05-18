"""
Board.py 
Class Board, a N-by-N grid array.
"""
from typing import *
from queue import Queue


class Board:
    board = []

    def __init__(self, tiles):
        self.n = len(tiles[0])
        self.tiles = tiles
        self.board = [0 for _ in range(self.n) for j in range(self.n)]
        self.q = Queue()
        for i in range(self.n):
            for j in range(self.n):
                self.board[i * self.n + j] = tiles[i][j]

    def hamming(self) -> int:
        count = 0
        for i in range(self.n * self.n):  # compare board[1] through board[N^2-1] with goal
            if self.board[i] != i + 1 and self.board[i] != 0:
                count += 1
        return count

    def manhattan(self) -> int:
        manhattan_sum = 0
        for i in range(self.n * self.n):
            if self.board[i] != i + 1 and self.board[i] != 0:
                manhattan_sum += self._manhattan(self.board[i], i)
        return manhattan_sum

    def _manhattan(self, goal, current) -> int:
        # row + col
        return abs((goal - 1) // self.n - current // self.n) + abs((goal - 1) % self.n - current % self.n)

    def is_goal(self):
        for i in range(self.n * self.n - 1):
            if self.board[i] != i + 1: return False
        return True

    def swap(self, a, i, j):
        a.board[i], a.board[j] = a.board[j], a.board[i]

    def __eq__(self, y) -> bool:
        return self.board == y

    def neighbors(self):
        index = 0
        found = False
        neighbor = None

        for i in range(len(self.board)):
            if self.board[i] == 0:
                index = i
                found = True
                break

        if not found: return None
        if index // self.n != 0:  # if not first row
            neighbor = Board(self.board)
            self.swap(neighbor, index, index - self.n)  # exchange with upper block
            self.q.put(neighbor)

        if index // self.n != (self.n - 1):  # if not last row
            neighbor = Board(self.board)
            self.swap(neighbor, index, index + self.n)  # exchange with lower block
            self.q.put(neighbor)

        if (index % self.n) != 0:  # if not leftmost column
            neighbor = Board(self.board)
            self.swap(neighbor, index, index - 1)  # exchange with left block
            self.q.put(neighbor)

        if (index % self.n) != self.n - 1:  # if not rightmost column
            neighbor = Board(self.board)
            self.swap(neighbor, index, index + 1)  # exchange with left block
            self.q.put(neighbor)

        return self.q

    def __iter__(self):
        yield from self.neighbors()

    def __repr__(self):
        return f'<Board(n = {self.n}, board={self.board}, tiles = {self.tiles}, q = {str(self.q.queue)}>'

    # def __str__(self):
    #     return f'{self.board}'
