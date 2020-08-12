"""
TrieST.py
A string symbol table for extended ASCII strings, implemented
using a 256-way trie.
This implementation uses a 256-way trie.
 *  The put, contains, delete, and
 *  longest prefix operations take time proportional to the length (L)
 *  of the key (in the Worst Case). Construction takes O(1).
 *  The size, and is-empty operations take constant time.
 *  Construction takes O(1).
 *  Typical case take Theta(L) for search hit and insert; Theta(logR*N) for a search miss.
 *  Space takes Theta(R + 1)N
"""
from queue import Queue


class TrieST:
    R = 256  # extended ASCII
    _root = None
    _n = 0

    def __init__(self):
        self._root = Node()
        self._n = 0
        self.R = 256

    def get(self, key):
        if key is None:
            raise AttributeError(f'argument to get() is None')
        x = self.__get(self._root, key, 0)
        if x is None:
            return None
        return x._val

    def __get(self, x, key, d):
        if x is None:
            return None
        if d == len(key):
            return x
        c = ord(key[d])
        return self.__get(x._next[c], key, d + 1)

    def contains(self, key):
        if key is None:
            raise AttributeError(f'argument to contains() is None')
        return self.get(key) is not None

    def put(self, key, val):
        if key is None:
            raise AttributeError(f'argument to contains() is None')
        if val is None:
            self.delete(key)
        else:
            self.__put(self._root, key, val, 0)

    def __put(self, x, key, val, d):
        if x is None:
            x = Node()
        if d == len(key):
            if x._val is None:
                self._n += 1
            x._val = val
            return x
        c = ord(key[d])
        x._next[c] = self.__put(x._next[c], key, val, d + 1)
        return x

    def size(self):
        return self._n

    def is_empty(self):
        return self.size() == 0

    def keys(self):
        return self.keys_with_prefix("")

    def keys_with_prefix(self, prefix):
        results = Queue()
        x = self.__get(self._root, prefix, 0)
        self.__collect(x, prefix, results)
        return results.queue

    def __collect(self, x, prefix, results):
        if x is None:
            return
        if x._val is not None:
            results.put(prefix)
        for c in range(self.R):
            self.__collect(x._next[c], prefix + chr(c), results)

    def keys_that_match(self, pattern):
        results = Queue()
        self.__collect_match(self._root, "", results, pattern)
        return results.queue

    def __collect_match(self, x, prefix, results, pattern):
        if x is None:
            return
        d = len(prefix)
        if d == len(pattern) and x._val is not None:
            results.put(prefix)
        if d == len(pattern):
            return
        c = ord(pattern[d])
        if chr(c) == '.':
            for ch in range(self.R):
                self.__collect_match(x._next[ch], prefix + chr(ch), results, pattern)
        else:
            self.__collect_match(x._next[c], prefix + chr(c), results, pattern)

    def longest_prefix_of(self, query):
        if query is None:
            raise AttributeError(f'argument to longest_prefix_of() is None')
        length = self.__longest_prefix_of(self._root, query, 0, -1)
        if length == -1:
            return None
        else:
            return query[:length]

    def __longest_prefix_of(self, x, query, d, length):
        if x is None:
            return length
        if x._val is not None:
            length = d
        if len(query) == d:
            return length
        c = ord(query[d])
        return self.__longest_prefix_of(x._next[c], query, d+1, length)

    def delete(self, key):
        if key is None:
            raise AttributeError(f'argument to delete() is None')
        self._root = self.__delete(self._root, key, 0)

    def __delete(self, x, key, d):
        if x is None:
            return None
        if len(key) == d:
            if x._val is not None:
                self._n -= 1
            x._val = None
        else:
            c = ord(key[d])
            x._next[c] = self.__delete(x._next[c], key, d+1)

        # remove sub-trie rooted at x if it is completely empty
        if x._val is not None:
            return x
        for c in range(self.R):
            if x._next[c] is not None:
                return x
        return None

    def __repr__(self):
        return f'<{__class__.__name__}(_root={self._root})>'


class Node:

    def __init__(self):
        self._val = None
        self._next = [None] * TrieST.R

    def __repr__(self):
        return f'<{self.__class__.__name__}(_val: {self._val}, _next={self._next})>'


def main():
    t = TrieST()

    with open('../resources/shellsST.txt') as f:

        lines = "".join(f.readlines()).split(' ')
        for i, line in enumerate(lines):
            t.put(line, i)

        print(t)
        # print(t.get('shells'))
        if t.size() < 100:
            print('keys: ')
            for key in t.keys():
                print(f'{key} {t.get(key)}')
            print()

        print('longest_prefix_of(\'shellsort\')')
        print(t.longest_prefix_of('shellsort'))
        print()

        print('longest_prefix_of(\'quicksort\')')
        print(t.longest_prefix_of('quicksort'))
        print()

        print('keys_with_prefix(\'shor\')')
        for s in t.keys_with_prefix('shor'):
            print(s)
        print()

        print('keys_that_match(\'.he.l.\')')
        for s in t.keys_that_match('.he.l.'):
            print(s)


if __name__ == '__main__':
    main()
