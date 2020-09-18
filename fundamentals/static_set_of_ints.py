"""
static_set_of_ints.py
 *  The StaticSETofInts class represents a set of integers.
 *  It supports searching for a given integer in the set. It accomplishes
 *  this by keeping the set of integers in a sorted array and using
 *  binary search to find the given integer.
 *
 *  The rank and contains operations take
 *  logarithmic time in the worst case.
"""
from typing import List


class StaticSETofInts:

    _a = None

    def __init__(self, keys: List[int]):
        self._a = sorted([keys[i] for i in range(len(keys))])
        for i in range(1, len(self._a)):
            if self._a[i] == self._a[i - 1]:
                raise ValueError('Argument arrays contains duplicate keys.')

    def contains(self, key):
        return self.rank(key) != -1

    def rank(self, key):
        lo, hi = 0, len(self._a) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if key < self._a[mid]:
                hi = mid - 1
            elif key > self._a[mid]:
                lo = mid + 1
            else:
                return mid
        return -1

    def __str__(self):
        return f'a = {self._a}'


def main():
    a = [7, 20, 12, 32, 18, 4]
    s = StaticSETofInts(a)
    print(s)
    print(s.rank(20))


if __name__ == '__main__':
    main()
