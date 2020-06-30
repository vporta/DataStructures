"""
SET.py
Dependencies: AVLTreeST
SET class represents an ordered set of comparable keys.
 *  It supports the usual add, contains, and delete
 *  methods. It also provides ordered methods for finding the minimum,
 *  maximum, floor, and ceiling and set methods
 *  for union, intersection, and equality.
 *  <p>
 *  Even though this implementation include the method equals(), it
 *  does not support the method hashCode() because sets are mutable.
 *  <p>
 *  This implementation uses a balanced binary search tree.
 *  The add, contains, delete, minimum,
 *  maximum, ceiling, and floor methods take
 *  logarithmic time in the worst case.
 *  The size, and is-empty operations take constant time.
 *  Construction takes constant time.
"""

from BinarySearchTree.AVLTreeST import AVLTreeST as TreeSet


class SET:

    def __init__(self):
        self._set = TreeSet()

    def get_set(self):
        return self._set

    def add(self, key):
        if key is None:
            raise AttributeError('called add() with a None key')
        return self.get_set().put(key)

    def contains(self, key):
        if key is None:
            raise AttributeError('called contains() with a None key')
        return self.get_set().contains(key)

    def remove(self, key):
        if key is None:
            raise AttributeError('called remove() with a None key')
        return self.get_set().delete(key)

    def size(self):
        return self.get_set().size()

    def is_empty(self):
        return self.size() == 0

    def iterator(self):
        return self.get_set().keys()

    def max(self):
        if self.is_empty():
            raise ValueError('called max() with empty set')
        return self.get_set().max()

    def min(self):
        if self.is_empty():
            raise ValueError('called min() with empty set')
        return self.get_set().min()

    # Returns the smallest key in the BST greater than or equal to key ie "successor."
    def ceiling(self, key):
        if key is None:
            raise AttributeError('called ceiling() with a None key')
        k = self.get_set().ceiling(key)
        if k is None:
            raise ValueError(f'all keys are less than {key}')
        return k

    # Returns the largest key in the BST less than or equal to key ie "predecessor."
    def floor(self, key):
        if key is None:
            raise AttributeError('called floor() with a None key')
        k = self.get_set().floor(key)
        if k is None:
            raise ValueError(f'all keys are greater than {key}')
        return k

    def union(self, that):
        if that is None:
            raise ValueError('called union() with a None argument')
        c = SET()
        for x in self:
            c.add(x)
        for x in that:
            c.add(x)
        return c

    def intersects(self, that):
        if that is None:
            raise ValueError('called intersects() with a None argument')
        c = SET()
        if self.size() < that.size():
            for x in self:
                if that.contains(x):
                    c.add(x)
        else:
            for x in that:
                if self.contains(x):
                    c.add(x)
        return c

    def __repr__(self):
        return f'<SET(set={self.get_set()})>'

    def __iter__(self):
        yield from self


def main():
    st = SET()
    print(f'set = {st}')
    st.add("www.cs.princeton.edu")
    st.add("www.cs.princeton.edu")
    st.add("www.princeton.edu")
    st.add("www.math.princeton.edu")
    print(st.contains("www.cs.princeton.edu"))
    print(not st.contains("www.harvardsucks.com"))
    print(st.contains("www.simpsons.com"))
    print()

    # print("ceiling(www.simpsonr.com) = ", st.ceiling("www.simpsonr.com"))
    # print("ceiling(www.simpsons.com) = ", st.ceiling("www.simpsons.com"))
    # print("ceiling(www.simpsont.com) = ", st.ceiling("www.simpsont.com"))
    # print("floor(www.simpsonr.com)   = ", st.floor("www.simpsonr.com"))
    # print("floor(www.simpsons.com)   = ", st.floor("www.simpsons.com"))
    # print("floor(www.simpsont.com)   = ", st.floor("www.simpsont.com"))
    print()

    print("set = ", st)
    print(st.iterator())


if __name__ == '__main__':
    main()
