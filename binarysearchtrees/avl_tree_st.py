"""
avl_tree_st.py
In an AVL Tree, the heights of the two child subtrees of any
node differ by at most one; if at any time they differ by more than one,
re-balancing is done to restore this property.
For lookup-intensive applications, AVL trees are faster than red–black trees because they are
more strictly balanced. Similar to red–black trees, AVL trees are height-balanced.

Big-O Running Time
Algorithm		Average	    Worst case
Space		    O(n) 	        O(n)
Search		    O(log n)    	O(log n)
Insert		    O(log n) 	    O(log n)
Delete		    O(log n) 	    O(log n)
Construction    O(1)            O(1)
Is Empty        O(1)            O(1)
"""
from collections import deque


class AVLTreeST:

    _root = None

    class Node:
        _left, _right = None, None

        def __init__(self, key, val, height, size):
            self._key = key
            self._val = val
            self._height = height
            self._size = size

        def get_key(self):
            return self._key

        def get_val(self):
            return self._val

        def get_left(self):
            return self._left

        def get_right(self):
            return self._right

        def get_size(self):
            return self._size

        def get_height(self):
            return self._height

        def __repr__(self):
            return f'<Node(' \
                   f'_key={self._key}, ' \
                   f'_val={self._val}, ' \
                   f'_height={self._height}, ' \
                   f'_size={self._size},' \
                   f'_left={self._left},' \
                   f'_right={self._right})>'

    def get_root(self):
        return self._root

    def is_empty(self):
        return self._root is None

    def size(self):
        return self._size(self._root)

    def _size(self, x):
        if x is None:
            return 0
        return x.get_size()

    def height(self):
        return self._height(self._root)

    def _height(self, x):
        if x is None:
            return -1
        return x.get_height()

    def get(self, key):
        if key is None:
            raise ValueError('argument to get() is None')
        x = self.__get(self._root, key)
        if x is None:
            return None
        return x.get_key()  # For use in SymbolTables.SET, otherwise use return x.get_val()

    def __get(self, x, key):
        if x is None:
            return None
        if key < x.get_key():
            return self.__get(x.get_left(), key)
        elif key > x.get_key():
            return self.__get(x.get_right(), key)
        else:
            return x

    def contains(self, key):
        return self.get(key) is not None

    def put(self, key, val=None):
        if key is None:
            raise ValueError('first argument to put() is None')
        # *** Not for use in SymbolTables.SET
        # if val is None:
        #     self.delete(key)
        #     return
        # ***
        self._root = self.__put(self._root, key, val)

    def __put(self, h, key, val):
        if h is None:
            return AVLTreeST.Node(key, val, 0, 1)
        if key < h.get_key():
            h._left = self.__put(h._left, key, val)
        elif key > h.get_key():
            h._right = self.__put(h._right, key, val)
        else:
            h._val = val
            return h
        h._size = self._size(h._left) + self._size(h._right) + 1
        h._height = 1 + max(self._height(h._left), self._height(h._right))
        return self.__balance(h)

    def __balance(self, x):
        if self.__balance_factor(x) < -1:
            if self.__balance_factor(x._right) > 0:
                x._right = self.__rotate_right(x._right)
            x = self.__rotate_left(x)
        elif self.__balance_factor(x) > 1:
            if self.__balance_factor(x._left) < 0:
                x._left = self.__rotate_left(x._left)
            x = self.__rotate_right(x)
        return x

    def __balance_factor(self, x):
        return self._height(x.get_left()) - self._height(x.get_right())

    def __rotate_right(self, x):
        y = x._left
        x._left = y._right
        y._right = x
        y._size = x._size
        x._size = self._size(x._left) + self._size(x.get_right()) + 1
        x._height = max(self._height(x.get_left()), self._height(x.get_right())) + 1
        y._height = max(self._height(y.get_left()), self._height(y.get_right())) + 1
        return y

    def __rotate_left(self, x):
        y = x._right
        x._right = y._left
        y._left = x
        y._size = x._size
        x._size = self._size(x.get_left()) + self._size(x.get_right()) + 1
        x._height = max(self._height(x.get_left()), self._height(x.get_right())) + 1
        y._height = max(self._height(y.get_left()), self._height(y.get_right())) + 1
        return y

    def delete(self, key):
        if key is None:
            raise ValueError('argument to delete() is None')
        if not self.contains(key):
            return
        self._root = self.__delete(self._root, key)

    def __delete(self, x, key):
        if key < x.__key:
            x._left = self.__delete(x._left, key)
        elif key > x.__key:
            x._right = self.__delete(x._right, key)
        else:
            if x._left is None:
                return x._right
            elif x._right is None:
                return x._left
            else:
                y = x
                x = self.__min(y.get_right())
                x._right = self.__delete_min(y.get_right())
                x._left = y.get_left()

        x._size = self._size(x._left) + self._size(x._right) + 1
        x._height = max(self._height(x._left), self._height(x._right)) + 1
        return self.__balance(x)

    def delete__min(self):
        if self.is_empty():
            raise ValueError('Called delete_min() with empty symbol table')
        self._root = self.__delete_min(self._root)

    def __delete_min(self, x):
        if x._left is None:
            return x.get_right()
        x._left = self.__delete_min(x.left)
        x._size = self._size(x._left) + self._size(x.get_right()) + 1
        x._height = max(self._height(x._left), self._height(x.get_right())) + 1
        return self.__balance(x)

    def min(self):
        if self.is_empty():
            raise ValueError('calls min() with empty symbol table')
        return self.__min(self._root).__key

    def __min(self, x):
        if x.get_left() is None:
            return x
        else:
            return self.__min(x.get_left())

    def max(self):
        if self.is_empty():
            raise ValueError('calls min() with empty symbol table')
        return self.__max(self._root).__key

    def __max(self, x):
        if x.get_right() is None:
            return x
        else:
            return self.__max(x.get_right())

    def floor(self, key):
        if key is None:
            raise AttributeError('argument to floor() is None')
        if self.is_empty():
            raise ValueError('called floor with empty symbol table')
        x = self.__floor(self._root, key)
        if x is None:
            return None
        else:
            return x._key

    def __floor(self, x, key):
        if x is None:
            return None
        if key == x.get_key():
            return x
        if key < x.get_key():
            return self.__floor(x.get_left(), key)
        y = self.__floor(x.get_right(), key)
        if y is not None:
            return y
        else:
            return x

    def ceiling(self, key):
        if key is None:
            raise AttributeError('argument to ceiling() is None')
        if self.is_empty():
            raise ValueError('called ceiling() with empty symbol table')
        x = self.__ceiling(self._root, key)
        if x is None:
            return None
        else:
            return x._key

    def __ceiling(self, x, key):
        if x is None:
            return None
        if key == x.get_key():
            return x
        if key > x.get_key():
            return self.__ceiling(x.get_right(), key)
        y = self.__ceiling(x.get_left(), key)
        if y is not None:
            return y
        else:
            return x

    def keys(self):
        return self.keys_in_order()

    def keys_in_order(self):
        q = deque()
        self.__keys_in_order(self._root, q)
        return list(q)

    def __keys_in_order(self, x, q):
        if x is None:
            return
        self.__keys_in_order(x.get_left(), q)
        q.append(x.get_key())
        self.__keys_in_order(x.get_right(), q)

    def keys_level_order(self):
        q = deque()
        keys = deque()
        q.append(self._root)
        self.__keys_level_order(q, keys)
        return list(keys)

    def __keys_level_order(self, q, keys):
        while q:
            x = q.popleft()
            if x is None:
                continue
            keys.append(x._key)
            q.append(x._left)
            q.append(x._right)

    # def keys(self, lo, hi):
    #     if lo is None:
    #         raise ValueError('first argument to keys() is None')
    #     if hi is None:
    #         raise ValueError('second argument to keys() is None')
    #     q = Queue()
    #     self.__keys(self._root, q, lo, hi)
    #     return q

    def __keys(self, x, q, lo, hi):
        if x is None:
            return
        if lo < x._key:
            self.__keys(x._left, q, lo, hi)
        if lo <= x._key and hi >= x._key:
            q.put(x._key)
        if hi > x._key:
            self.__keys(x._right, q, lo, hi)

    def check(self):
        if not self.is_avl():
            print('AVL property not consistent')
        if not self.is_bst():
            print('Symmetric order not consistent')

    def is_avl(self):
        return self.__is_avl(self._root)

    def __is_avl(self, x):
        if x is None:
            return True
        bf = self.__balance_factor(x)
        if bf > 1 or bf < -1: return False
        return self.__is_avl(x._left) and self.__is_avl(x._right)

    def is_bst(self):
        return self.__is_bst(self._root, None, None)

    def __is_bst(self, x, __min, __max):
        if x is None:
            return True
        if __min is not None and x.__key <= __min:
            return False
        if __max is not None and x.__key >= __max:
            return False
        return self.__is_bst(
            x._left, __min, x.__key) and self.__is_bst(
            x._right, x.__key, __max)

    def __repr__(self):
        return f'<AVLTreeST(_root={self._root})>'


def main():
    st = AVLTreeST()
    inp = 'SEARCHEXAMPLE'
    for i in range(len(inp)):
        st.put(inp[i], i)
    print(st)
    print(st.get('E'))
    print(st.put('Y'))
    print(st.get('Y'))
    print(st.keys())
    for m in st.keys_in_order():
        print(m)
    print()
    for m in st.keys_level_order():
        print(m)


if __name__ == '__main__':
    main()
