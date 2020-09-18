"""
stopwatch.py
 *  A utility class to measure the running time (wall clock) of a program.
 *  The Stopwatch data type is for measuring
 *  the time that elapses between the start and end of a
 *  programming task (wall-clock time).
 *
 *  See StopwatchCPU for a version that measures CPU time.
 *  For additional documentation,
"""
import time, math


class StopWatch:

    def __init__(self):
        self._start = int(time.time()) * 1000  # time in milli seconds

    def elapsed_time(self):
        now = int(time.time()) * 1000
        return (now - self._start) / 1000


def main():
    timer1 = StopWatch()
    sum1 = 0.0
    n = 10000000
    for i in range(1, n+1):
        sum1 += math.sqrt(i)
    time1 = timer1.elapsed_time()
    print(f'{sum1} ({time1} seconds)')

    timer2 = StopWatch()
    sum2 = 0.0
    for i in range(1, n + 1):
        sum2 += math.pow(i, 0.5)
    time2 = timer2.elapsed_time()
    print(f'{sum2} ({time2} seconds)')

if __name__ == '__main__':
    main()