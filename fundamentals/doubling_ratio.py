"""
doubling_ratio.py
 *  The DoublingRatio class provides a client for measuring
 *  the running time of a method using a doubling ratio test.
"""
import random as r
from fundamentals.stopwatch import StopWatch
from fundamentals.three_sum import ThreeSum


class DoublingRatio:
    MAXIMUM_INTEGER = 1000000

    @staticmethod
    def time_trial(n):
        a = [r.uniform(-DoublingRatio.MAXIMUM_INTEGER, DoublingRatio.MAXIMUM_INTEGER)
             for _ in range(n)]
        timer = StopWatch()
        ThreeSum.count(a)
        return timer.elapsed_time()


def main():
    prev = DoublingRatio.time_trial(125)
    n = 250
    while True:
        time = DoublingRatio.time_trial(n)
        print(f'{n}     {time}     {time/prev if prev != 0 else prev}')
        prev = time
        n += n


if __name__ == '__main__':
    main()