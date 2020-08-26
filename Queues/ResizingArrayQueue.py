"""
ResizingArrayQueue.py
 *  Queue implementation with a resizing array.
 *  The ResizingArrayQueue class represents a first-in-first-out (FIFO)
 *  queue of generic items.
 *  It supports the usual enqueue and dequeue
 *  operations, along with methods for peeking at the first item,
 *  testing if the queue is empty, and iterating through
 *  the items in FIFO order.
 *  This implementation uses a resizing array, which doubles the underlying array
 *  when it is full and halves the underlying array when it is one-quarter full.
 *  The enqueue and dequeue operations take constant amortized time.
 *  The size, peek, and is-empty operations takes
 *  constant time in the worst case.
"""


class ResizingArrayQueue:

    def __init__(self):
        self._q = [None] * 2
        self._first = 0
        self._last = 0
        self._n = 0

    def is_empty(self):
        return self._first is None

    def size(self):
        return self._n

    def _resize(self, capacity):
        assert capacity >= self._n
        copy = [None] * capacity
        for i in range(self._n):
            copy[i] = self._q[(self._first + i) % len(self._q)]
        self._q = copy
        self._first = 0
        self._last = self._n

    def peek(self):
        if self.is_empty():
            raise Exception('No such element')
        return self._q[self._first]

    def enqueue(self, item):
        if self._n == len(self._q):
            self._resize(2 * len(self._q))
        self._q[self._last] = item
        self._last += 1
        if self._last == len(self._q):
            self._last = 0
        self._n += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queues underflow')
        item = self._q[self._first]
        self._q[self._first] = None
        self._n -= 1
        self._first += 1
        if self._first == len(self._q):
            self._first = 0
        if self._n > 0 and self._n == len(self._q) // 4:
            self._resize(len(self._q) // 2)
        return item

    def __repr__(self):
        return "".join([f'{item} ' for item in self])

    def __len__(self):
        return self.size()

    def __iter__(self):
        i = 0
        while i < self._n:
            item = self._q[(i + self._first) % len(self._q)]
            assert item is not None
            yield item
            i += 1


