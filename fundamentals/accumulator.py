"""
accumulator.py
 *  The Accumulator class is a data type for computing the running
 *  mean, sample standard deviation, and sample variance of a stream of real
 *  numbers. It provides an example of a mutable data type and a streaming
 *  algorithm.
 *
 *  This implementation uses a one-pass algorithm that is less susceptible
 *  to floating-point roundoff error than the more straightforward
 *  implementation based on saving the sum of the squares of the numbers.
 *  This technique is due to https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Online_algorithm"
 *  Each operation takes constant time in the worst case.
 *  The amount of memory is constant - the data values are not stored.
"""
import math
import sys


class Accumulator:

    _n = 0  # number of data values
    _sum = 0.0  # sample variance * (n-1)
    _mu = 0.0  # sample mean

    def __init__(self):
        pass

    def add_data_value(self, x):
        self._n += 1
        delta = x - self._mu
        self._mu += delta / self._n
        self._sum += (self._n - 1) / self._n * delta * delta

    def mean(self):
        return self._mu

    def variance(self):
        if self._n <= 1:
            return float('NaN')
        return self._sum / (self._n - 1)

    def stddev(self):
        return math.sqrt(self.variance())

    def count(self):
        return self._n

    def __str__(self):
        return f"n = {self._n}, mean = {self.mean()}, stddev = {self.stddev()}"


def main():
    stats = Accumulator()
    real_nums = [32.45, 68.22, 78.56, 5.39, 92.64]
    for num in real_nums:
        stats.add_data_value(num)
    print(stats)
    print(f'n   = {stats.count()}')
    print(f'mean   = {stats.mean()}')
    print(f'stddev   = {stats.stddev()}')
    print(f'variance   = {stats.variance()}')


if __name__ == '__main__':
    main()