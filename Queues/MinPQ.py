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


class MinPQ:

    def __init__(self, _max=1):
        """ initializes an empty priority queue"""
        self._pq = [None for _ in range(_max+1)]
        # self.build_heap(self.pq)
        self._n = 0

    def is_empty(self):
        """ Returns true if this priority queue is empty."""
        return self._n == 0

    def size(self):
        """ Returns the number of keys on this priority queue."""
        return self._n

    def min(self):
        """ Returns a smallest key on this priority queue."""
        if self.is_empty():
            raise Exception('Priority Queues underflow.')
        assert self._pq is not None
        return self._pq[1]

    def insert(self, x):
        """ Adds a new item to this priority queue."""
        if self._n == len(self._pq) - 1:
            self.__resize(2 * len(self._pq))
        self._n += 1
        self._pq[self._n] = x
        self.__swim(self._n)

    def del_min(self):
        """ Removes and returns a smallest key on this priority queue"""
        if self.is_empty():
            raise Exception('Priority Queues underflow.')
        _min = self._pq[1]
        assert _min is not None
        self.exch(1, self._n)
        self._n -= 1
        self.__sink(1)
        self._pq[self._n + 1] = None
        if self._n > 0 and self._n == (len(self._pq) - 1) // 4:
            self.__resize(len(self._pq) // 2)
        return _min

    def __len__(self):
        return self.size()

    # ***************************************************************************
    # * Helper functions to restore the heap invariant.
    # ***************************************************************************

    def __swim(self, i):
        while i > 1 and self.greater(i // 2, i):
            self.exch(i, i // 2)
            i = i // 2

    def __sink(self, i):
        while i * 2 <= self._n:
            j = 2 * i

            if j < self._n and self.greater(j, j + 1):
                j += 1
            if not self.greater(i, j):
                break
            self.exch(i, j)
            i = j

    # ***************************************************************************
    #  Helper functions for compares and swaps.
    # ***************************************************************************

    def greater(self, i, j):
        pq = self._pq
        return pq[i] > pq[j]

    def exch(self, i, j):
        pq = self._pq
        pq[i], pq[j] = pq[j], pq[i]

    def __resize(self, capacity):
        temp = [None] * capacity
        for i in range(1, self._n + 1):
            temp[i] = self._pq[i]
        self._pq = temp

    def is_min_heap(self):
        pq, n = self._pq, len(self)
        for i in range(n):
            if pq[i] is None:
                return False
        for i in range(n + 1, len(pq)):
            if pq[i] is not None:
                return False
        if pq[1] is not None:
            return False
        return self.is_min_heap_ordered(1)

    def is_min_heap_ordered(self, i):
        n = len(self)
        if i > n:
            return True
        left, right = 2 * i, 2 * i + 1
        if left <= n and self.greater(i, left):
            return False
        if right <= n and self.greater(i, right):
            return False
        return self.is_min_heap_ordered(left) and self.is_min_heap_ordered(right)

    def __repr__(self):
        return f'<{self.__class__.__name__}(pq={self._pq}, n={len(self)})>'

    def __iter__(self):
        """Iterates over all the items in this priority queue in ascending
        order."""
        copy = MinPQ(self.size())
        for i in range(1, self._n + 1):
            copy.insert(self._pq[i])
        for i in range(1, copy._n + 1):
            yield copy.del_min()


def main():
    keys = [9, 5, 6, 2, 3]
    pq = MinPQ()

    for key in keys:
        print(key)
        pq.insert(key)
        if not pq.is_empty():
            print(pq.del_min(), ' ')
        print(f'Is min heap ordered: {pq.is_min_heap_ordered(key)}')
    print(pq)
    print(f'( {pq.size()} left on pq.')


if __name__ == '__main__':
    print(main())
