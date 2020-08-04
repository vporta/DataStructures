"""
TST.py
Symbol table with string keys, implemented using a ternary search
trie (TST).

 *  The TST class represents an symbol table of key-value
 *  pairs, with string keys and generic values.
 *  It supports the usual put, get, contains,
 *  delete, size, and is-empty methods.
 *  It also provides character-based methods for finding the string
 *  in the symbol table that is the longest prefix of a given prefix,
 *  finding all strings in the symbol table that start with a given prefix,
 *  and finding all strings in the symbol table that match a given pattern.
 *  A symbol table implements the associative array abstraction:
 *  when associating a value with a key that is already in the symbol table,
 *  the convention is to replace the old value with the new value.
 *  Unlike java.util.Map, this class uses the convention that
 *  values cannot be null—setting the
 *  value associated with a key to null is equivalent to deleting the key
 *  from the symbol table.
"""
from queue import Queue


class Node:

    def __init__(self):
        self.c = None
        self.val = None
        self.left = None
        self.mid = None
        self.right = None


class TST:

    def __init__(self):
        self._n = 0
        self._root = None

    def size(self):
        return self._n

    def contains(self, key):
        if key is None:
            raise AttributeError('argument to contain() is None')
        return self.get(key) is not None

    def get(self, key):
        if key is None:
            raise AttributeError('argument to get() is None')
        if len(key) == 0:
            raise AttributeError('key must have length >= 1')
        x = self.__get(self._root, key, 0)
        if x is None:
            return None
        return x.val

    def __get(self, x, key, d):
        if x is None:
            return None
        if len(key) == 0:
            raise AttributeError('key must have length >= 1')
        c = ord(key[d])
        if c < x.c:
            return self.__get(x.left, key, d)
        elif c > x.c:
            return self.__get(x.right, key, d)
        elif d < len(key) - 1:
            return self.__get(x.mid, key, d+1)
        else:
            return x

    def put(self, key, val):
        if key is None:
            raise AttributeError('calls put() with None key')
        if not self.contains(key):
            self._n += 1
        elif val is None:
            self._n -= 1
        self._root = self.__put(self._root, key, val, 0)

    def __put(self, x, key, val, d):
        c = ord(key[d])
        if x is None:
            x = Node()
            x.c = c
        if c < x.c:
            x.left = self.__put(x.left, key, val, d)
        elif c > x.c:
            x.right = self.__put(x.right, key, val, d)
        elif d < len(key) - 1:
            x.mid = self.__put(x.mid, key, val, d + 1)
        else:
            x.val = val
        return x

    def longest_prefix_of(self, query):
        if query is None:
            raise AttributeError('calls longest_prefix_of() with null argument')
        if len(query) == 0:
            return None
        length = 0
        x = self._root
        i = 0
        while i < len(query) and x is not None:
            c = query[i]
            if c < chr(x.c):
                x = x.left
            elif c > chr(x.c):
                x = x.right
            else:
                i += 1
                if x.val is not None:
                    length = i
                x = x.mid

        return query[:length]

    def keys_with_prefix(self, prefix):
        if prefix is None:
            raise AttributeError('calls keys_with_prefix() with None argument')
        queue = Queue()
        x = self.__get(self._root, prefix, 0)
        if x is None:
            return queue
        if x.val is not None:
            queue.put(prefix)
        self.__collect(x, prefix, queue)
        return queue.queue

    def keys(self):
        queue = Queue()
        self.__collect(self._root, "", queue)
        return queue.queue

    def __collect(self, x, prefix, queue):
        if x is None:
            return
        self.__collect(x.left, prefix, queue)
        if x.val is not None:
            c = prefix + chr(x.c)
            queue.put(c)
        self.__collect(x.mid, prefix + chr(x.c), queue)
        self.__collect(x.right, prefix, queue)

    def keys_that_match(self, pattern):
        queue = Queue()
        self.__collect_match(self._root, "", 0, pattern, queue)
        return queue.queue

    def __collect_match(self, x, prefix, i, pattern, queue):
        if x is None:
            return
        c = pattern[i]

        # go left if c comes before char in TST
        if c == '.' or c < chr(x.c):
            self.__collect_match(x.left, prefix, i, pattern, queue)

        # find wildcard pattern and a char match
        # add char's to prefix string and add to the queue,
        # when we get to the end of the pattern string
        if c == '.' or c == chr(x.c):
            if i == len(pattern) - 1 and x.val is not None:
                queue.put(prefix + chr(x.c))

            # keep going down the pattern char by char, inc i because a match is encountered, recur
            if i < len(pattern) - 1:
                self.__collect_match(x.mid, prefix + chr(x.c), i+1, pattern, queue)

        # go right if c comes before char in TST
        # we don't need to inc. i because c hasn't been found in the TST yet.
        if c == '.' or c > chr(x.c):
            self.__collect_match(x.right, prefix, i, pattern, queue)


def main():
    t = TST()

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





