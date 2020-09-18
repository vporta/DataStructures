"""
pqueues.py
A generic queue. 
 *  The pqueues class represents a first-in-first-out (FIFO)
 *  queue of generic items.
 *  It supports the usual enqueue and dequeue
 *  operations, along with methods for peeking at the first item,
 *  testing if the queue is empty, and iterating through the items in FIFO order.
 *  This implementation uses a singly linked list with a static nested class for linked-list nodes
 *  The enqueue, dequeue, peek, size, and is-empty operations all take constant time in the worst case.
"""


class Queue:
    
    class _Node:
        def __init__(self, _item=None, _next=None):
            self._item = _item 
            self._next = _next

        def __repr__(self):
            return f"<_Node(_item={self._item}, _next={self._next})>"

    def __init__(self):
        self._first = None
        self._last = None
        self._n = 0

    def is_empty(self):
        return self._first == None

    def size(self):
        return self._n

    def peek(self):
        if self.is_empty():
            raise Exception('No such element')
        return self._first._item

    def enqueue(self, item):
        old_last = self._last
        self._last = Queue._Node()
        self._last._item = item
        self._last._next = None
        if self.is_empty(): 
            self._first = self._last
        else: 
            old_last._next = self._last
        self._n += 1

    def dequeue(self):
        if self.is_empty(): raise Exception('pqueues underflow')
        item = self._first._item
        self._first = self._first._next
        self._n -= 1
        if self.is_empty():
            self._last = None
        return item 

    def __repr__(self):
        return f"<Queue(first={self._first}, last={self._last}, n={self._n})>"

    def __iter__(self):
        current = self._first
        while current is not None:
            yield current._item
            current = current._next


def main():
    queue = Queue()
    queue.enqueue('A')
    queue.enqueue('B')
    queue.enqueue('C')
    print(queue)
    # queue.dequeue()
    print(queue)
    print(queue.peek())
    print(queue.size())
    for i in queue:
        print(i.first._item)


if __name__ == '__main__':
    main()







