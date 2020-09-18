"""
st.py
 *  Sorted symbol table implementation using a java.util.TreeMap.
 *  Does not allow duplicates.
 *  The ST class represents an ordered symbol table of generic
 *  key-value pairs.
 *  It supports the usual put, get, contains,
 *  delete, size, and is-empty methods.
 *  It also provides ordered methods for finding the minimum,
 *  maximum, floor, and ceiling.
 *  It also provides a keys method for iterating over all of the keys.
 *  A symbol table implements the associative array abstraction:
 *  when associating a value with a key that is already in the symbol table,
 *  the convention is to replace the old value with the new value.
 *  Unlike java.util.Map, this class uses the convention that
 *  values cannot be  null—setting the
 *  value associated with a key to  null is equivalent to deleting the key
 *  from the symbol table.
 *
 *  It requires that
 *  the key type implements the  Comparable interface and calls the
 *   compareTo() and method to compare two keys. It does not call either
 *   equals() or  hashCode().
 *
 *  This implementation uses a red-black BST.
 *  The put, get, contains, remove,
 *  minimum, maximum, ceiling, and floor
 *  operations each take Theta(log n) time in the worst case,
 *  where n is the number of key-value pairs in the symbol table.
 *  The size and is-empty operations take Theta(1) time.
 *  Construction takes Theta(1) time.

"""


class ST:
    def __init__(self):
        self._st = dict()

    def get(self, key):
        if key is None:
            raise AttributeError("called get() with None key")
        return self._st.get(key)

    def put(self, key, val):
        if key is None:
            raise AttributeError("called put() with None key")
        if val is None:
            self._st.pop(key, None)
        else:
            self._st[key] = val

    def delete(self, key):
        if key is None:
            raise AttributeError("called delete() with None key")
        self._st.pop(key, None)

    def contains(self, key):
        if key is None:
            raise AttributeError("called contains() with None key")
        return key in self._st

    def size(self):
        return len(self._st)

    def __len__(self):
        return self.size()

    def is_empty(self):
        return self.size() == 0

    def keys(self):
        return self._st.keys()

    def __iter__(self):
        for k in self.keys():
            yield k

    def min(self):
        if self.is_empty():
            raise ValueError("called min() with empty symbol table")
        return min(self._st)

    def max(self):
        if self.is_empty():
            raise ValueError("called max() with empty symbol table")
        return max(self._st)

    def ceiling(self, key):
        if key is None:
            raise AttributeError("called ceiling() with None key")
        keys = self.keys()
        ceiling = None
        for k in keys:
            if (ceiling is None and k >= key) or (
                    ceiling is not None and key <= k < ceiling
            ):
                ceiling = k
        if ceiling is None:
            raise ValueError("all keys are less than " + str(key))
        return ceiling

    def floor(self, key):
        if key is None:
            raise AttributeError("called floor() with None key")
        keys = self.keys()
        floor = None
        for k in keys:
            if (floor is None and k <= key) or (
                    floor is not None and key >= k > floor
            ):
                floor = k
        if floor is None:
            raise ValueError("all keys are greater than " + str(key))
        return floor
