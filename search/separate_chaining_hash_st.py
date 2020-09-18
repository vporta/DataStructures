"""
separate_chaining_hash_st.py
The SeparateChainingHashST class represents a symbol table of generic key-value pairs
RT analysis
 * avg: Constant for Search hit, insert, delete
 * worst: log N for Search, insert, delete
"""
from collections import deque


class SeparateChainingHashST:
    n, M = 0, 97
    st = [0 for _ in range(97)]

    def __init__(self):
        for i in range(len(self.st)):
            self.st[i] = SeparateChainingHashST.Node()

    class Node:
        def __init__(self, key=None, val=None, nxt=None):
            self._key = key
            self._val = val
            self._nxt = nxt

        def get_key(self):
            return self._key

        def get_val(self):
            return self._val

        def get_nxt(self):
            return self._nxt

        def __repr__(self):
            return f'<Node(key={self.get_key()}, val={self.get_val()}, next={self.get_nxt()})>'

    def __hash(self, key):
        return hash(key) & 0x7fffffff % self.M

    def size(self):
        return self.n

    def is_empty(self):
        return self.size() == 0

    def contains(self, key):
        if key is None:
            return AttributeError('argument to contains() is None')
        return self.get(key) is not None

    def get(self, key):
        if key is None:
            return AttributeError('argument to get() is None')
        i = self.__hash(key)
        x = self.st[i]
        while x is not None:
            if key == x.get_key():
                return x.get_val()
            x = x._nxt
        return None

    def put(self, key, val):
        if key is None:
            return AttributeError('argument to put() is None')
        if val is None:
            self.delete(key)
            return
        # if self.n >= 10 * self.M:
        #     self.resize(2*self.M)

        i = self.__hash(key)
        x = self.st[i]
        while x is not None:
            if key == x.get_key():
                x._val = val
                return
            x = x._nxt
        self.st[i] = SeparateChainingHashST.Node(key, val, self.st[i])
        self.n += 1

    def delete(self, key):
        if key is None:
            return AttributeError('argument to delete() is None')
        i = self.__hash(key)
        x = self.st[i]
        while x is not None:
            if key == x.get_key():
                self.n -= 1
                return x.get_nxt()
        x._next = self.delete(key)
        return x

    def keys(self):
        queue = deque()
        for i in range(self.M):
            x = self.st[i]
            while x is not None:
                queue.appendleft(x.get_key())
                x = x.get_nxt()
        return list(queue)

    def __iter__(self):
        yield from self.keys()

    def __repr__(self):
        return f'<SeparateChainingHashST(st={self.st})>'


def main():
    inp = 'SEARCHEXAMPLE'
    st = SeparateChainingHashST()
    for i in range(len(inp)):
        st.put(inp[i], i)
    print(st)
    print('P', st.get('P'))
    print('R', st.get('R'))
    print(st.keys())


if __name__ == '__main__':
    main()
