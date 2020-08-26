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

    def is_empty(self):
        return self._first is None

    def push(self, item):
        old_first = self._first
        first = LinkedStackOfStrings._Node()
        first.item = item
        first._next = old_first

    def pop(self):
        item = self._first.item
        self._first = self._first.next
        return item
