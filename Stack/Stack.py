"""
Stack.py 
The class represents a last-in-first-out (LIFO) stack of generic items.
 * It supports the usual push and pop operations, along with methods
 * for peeking at the top item, testing if the stack is empty, and iterating through the items in LIFO order.
 * This implementation uses a singly linked list with a static nested class for linked-list nodes
 * The push, pop, peek, size, and is-empty operations all take constant time in the worst case.
 """


class Stack:

    class _Node:

        def __init__(self):
            self._item = None
            self._next = None

        def __repr__(self):
            return f"<_Node(_item={self._item}, _next={self._next})>"

    def __init__(self):
        self.first = None
        self.n = 0 

    def is_empty(self):
        return self.first is None

    def size(self):
        return self.n 

    def push(self, item):
        old_first = self.first
        self.first = Stack._Node()
        self.first._item = item 
        self.first._next = old_first
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

    def __repr__(self):
        return f"<Stack(first={self.first}, n={self.n})>"

    def __iter__(self):
        current = self.first
        while current is not None:
            item = current._item
            assert item is not None
            yield item
            current = current._next


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


if __name__ == '__main__':
    main()











