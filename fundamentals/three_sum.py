"""
three_sum.py
 *  A program with cubic running time. Reads n integers
 *  and counts the number of triples that sum to exactly 0
 *  (ignoring integer overflow).
 *  The ThreeSum class provides static methods for counting
 *  and printing the number of triples in an array of integers that sum to 0
 *  (ignoring integer overflow).
 *  This implementation uses a triply nested loop and takes proportional to n^3,
 *  where n is the number of integers.
"""
from fundamentals.stopwatch import StopWatch


class ThreeSum:

    @staticmethod
    def print_all(a):
        n = len(a)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if a[i] + a[j] + a[k] == 0:
                        print(f'{a[i]}     {a[j]}     {a[k]}')

    @staticmethod
    def count(a):
        n = len(a)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if a[i] + a[j] + a[k] == 0:
                        count += 1
        return count


def main():
    with open('../resources/1Kints.txt') as f:

        a = list(map(int, f.read().replace(' ', '').splitlines()))
        timer = StopWatch()
        count = ThreeSum.count(a)
        print(f'elapsed time = {timer.elapsed_time()}')
        print(count)


if __name__ == '__main__':
    main()