"""
stopwatch_cpu.py
 *  A version of Stopwatch.java that measures CPU time on a single
 *  core or processor (instead of wall clock time).
 *  The StopwatchCPU data type is for measuring
 *  the CPU time used during a programming task.
"""
import time
import math


class StopwatchCPU:
    NANOSECONDS_PER_SECOND = 1000000000

    def __init__(self):
        self._start = time.process_time() * self.NANOSECONDS_PER_SECOND

    def elapsed_time(self):
        now = time.process_time() * self.NANOSECONDS_PER_SECOND
        return (now - self._start) / self.NANOSECONDS_PER_SECOND


def main():
    timer1 = StopwatchCPU()
    sum1 = 0.0
    n = 1000000
    for i in range(1, n + 1):
        sum1 += math.sqrt(i)
    time1 = timer1.elapsed_time()
    print(f'{sum1} ({time1} seconds)')

    timer2 = StopwatchCPU()
    sum2 = 0.0
    for i in range(1, n + 1):
        sum2 += math.pow(i, 0.5)
    time2 = timer2.elapsed_time()
    print(f'{sum2} ({time2} seconds)')


if __name__ == '__main__':
    main()

