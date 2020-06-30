"""
ArrayQueueOfStrings.py 
Implements a queue using a Python list instead of a 
linked list data type. 
"""

class ArrayQueueOfStrings:

    def __init__(self):
        self._q = list()
        self._head = 0  
        self._tail = -1 
        self._N = 0

    def enqueue(self, item: str):
        self._q.insert(self._head, item)
        self._N += 1
        return 

    def dequeue(self) -> str:
        item = self.q[self._tail]
        del self.q[self._tail]
        self._N -= 1 
        return item

    def is_empty(self):
        return self._N == 0
