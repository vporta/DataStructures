"""
LinkedStack.py
 *  A generic stack, implemented using a linked list. Each stack
 *  element is of type Item.
 *  The LinkedStack class represents a last-in-first-out (LIFO) stack of
 *  generic items.
 *  It supports the usual push and pop operations, along with methods
 *  for peeking at the top item, testing if the stack is empty, and iterating through
 *  the items in LIFO order.
 *
 *  This implementation uses a singly linked list with a non-static nested class for
 *  linked-list nodes. See Stack for a version that uses a static nested class.
 *  The push, pop, peek, size, and is-empty
 *  operations all take constant time in the worst case.
"""


class Node:
    def __init__(self):
        self._item = ""
        self._next = None


class LinkedStack:
    def __init__(self):
        self._first = None
        self._n = 0
        assert self._check()

    def is_empty(self):
        return self._first is None

    def size(self):
        return self._n

    def push(self, item):
        old_first = self._first
        self._first = Node()
        self._first._item = item
        self._first._next = old_first
        self._n += 1
        assert self._check()

    def pop(self):
        if self.is_empty():
            raise ValueError('Stack underflow')
        item = self._first._item
        self._first = self._first._next
        self._n -= 1
        assert self._check()
        return item

    def peek(self):
        if self.is_empty():
            raise ValueError('Stack underflow')
        return self._first._item

    def __str__(self):
        s = ''
        for item in self:
            s += item
        return s

    def __iter__(self):
        current = self._first
        while current is not None:
            item = current._item
            assert item is not None
            yield item
            current = current._next

    def _check(self):
        if self._n < 0:
            return False
        if self._n == 0:
            if self._first is not None:
                return False
        elif self._n == 1:
            if self._first is None:
                return False
            if self._first._next is not None:
                return False
        else:
            if self._first is None:
                return False
            if self._first._next is None:
                return False
        num_nodes = 0
        x = self._first
        while x is not None and num_nodes <= self._n:
            num_nodes += 1
            x = x._next
        if num_nodes != self._n:
            return False
        return True
