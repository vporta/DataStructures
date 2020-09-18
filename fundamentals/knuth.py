"""
knuth.py
The Knuth (or Fisher-Yates) shuffling algorithm guarantees
 *  to rearrange the elements in uniformly random order, under
 *  the assumption that Math.random() generates independent and
 *  uniformly distributed numbers between 0 and 1.
"""
import random  
from typing import *


class Knuth:

    @staticmethod
    def shuffle(a: list):
        n = len(a)
        for i in range(n):
            # choose index uniformly in [0, i]
            r = int(random.random() * (i + 1))
            Knuth._exch(a, i, r)

    @staticmethod
    def shuffle_alternate(a: List[Any]):
        n = len(a)
        for i in range(n):
            r = i + int(random.random() * n - i)
            Knuth._exch(a, i, r)

    @staticmethod
    def _exch(a, i, r):
        a[i], a[r] = a[r], a[i]


def main():
    a = [1, 2, 3, 4, 5]
    print(a)
    Knuth.shuffle(a)
    print(a)


if __name__ == '__main__':
    main()




