"""
ResizingArrayStack.py
 *  Stack implementation with a resizing array.
 *  The ResizingArrayStack class represents a last-in-first-out (LIFO) stack
 *  of generic items.
 *  It supports the usual push and pop operations, along with methods
 *  for peeking at the top item, testing if the stack is empty, and iterating through
 *  the items in LIFO order.
 *
 *  This implementation uses a resizing array, which double the underlying array
 *  when it is full and halves the underlying array when it is one-quarter full.
 *  The push and pop operations take constant amortized time.
 *  The size, peek, and is-empty operations takes
 *  constant time in the worst case.
"""


class ResizingArrayStack:

    def __init__(self):
        self._a = [None]
        self._n = 0

    def is_empty(self):
        return self._n == 0

    def size(self):
        return self._n

    def _resize(self, capacity):
        assert capacity >= self._n
        copy = [None] * capacity
        for i in range(self._n):
            copy[i] = self._a[i]
        self._a = copy

    def push(self, item):
        if self._n == len(self._a):
            self._resize(2 * len(self._a))
        self._a[self._n] = item
        self._n += 1

    def pop(self):
        if self.is_empty():
            raise ValueError('Stack underflow')
        item = self._a[self._n - 1]
        self._a[self._n - 1] = None  # to avoid loitering
        self._n -= 1

        # shrink the size of the list if necessary
        if self._n > 0 and self._n == len(self._a) // 4:
            self._resize(len(self._a) // 2)
        return item

    def peek(self):
        if self.is_empty():
            raise ValueError('Stack underflow')
        return self._a[self._n - 1]

    def __iter__(self):
        i = self._n - 1
        while i >= 0:
            item = self._a[i]
            yield item
            i -= 1


