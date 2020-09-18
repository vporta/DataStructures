"""
three_sum_fast.py
 *  A program with n^2 log n running time. Reads n integers
 *  and counts the number of triples that sum to exactly 0.
 *  The ThreeSumFast class provides static methods for counting
 *  and printing the number of triples in an array of distinct integers that
 *  sum to 0 (ignoring integer overflow).
 *
 *  This implementation uses sorting and binary search and takes time
 *  proportional to n^2 log n, where n is the number of integers.
"""
from bisect import bisect_left
from fundamentals.stopwatch import StopWatch


def binary_search(a, x, lo=0, hi=None):  # can't use a to specify default for hi
    hi = hi if hi is not None else len(a)  # hi defaults to len(a)
    pos = bisect_left(a, x, lo, hi)  # find insertion position
    return pos if pos != hi and a[pos] == x else -1  # don't walk off the end


class ThreeSumFast:

    @staticmethod
    def _contains_duplicates(a):
        n = len(a)
        for i in range(1, n):
            if a[i] == a[i - 1]:
                return True
        return False

    @staticmethod
    def print_all(a):
        n = len(a)
        a.sort()
        if ThreeSumFast._contains_duplicates(a):
            raise AttributeError('list contains duplicate integers')
        for i in range(n):
            for j in range(i + 1, n):
                k = binary_search(a, -(a[i] + a[j]))
                if k > j:
                    print(f'{a[i]}     {a[j]}     {a[k]}')

    @staticmethod
    def count(a):
        n = len(a)
        a.sort()
        if ThreeSumFast._contains_duplicates(a):
            raise AttributeError('list contains duplicate integers')
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                k = binary_search(a, -(a[i] + a[j]))
                if k > j:
                    count += 1
        return count


def main():
    with open('../resources/1Kints.txt') as f:
        a = list(map(int, f.read().replace(' ', '').splitlines()))
        timer = StopWatch()
        count = ThreeSumFast.count(a)
        print(f'elapsed time = {timer.elapsed_time()}')
        print(count)
        ThreeSumFast.print_all(a)


if __name__ == '__main__':
    main()

