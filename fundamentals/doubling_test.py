"""
doubling_test.py
 *  The DoublingTest class provides a client for measuring
 *  the running time of a method using a doubling test.
"""
import random as r

from fundamentals.stopwatch import StopWatch
from fundamentals.three_sum import ThreeSum


class DoublingTest:
    MAXIMUM_INTEGER = 1000000

    @staticmethod
    def time_trial(n):
        a = [r.uniform(-DoublingTest.MAXIMUM_INTEGER, DoublingTest.MAXIMUM_INTEGER)
             for _ in range(n)]
        timer = StopWatch()
        ThreeSum.count(a)
        return timer.elapsed_time()


def main():
    n = 250
    while True:
        time = DoublingTest.time_trial(n)
        print(f'{n}     {time}')
        n += n


if __name__ == '__main__':
    main()