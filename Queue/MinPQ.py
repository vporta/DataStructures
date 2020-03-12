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
        self.n = len(self.pq) 


    def is_empty(self):
        """ Returns true if this priority queue is empty."""
        return self.n == 0 


    def size(self):
        """ Returns the number of keys on this priority queue."""
        return self.n 


    def min(self):
        """ Returns a smallest key on this priority queue."""
        if self.is_empty(): raise Exception('Priority Queue underflow.')
        return self.pq[0]
    
    def insert(self, x):
        """ Adds a new item to this priority queue."""
        self.pq.append(x)
        self.n += 1
        # self.pq.insert(self.n, x)
        self.swim(self.n)
        # assert self.is_min_heap()        

    def del_min(self):
        """ Removes and returns a smallest key on this priority queue"""
        if self.is_empty(): raise Exception('Priority Queue underflow.')
        _min = self.min()
        n = self.n
        n -= 1
        self.exch(0, n)
        self.sink(0)
        assert self.is_min_heap()
        return _min 


    # ***************************************************************************
    # * Helper functions to restore the heap invariant.
    # ***************************************************************************

    def swim(self, k):
        # current_value = self.pq[k]
        # parent_k, parent_value = self.__get_parent(k)
        # if k > 0 and self.compare(current_value, parent_value):
        #     self.pq[parent_index], self.pq[index] = current_value, parent_value
        #     self.__siftup(parent_index)
        # return
        parent = (k-1) // 2
        import pdb; pdb.set_trace()  # breakpoint 649c817a //
        while k > 0 and self.greater(parent, k):
            self.exch(k, parent)
            k = parent


    def sink(self, k):
        n = self.n
        while (2*k <= n):
            j = 2 * k 
            if j < n and self.greater(j, j + 1): 
                j += 1
            if not self.greater(k, j): 
                break 
            self.exch(k, j)
            k = j 


    # ***************************************************************************
    # * Helper functions for compares and swaps.
    # ***************************************************************************


    def greater(self, i, j):
        pq = self.pq 
        return pq[i] > pq[j]


    def exch(self, i, j):
        pq = self.pq
        pq[i], pq[j] = pq[j], pq[i]

    
    def is_min_heap(self):
        pq, n = self.pq, self.n
        for i in range(n):
            if pq[i] is None: return False 
        for i in range(n+1, len(pq)):
            if pq[i] is not None: return False 
        if pq[0] is not None: return False 
        return self.is_min_heap_ordered(0)


    def is_min_heap_ordered(self, k):
        n = self.n 
        if k > n: return True 
        left, right = 2 * k + 1, 2 * k + 2 
        if left <= n and self.greater(k, left): return False 
        if right <= n and self.greater(k, right): return False 
        return self.is_min_heap_ordered(left) and self.is_min_heap_ordered(right)




def main():
    keys = 'P Q E - X A M - P L E -'
    # keys = keys.replace(' ', '')
    # keys = [('A', 8), ('E', 3), ('B', 5), ('Z', 2)]
    pq = MinPQ()
    for i, key in enumerate(keys):
        print(key)
        if not key == '-': pq.insert(key)
        elif not pq.is_empty(): print(pq.del_min() + ' ')
        # print(f'Is min heap ordered: {pq.is_min_heap_ordered(key)}')
    print(f'( {pq.size()} left on pq.')
    
if __name__ == '__main__':
    print(main())




