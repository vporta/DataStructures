"""
Deque.py
A double-ended queue or deque (pronounced "deck") is a generalization of a stack and a queue that supports inserting and removing items from either the front or the back of the data structure.
"""
from Item import Item 

class Deque:

    def __init__(self):
        self._deque = list()
        self._head = 0
        self._tail = -1 
        self._N = 0 

    def is_empty(self) -> bool:
        return self._N == 0 

    def add_first(self, item: Item):
        if item is None: raise ValueError('Illegal Argument. Item cannot be None.')
        self._deque.insert(self._head, item)
        self._N += 1 
        return 

    def add_last(self, item: Item):
        if item is None: raise ValueError('Illegal Argument. Item cannot be None.')
        self._deque.insert(self._tail, item)
        self._N += 1 
        return 

    def remove_first(self) -> Item:
        if self.is_empty(): raise ValueError('No Such Element Exists. Deque is empty.')
        item = self._deque[self._head]
        del self._deque[self._head]
        self._N -= 1 
        return item 

    def remove_last(self) -> Item:
        if self.is_empty(): raise ValueError('No Such Element Exists. Deque is empty.')
        item = self._deque[self._tail]
        del self._deque[self._tail]
        self._N -= 1 
        return item 

    def __repr__(self):
        return f"<Deque(_deque={self._deque}, _N={self._N})>"

    def __iter__(self):
        return iter(self._deque)

def main():
    d = Deque()
    print(d)
    d.add_first(Item('One', 10))
    d.add_first(Item('Two', 10))
    d.add_first(Item('Three', 10))
    d.add_first(Item('Four', 10))
    d.add_first(Item('Five', 10))
    print(d)
    d.remove_first()
    print(d)
    d.remove_last()
    for item in d:
        print(f'item: {item}')

if __name__ == '__main__':
    main()