"""
LinkedQueue.py
 *  A generic queue, implemented using a singly linked list.
 *  The LinkedQueue class represents a _first-in-_first-out (FIFO)
 *  queue of generic items.
 *  It supports the usual enqueue and dequeue
 *  operations, along with methods for peeking at the _first item,
 *  testing if the queue is empty, and iterating through
 *  the items in FIFO order.
 *
 *  This implementation uses a singly linked list with a non-static nested class
 *  for linked-list nodes.  See Queue for a version that uses a static nested class.
 *  The enqueue, dequeue, peek, size, and is-empty
 *  operations all take constant time in the worst case.
"""


class Node:
    def __init__(self):
        self._item = None
        self._next = None

    def __repr__(self):
        return f"<Node(_item={self._item}, _next={self._next})>"


class LinkedQueue:

    def __init__(self):
        self._first = None
        self._last = None
        self._n = 0

    def is_empty(self):
        return self._first is None

    def size(self):
        return self._n

    def peek(self):
        if self.is_empty():
            raise Exception('No such element')
        return self._first._item

    def enqueue(self, item):
        old_last = self._last
        self._last = Node()
        self._last._item = item
        self._last._next = None
        if self.is_empty():
            self._first = self._last
        else:
            old_last._next = self._last
        self._n += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queues underflow')
        item = self._first._item
        self._first = self._first._next
        self._n -= 1
        if self.is_empty(): self._last = None
        return item

    def __repr__(self):
        return "".join([f'{item} ' for item in self])

    def __len__(self):
        return self.size()

    def __iter__(self):
        current = self._first
        while current is not None:
            yield current._item
            current = current._next


