"""
Stack.py 
The {@code Stack} class represents a last-in-first-out (LIFO) stack of generic items.
 *  It supports the usual <em>push</em> and <em>pop</em> operations, along with methods
 *  for peeking at the top item, testing if the stack is empty, and iterating through
 *  the items in LIFO order.
 This implementation uses a singly linked list with a static nested class for
 *  linked-list nodes
 The <em>push</em>, <em>pop</em>, <em>peek</em>, <em>size</em>, and <em>is-empty</em>
 *  operations all take constant time in the worst case.
 """

class Stack:

    class _Node:

        def __init__(self, _item=None, _next=None):
            self._item = _item 
            self._next = _next 

        def __str__(self):
            return f"<_Node(_item={self._item}, _next={self._next})>"

        def __repr(self):
            return str(self)

    def __init__(self, first=None):
        self.first = first
        self.n = 0 

    def is_empty(self):
        return self.first == None 

    def size(self):
        return self.n 

    def push(self, item):
        oldfirst = self.first 
        self.first = Stack._Node()
        self.first._item = item 
        self.first._next = oldfirst 
        self.n += 1 

    def pop(self):
        if self.is_empty(): raise Exception('Stack underflow')
        item = self.first._item  # save item to return 
        self.first = self.first._next   # delete first node
        self.n -= 1 
        return item  # return saved item 

    def peek(self):
        if self.is_empty(): raise Exception('Stack underflow')
        return self.first._item

    def __str__(self):
        return f"<Stack(first={self.first}, n={self.n})>"

    def __repr(self):
        return str(self)

    def __iter__(self):
        a = []
        for i in range(self.n):
            a.append(self)
        return iter(a)

def main():
    stack = Stack()
    stack.push('A')
    stack.push('B')
    stack.push('C')
    print(stack)

    print(stack.peek())
    print(stack.size())
    stack.pop()
    for i in stack:
        print(i)
main()











