"""
LinearProbingHashST.py
LinearProbingHashST class represents a symbol table of key-value pairs.
This implementation uses a linear probing hash table. It requires that
 *  the key type overrides the equals() and hashCode() methods.
 *  The expected time per put, contains, or remove
 *  operation is constant, subject to the uniform hashing assumption.
 *  The size, and is-empty operations take constant time.
 *  Construction takes constant time.
"""
from collections import deque


class LinearProbingHashST:
    INIT_CAPACITY = 4

    def __init__(self, capacity=4):
        self._m = capacity
        self._n = 0
        self._keys = [None for _ in range(self._m)]
        self._values = [None for _ in range(self._m)]

    def get_m(self):
        return self._m

    def get_n(self):
        return self._n

    def get_keys(self):
        return self._keys

    def get_values(self):
        return self._values

    def size(self):
        return self.get_n()

    def is_empty(self):
        return self.size() == 0

    def contains(self, key):
        if key is None:
            raise AttributeError('argument to contains() is None')
        return self.get(key) is not None

    def __hash(self, key):
        return hash(key) & 0x7fffffff % self.get_m()

    def __resize(self, capacity):
        temp = LinearProbingHashST(capacity)
        for i in range(self.get_m()):
            if self.get_keys()[i] is not None:
                temp.put(self.get_keys()[i], self.get_values()[i])
        self._keys = temp._keys
        self._values = temp._values
        self._m = temp._m

    def put(self, key, value):
        if key is None:
            raise AttributeError('first argument to put() is None')
        if value is None:
            self.delete(key)
            return
        if self.get_n() >= self.get_m() // 2:
            m = 2 * self.get_m()
            self.__resize(m)
        i = self.__hash(key)
        while self.get_keys()[i] is not None:
            if self.get_keys()[i] == key:
                self.get_values()[i] = value
                return
            i = (i + 1) % self.get_m()
        self.get_keys()[i] = key
        self.get_values()[i] = value
        self._n += 1

    def get(self, key):
        if key is None:
            raise AttributeError('argument to get() is None')
        i = self.__hash(key)
        while self.get_keys()[i] is not None:
            if self.get_keys()[i] == key:
                return self.get_values()[i]

            i = (i + 1) % self.get_m()
        return None

    def delete(self, key):
        if key is None:
            raise AttributeError('argument to delete() is None')
        if not self.contains(key):
            return
        # find position of key
        i = self.__hash(key)
        while key != self.get_keys()[i]:
            i = (i + 1) % self.get_m()
        self.get_keys()[i] = None
        self.get_values()[i] = None
        # rehash all keys in the same cluster
        i = (i + 1) % self.get_m()
        while self.get_keys()[i] is not None:
            # delete _keys[i] and values[i] and reinsert
            key_to_rehash = self.get_keys()[i]
            value_to_rehash = self.get_values()[i]
            self._n -= 1
            self.put(key_to_rehash, value_to_rehash)
            i = (i + 1) % self.get_m()
        self._n -= 1
        # halves the size of the list if it is 12.5% full or less
        if 0 < self.get_n() <= self.get_m() // 8:  # _n > 0 and _n <= _m / 8
            m = self.get_m() // 2
            self.__resize(m)

    def keys(self):
        queue = deque()
        for i in range(self.get_m()):
            if self.get_keys()[i] is not None:
                queue.appendleft(self.get_keys()[i])
        return list(queue)

    def __repr__(self):
        return f'<LinearProbingHashST(' \
               f'm={self.get_m()}, ' \
               f'n={self.get_n()}, ' \
               f'keys={self.get_keys()}, ' \
               f'values={self.get_values()})>'


def main():
    st = LinearProbingHashST()
    inp = 'SEARCHEXAMPLE'
    for i in range(len(inp)):
        st.put(inp[i], i)
    print(st)
    print(st.get('P'))
    print(st.size())
    print(st.contains('S'))
    for s in st.keys():
        print(f'{s} {st.get(s)}')


if __name__ == '__main__':
    main()
