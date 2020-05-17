"""
MinPQ.py 
Generic min priority queue implementation with a binary heap.
It supports the usual <em>insert</em> and <em>delete-the-minimum</em>
 *  operations, along with methods for peeking at the minimum key,
 *  testing if the priority queue is empty, and iterating through
 *  the keys.

Time and Space Complexity 
# Algorithm             Average             Worst case
 insert                 Theta(log n)
 delete-the-minimum     Theta(log n)
 min                                        Theta(1)
 size                                       Theta(1)
 is-empty                                   Theta(1)
"""
from Item import Item

class MinPQ:
    
    def __init__(self):
        """ initializes and empty priority queue"""
        self.pq = []
        self.build_heap(self.pq)
    
    def __len__(self):
        return len(self.pq) - 1

    def is_empty(self):
        """ Returns true if this priority queue is empty."""
        return self.size() == 1 

    def size(self):
        """ Returns the number of keys on this priority queue."""
        return len(self) 

    def min(self):
        """ Returns a smallest key on this priority queue."""
        if self.is_empty(): raise Exception('Priority Queue underflow.')
        return self.pq[1]
    
    def insert(self, x):
        """ Adds a new item to this priority queue."""
        self.pq.append(x)
        self.swim()

    def del_min(self):
        """ Removes and returns a smallest key on this priority queue"""
        if self.is_empty(): raise Exception('Priority Queue underflow.')
        _min = self.min()
        self.pq[1] = self.pq[len(self)]
        self.pq.pop()
        self.sink(1)
        assert self.is_min_heap()
        return _min 

    def build_heap(self, alist):
        i = len(alist) // 2
        self.pq = [0] + alist
        while i > 0:
            self.sink(i)
            i = i - 1

    # ***************************************************************************
    # * Helper functions to restore the heap invariant.
    # ***************************************************************************

    def swim(self):
        i = len(self)
        while i // 2 > 0 and self.greater(i//2, i):
            self.exch(i//2, i)
            i = i//2

    def sink(self, i):
        while i * 2 <= len(self):
            mc = self.min_child(i)
            if self.greater(i, mc):
                self.exch(i, mc)
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > len(self):
            return i * 2

        if self.pq[i * 2] < self.pq[i * 2 + 1]:
            return i * 2

        return i * 2 + 1

    # ***************************************************************************
    #  Helper functions for compares and swaps.
    # ***************************************************************************

    def greater(self, i, j):
        pq = self.pq 
        return pq[i] > pq[j]

    def exch(self, i, j):
        pq = self.pq
        pq[i], pq[j] = pq[j], pq[i]
    
    def is_min_heap(self):
        pq, n = self.pq, len(self)
        for i in range(n):
            if pq[i] is None: return False 
        for i in range(n+1, len(pq)):
            if pq[i] is not None: return False 
        if pq[1] is not None: return False 
        return self.is_min_heap_ordered(1)

    def is_min_heap_ordered(self, i):
        n = len(self) 
        if i > n: return True 
        left, right = 2 * i, 2 * i + 1 
        if left <= n and self.greater(i, left): return False 
        if right <= n and self.greater(i, right): return False 
        return self.is_min_heap_ordered(left) and self.is_min_heap_ordered(right)

    def __repr__(self):
        return f'<MinPQ(pq={self.pq}, n={len(self)})>'

    def __iter__(self):
        yield from self.pq

# def main():
#     keys = [9, 5, 6, 2, 3]
#     pq = MinPQ()
   
#     for key in keys:
#         print(key)
#         pq.insert(key)
#         if not pq.is_empty(): print(pq.del_min(), ' ')
#         print(f'Is min heap ordered: {pq.is_min_heap_ordered(key)}')
#     print(pq)
#     print(f'( {pq.size()} left on pq.')


# if __name__ == '__main__':
#     print(main())




