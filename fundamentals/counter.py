"""
counter.py
 *  A mutable data type for an integer counter.
 *  The test clients create n counters and performs trials increment
 *  operations on random counters.
 $ python fundamentals/counter.py 6 600000
"""
import random as r
import sys


class Counter:

    _count = 0

    def __init__(self, id):
        self._name = id

    def increment(self):
        self._count += 1

    def tally(self):
        return self._count

    def __str__(self):
        return f'{self._count}  {self._name}'

    def __lt__(self, other):
        return self._count < other._count

    def __gt__(self, other):
        return other.__lt__(self)

    def __eq__(self, other):
        return self._count == other._count

    def __ne__(self, other):
        return not self.__eq__(other)


def main(*args):
    args = list(*args)
    n = int(args[0])
    trials = int(args[1])
    hits = [Counter(f'counter {i}') for i in range(n)]

    for t in range(trials):
        hits[int(r.uniform(0, n))].increment()

    for i in range(n):
        print(hits[i])


if __name__ == '__main__':
    main(sys.argv[1:])