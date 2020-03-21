"""
LinkedStackOfStrings.py 
Implements a last-in-first-out (LIFO) stack of strings
and uses an inner Node class for linked list nodes. 
"""

class LinkedStackOfStrings:
    _first = None 

    class _Node:
        item = ""
        _next = None 

    def is_empty(self) -> bool:
        return self.first == None 

    def push(self, item: str):
        oldfirst = self._first
        first = LinkedStackOfStrings._Node()
        first.item = item 
        first._next = oldfirst

    def pop(self) -> str:
        item = self._first.item 
        self._first = self._first.next
        return item  
