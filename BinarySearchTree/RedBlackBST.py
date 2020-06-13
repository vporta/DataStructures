"""
RedBlackBST.py
A symbol table implemented using a left-leaning red-black BST.
The put, get, contains, remove, minimum, maximum operations each take Θ(log n)
time in the worst case, where n is the number of key-value pairs in the symbol table.
The size, and is-empty operations take Θ(1) time. The keys methods take O(log n + m) time,
where m is the number of keys returned by the iterator. Construction takes Θ(1) time.
This is the 2-3 version.
"""


class RedBlackBST:
    RED: bool = True
    BLACK: bool = False

    class Node:

        def __init__(self, key, val, size, color=True, left=None, right=None):
            self.key = key
            self.val = val
            self.color = color
            self.size = size
            self.left = left
            self.right = right

        def __lt__(self, other):
            return self.key < other.key

        def __gt__(self, other):
            return self.key > other.key

        def __eq__(self, other):
            return self.key == other.key

        def __repr__(self):
            return f'<Node(key={self.key}, ' \
                   f'val={self.val}, ' \
                   f'size={self.size}, ' \
                   f'color={self.color}, ' \
                   f'left={self.left}, ' \
                   f'right={self.right})>'

    def __init__(self):
        self.TNULL = RedBlackBST.Node('', 0, 1, False)
        self.root = self.TNULL

    def _is_red(self, x: Node):
        if x is None:
            return False
        return x.color == self.RED

    def __size(self, x: Node):
        if x is None:
            return 0
        return x.size

    def size(self):
        return self.__size(self.root)

    def is_empty(self):
        return self.root is None

    def get(self, key):
        if key is None:
            raise ValueError('argument to get() is None')
        return self.__get(self.root, key)

    def __get(self, x, key):
        while x is not None:
            if key < x.key:
                x = x.left
            elif key > x.key:
                x = x.right
            else:
                return x.val
        return None

    def put(self, key, val):
        if key is None:
            raise ValueError('first argument to put() is None')
        if val is None:
            self.delete(key)
            return
        self.root = self.__put(self.root, key, val)
        self.root.color = self.BLACK
        # assert self.check()

    def __put(self, h, key, val):
        if h is None:
            return RedBlackBST.Node(key, val, 1, self.RED)
        if key < h.key:
            h.left = self.__put(h.left, key, val)
        elif key > h.key:
            h.right = self.__put(h.right, key, val)
        else:
            h.val = val

        if self._is_red(h.right) and not self._is_red(h.left):
            h = self.rotate_left(h)
        if self._is_red(h.left) and self._is_red(h.left.left):
            h = self.rotate_right(h)
        if self._is_red(h.left) and self._is_red(h.right):
            print(f'h {h}')
            self.flip_colors(h)
        h.size = self.__size(h.left) + self.__size(h.right) + 1
        return h

    def contains(self, key):
        return self.get(key) is not None

    def delete_min(self):
        if self.is_empty():
            raise ValueError('BST underflow')
        if not self._is_red(self.root.left) and not self._is_red(self.root.right):
            self.root.color = self.RED

        self.root = self.__delete_min(self.root)
        if not self.is_empty():
            self.root.color = self.BLACK

    def __delete_min(self, h):
        if h.left is None: return None
        if not self._is_red(h.left) and not self._is_red(h.left.left):
            h = self._move_red_left(h)
        h.left = self.__delete_min(h.left)
        return self._balance(h)

    def delete_max(self):
        if self.is_empty():
            raise ValueError('BST underflow')

        # if both children of root are black, set root to red
        if not self._is_red(self.root.left) and not self._is_red(self.root.right):
            self.root.color = self.RED
        self.root = self._delete_max(self.root)

        if not self.is_empty():
            self.root.color = self.BLACK

    def _delete_max(self, h):
        if self._is_red(h.left):
            h = self.rotate_right(h)
        if h.right is None: return None
        if not self._is_red(h.left) and not self._is_red(h.right.left):
            h = self._move_red_right(h)
        h.right = self._delete_max(h.right)
        return self._balance(h)

    def delete(self, key):
        if key is None:
            raise ValueError('argument to delete() is None')
        if not self.contains(key): return
        # if both children of root are black, set root to red
        if not self._is_red(self.root.left) and not self._is_red(self.root.right):
            self.root.color = self.RED
        self.root = self._delete(self.root, key)
        if not self.is_empty():
            self.root.color = self.BLACK

    def _delete(self, h, key):
        if key < h.key:
            if not self._is_red(h.left) and not self._is_red(h.left.left):
                h = self._move_red_left(h)
            h.left = self._delete(h.left, key)
        else:
            if self._is_red(h.left):
                h = self.rotate_right(h)
            if key == h.key and h.right is None:
                return None
            if not self._is_red(h.right) and not self._is_red(h.right.left):
                h = self._move_red_right(h)
            if key == h.key:
                x = self._min(h.right)
                h.key = x.key
                h.val = x.val
                h.right = self.__delete_min(h.right)
            else:
                h.right = self._delete(h.right, key)
        return self._balance(h)

    def rotate_right(self, h):
        x = h.left
        h.left = x.right
        x.right = h
        x.color = x.right.color
        x.right.color = self.RED
        x.size = h.size
        h.size = self.__size(h.left) + self.__size(h.right) + 1
        return x

    def rotate_left(self, h):
        x = h.right
        h.right = x.left
        x.left = h
        x.color = x.left.color
        x.left.color = self.RED
        x.size = h.size
        h.size = self.__size(h.left) + self.__size(h.right) + 1
        return x

    def flip_colors(self, h):
        h.color = not h.color
        h.left.color = not h.left.color
        h.right.color = not h.right.color

    def _move_red_left(self, h):
        self.flip_colors(h)
        if self._is_red(h.right.left):
            h.right = self.rotate_right(h.right)
            h = self.rotate_left(h)
            self.flip_colors(h)
        return h

    def _move_red_right(self, h):
        self.flip_colors(h)
        if self._is_red(h.left.left):
            h = self.rotate_right(h)
            self.flip_colors(h)
        return h

    def _balance(self, h):
        if self._is_red(h.right):
            h = self.rotate_left(h)
        if self._is_red(h.left) and self._is_red(h.left.left):
            h = self.rotate_right(h)
        if self._is_red(h.left) and self._is_red(h.right):
            self.flip_colors(h)
        h.size = self.__size(h.left) + self.__size(h.right) + 1
        return h

    def height(self):
        return self._height(self.root)

    def _height(self, x):
        if x is None: return -1
        return 1 + max(self._height(x.left), self._height(x.right))

    def min(self):
        if self.is_empty(): raise ValueError('calls min() with empty symbol table')
        return self._min(self.root).key

    def _min(self, x):
        if x.left is None:
            return x
        else:
            return self._min(x.left)

    def max(self):
        if self.is_empty(): raise ValueError('calls max() with empty symbol table')
        return self._max(self.root).key

    def _max(self, x):
        if x.right is None:
            return x
        else:
            return self._max(x.right)

    def check(self):
        if not self.is_bst():
            print('Not in symmetric order')
        if not self.is23():
            print('Not a 2-3 tree')
        if not self.is_balanced():
            print('Not balanced')

    def is_bst(self):
        return self.__is_bst(self.root, None, None)

    def __is_bst(self, x, _min, _max):
        if x is None:
            return True
        if _min is not None and x.key <= _min:
            return False
        if _max is not None and x.key >= _max:
            return False
        return self.__is_bst(x.left, _min, x.key) and self.__is_bst(x.right, x.key, _max)

    def is_balanced(self):
        black = 0
        x = self.root
        while x is not None:
            if not self._is_red(x):
                black += 1
                x = x.left
        return self.__is_balanced(self.root, black)

    def __is_balanced(self, x, black):
        if x is None:
            return black == 0
        if not self._is_red(x):
            black -= 1
        return self.__is_balanced(x.left, black) and self.__is_balanced(x.right, black)

    def is23(self):
        return self.__is23(self.root)

    def __is23(self, x):
        """
        Does the tree have no red right links, and at most one (left)
        red links in a row on any path?
        :rtype: bool
        """
        if x is None:
            return True
        if self._is_red(x.right):
            return False
        if x != self.root and self._is_red(x) and self._is_red(x.left):
            return False
        return self.__is23(x.left) and self.__is23(x.right)

    def __repr__(self):
        return f'<RedBlackBST(root={self.root})>'


def main():
    inp = 'SEARCHEXAMPLE'
    st = RedBlackBST()
    for i in range(len(inp)):
        st.put(inp[i], i)
    print(st)


if __name__ == '__main__':
    main()
