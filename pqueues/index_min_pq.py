"""
index_min_pq.py
Minimum-oriented indexed PQ implementation using a binary heap
"""


class Key:

    def __init__(self, key=0.0, removed=False):
        self._key = key
        self._removed = removed

    def get_key(self):
        return self._key

    def __lt__(self, other):
        return self.get_key() < other.get_key()

    def __gt__(self, other):
        return self.get_key() > other.get_key()

    def __eq__(self, other):
        return self.get_key() == other.get_key()

    def __repr__(self):
        return f'<{self.__class__.__name__}(_key={self.get_key()}, _removed={self._removed})>'


class IndexMinPQ:

    def __init__(self, max_n):
        if max_n < 0:
            raise AttributeError()
        self._max_n = max_n
        self._n = 0
        self._keys = [Key()] * (max_n+1)
        self._pq = [0] * (max_n+1)
        self._qp = [-1] * (max_n+1)

    def is_empty(self):
        return self._n == 0

    def contains(self, i):
        self.__validate_index(i)
        return self._qp[i] != -1

    def __len__(self):
        return len(self._pq)

    def size(self):
        return self._n

    def insert(self, i, key):
        self.__validate_index(i)
        # print(i, self.size(), self._n, self.is_empty())
        if self.contains(i):
            raise AttributeError(f"index is already in the priority queue: {i}")
        self._n += 1
        self._qp[i] = self._n
        self._pq[self._n] = i
        self._keys[i] = Key(key)
        self.__swim(self._n)

    def min_index(self):
        if self._n == 0:
            raise AttributeError('Priority queue underflow')
        return self._pq[1]

    def min_key(self):
        if self._n == 0:
            raise AttributeError('Priority queue underflow')
        return self._keys[self._pq[1]]

    def del_min(self):
        if self._n == 0:
            raise AttributeError('Priority queue underflow')
        minimum = self._pq[1]
        self.__exch(1, self._n)
        self._n -= 1
        self.__sink(1)
        # print('min, self._pq[self._n+1]', minimum, self._pq[self._n+1])
        assert minimum == self._pq[self._n+1]
        self._qp[minimum] = -1
        self._keys[minimum] = Key(removed=True)
        self._pq[self._n + 1] = -1
        return minimum

    def key_of(self, i):
        self.__validate_index(i)
        if not self.contains(i):
            raise BaseException('index is not in the priority queue')
        return self._keys[i]

    def change_key(self, i, key):
        self.__validate_index(i)
        if not self.contains(i):
            raise BaseException('index is not in the priority queue')
        self._keys[i] = Key(key)
        self.__swim(self._qp[i])
        self.__sink(self._qp[i])

    def decrease_key(self, i, key):
        self.__validate_index(i)
        if not self.contains(i):
            raise BaseException('index is not in the priority queue')
        if self._keys[i] == Key(key):
            raise AttributeError('Calling decreaseKey() with a key equal to the key in the priority queue')
        if self._keys[i] < Key(key):
            raise AttributeError('Calling decreaseKey() with a key strictly greater than the key in the priority queue')
        self._keys[i] = Key(key)
        self.__swim(self._qp[i])

    def increase_key(self, i, key):
        self.__validate_index(i)
        if not self.contains(i):
            raise BaseException('index is not in the priority queue')
        if self._keys[i] == Key(key):
            raise AttributeError('Calling decreaseKey() with a key equal to the key in the priority queue')
        if self._keys[i] > Key(key):
            raise AttributeError('Calling decreaseKey() with a key strictly greater than the key in the priority queue')
        self._keys[i] = Key(key)
        self.__sink(self._qp[i])

    def delete(self, i):
        self.__validate_index(i)
        if not self.contains(i):
            raise AttributeError('index is not in the priority queue')
        index = self._qp[i]
        self._n -= 1
        self.__exch(index, self._n)
        self.__swim(index)
        self.__sink(index)
        self._keys[i] = Key(removed=True)
        self._qp[i] = -1

    def __exch(self, i, j):
        self._pq[i], self._pq[j] = self._pq[j], self._pq[i]
        self._qp[self._pq[i]] = i
        self._qp[self._pq[j]] = j

    def __swim(self, k):
        # parent_index = abs(k - 1) // 2
        while k > 1 and self._keys[self._pq[k//2]] > self._keys[self._pq[k]]:
            self.__exch(k, k//2)
            k = k//2

    def __sink(self, k):
        while 2 * k <= self._n:
            j = 2 * k
            if j < self._n and self._keys[self._pq[j]] > self._keys[self._pq[j+1]]:
                j += 1
            if not self._keys[self._pq[k]] > self._keys[self._pq[j]]:
                break
            self.__exch(k, j)
            k = j

    def __validate_index(self, i):
        if i < 0:
            raise AttributeError("index is negative: " + i)
        if i >= self._max_n:
            raise AttributeError("index >= capacity: " + i)

    def __repr__(self):
        return f'<{self.__class__.__name__}(' \
               f'_pq={self._pq}, ' \
               f'_n={self._n} ' \
               f'_keys={self._keys} ' \
               f'_qp={self._qp})>'


def main():
    strings = [125, 80, 200]
    pq = IndexMinPQ(len(strings))
    for i in range(len(strings)):
        pq.insert(i, strings[i])
    # pq.insert(0, 'it')
    # pq.insert(1, 'was')
    print(pq)
    print('size ', pq.size())
    pq.delete(1)
    print(pq)
    # while not pq.is_empty():
    #     i = pq.del_min()
    #     print(f'{i} {strings[i]}')



if __name__ == '__main__':
    main()