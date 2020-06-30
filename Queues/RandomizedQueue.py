"""
RandomizedQueue.py
Generic ADT for a randomized queue
A randomized queue is similar to a stack or queue, except that the item removed is chosen uniformly at random from items in the data structure.
"""
from Item import Item
import random as r 

class RandomizedQueue:

    def __init__(self):
        self._q = list()
        self._head = 0  
        self._tail = -1 
        self._N = 0

    def is_empty(self) -> bool:
        return self._N == 0 

    def add(self, item: Item):
        if item is None: raise ValueError('Illegal Argument. Item cannot be None.')
        self._q.insert(self._head, item)
        self._N += 1
        return 

    def remove(self) -> Item:
        if self.is_empty(): raise ValueError('No Such Element Exists. RandomizedQueue is empty.')
        item = r.choice(self._q) 
        index = self._q.index(item) 
        del self._q[index]
        self._N -= 1 
        return item

    def size(self) -> int:
        return self._N

    def __repr__(self):
        return f"<RandomizedQueue(_q={self._q}, _N={self._N})>"

    def __iter__(self):
        return iter(self._q)

def main():
    r = RandomizedQueue()
    print(r)
    r.add(Item('One', 10))
    r.add(Item('Two', 10))
    r.add(Item('Three', 10))
    r.add(Item('Four', 10))
    r.add(Item('Five', 10))
    print(r)
    r.remove()
    print(r)
    for item in r:
        print(f'item: {item}')

if __name__ == '__main__':
    main()