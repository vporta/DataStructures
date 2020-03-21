"""
Queue.py 
A generic queue. 
*  The {@code Queue} class represents a first-in-first-out (FIFO)
 *  queue of generic items.
 *  It supports the usual <em>enqueue</em> and <em>dequeue</em>
 *  operations, along with methods for peeking at the first item,
 *  testing if the queue is empty, and iterating through
 *  the items in FIFO order.
 *  <p>
 *  This implementation uses a singly linked list with a static nested class for
 *  linked-list nodes
 The <em>enqueue</em>, <em>dequeue</em>, <em>peek</em>, <em>size</em>, and <em>is-empty</em>
  *  operations all take constant time in the worst case.
"""


class Queue:
    
    class _Node:
        def __init__(self, _item=None, _next=None):
            self._item = _item 
            self._next = _next

        def __repr__(self):
            return return f"<_Node(_item={self._item}, _next={self._next})>"

    def __init__(self, first=None, last=None):
        self.first = first 
        self.last = last 
        self.n = 0 

    def is_empty(self):
        return self.first == None 

    def size(self):
        return self.n

    def peek(self):
        if self.is_empty(): raise Exception('No such element') 
        return self.first._item

    def enqueue(self, item):
        oldlast = self.last
        self.last = Queue._Node()
        self.last._item = item 
        self.last._next = None 
        if self.is_empty(): 
            self.first = self.last 
        else: 
            oldlast._next = self.last  
        self.n += 1

    def dequeue(self):
        if self.is_empty(): raise Exception('Queue underflow')
        item = self.first._item 
        self.first = self.first._next 
        self.n -= 1 
        if self.is_empty(): self.last = None 
        return item 

    def __repr__(self):
        return f"<Queue(first={self.first}, last={self.last}, n={self.n})>"

    def __iter__(self):
        a = []
        for i in range(self.n):
            a.append(self)
        return iter(a)


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
main()







