"""
BTree.py
The BTree class represents an ordered symbol table of String key-value pairs.
"""

from typing import List, Any


class BTree:
    __M = 4
    __height = 0
    __n = 0
    __root = None

    class Node:

        __m = 0
        __children = [0 for _ in range(4)]

        def __init__(self, k):
            self.__m = k

        def __repr__(self):
            return f'<Node(__children={self.__children}, __m={self.__m})>'

    # internal nodes: only use key and next
    # external nodes: only use key and value
    class Entry:
        def __init__(self, key, val, nxt):
            self.__key = key
            self.__val = val
            self.__next = nxt

    def __init__(self):
        self.__root = self.Node(0)
        print(self.size())

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return self.__n

    def height(self):
        return self.__height

    def get(self, key):
        if key is None:
            raise ValueError('argument to get() is None')
        return self.__search(self.__root, key, self.__height)

    def __search(self, x, key, ht):
        children = x.__children

        # external node
        if ht == 0:
            for j in range(x.__m):
                if key == children[j].__key:
                    return children[j].__val
        # internal node
        else:
            for j in range(x.__m):
                if j + 1 == x.__m or key < children[j + 1].__key:
                    return self.__search(children[j + 1].__next, key, ht - 1)
        return None

    def put(self, key, val):
        if key is None:
            raise ValueError('argument to put() is None')

        u = self.__insert(
            self.__root,
            key,
            val,
            self.__height)
        self.__n += 1
        if u is None:
            return
        # need to split the root
        t = BTree.Node(2)
        print(t)
        t.__children[0] = BTree.Entry(
            self.__root.__children[0].__key,
            None,
            self.__root)
        t.__children[1] = BTree.Entry(
            u.__children[0].__key,
            None,
            u)
        self.__root = t
        self.__height += 1

    def __insert(self, h, key, val, ht):
        j = 0
        t = self.Entry(key, val, None)
        # external node
        if ht == 0:
            for j in range(j, h.__m):
                if key < h.__children[j].__key:
                    break
        # internal node
        else:
            for j in range(j, h.__m):
                if j + 1 == h.__m or key < h.__children[j + 1].__key:
                    next_j = j + 1
                    u = self.__insert(h.__children[next_j].__next, key, val, ht - 1)
                    if u is None:
                        return None
                    t.key = u.__children[0].__key
                    t.__next = u
                    break
        i = h.__m
        while i > j:
            h.__children[i] = h.__children[i - 1]
            i -= 1
        h.__children[j] = t
        h.__m += 1
        if h.__m < self.__M:
            return None
        else:
            return self.__split(h)

    def __split(self, h):
        t = self.Node(self.__M // 2)
        h.__m = self.__M // 2
        for j in range(self.__M // 2):
            t.__children[j] = h.__children[self.__M // 2 + j]
        return t

    def __repr__(self):
        return f'<BTree(' \
               f'__M={self.__M}, ' \
               f'__height={self.__height}, ' \
               f'__n={self.__n}, ' \
               f'__root={self.__root})>'


def main():
    st = BTree()
    print(st)
    st.put("www.cs.princeton.edu", "128.112.136.12")
    st.put("www.cs.princeton.edu", "128.112.136.11")
    st.put("www.princeton.edu", "128.112.128.15")
    st.put("www.yale.edu", "130.132.143.21")


if __name__ == '__main__':
    main()
