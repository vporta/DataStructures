"""
ArrayStackOfStrings.py 
Implements a last-in-first-out (LIFO) stack of strings
and uses an array. 
"""

class ArrayStackOfStrings:

    def __init__(self):
        self._s = list()
        self._N = 0

    def is_empty(self) -> bool:
        return self._N == 0 

    def push(self, item: str):
        self._s.append(item)
        self._N += 1 

    def pop(self) -> str:
        item = self._s[self._N-1]
        self._N -= 1 
        return item 
