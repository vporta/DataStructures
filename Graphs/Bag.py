"""
The {@code Bag} class represents a bag (or multiset) of 
 *  generic items. It supports insertion and iterating over the 
 *  items in arbitrary order.
 *  <p>
 *  This implementation uses a singly linked list with a static nested class Node.
"""

class Bag:

    def __init__(self, first=None):
        self.first = first 
        self.n = 0 

    class _Node:
        def __init__(self, item=None, next=None):
            self.item = item 
            self.next = next 

        def __repr__(self):
            return f'<_Node(item = {self.item}, next = {self.next})>'

    def __iter__(self):
        head = self.first 
        while head:
            yield head 
            head = head.next 

    def is_empty(self):
        return self.first == None 

    def size(self):
        return self.n 

    def add(self, item):
        oldfirst = self.first 
        self.first = Bag._Node()
        self.first.item = item 
        self.first.next = oldfirst
        self.n += 1 

    def __repr__(self):
        return f'<Bag(first = {self.first}, n = {self.n})>'
