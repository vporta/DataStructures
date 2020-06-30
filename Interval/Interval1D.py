"""
Interval1D.py
The Interval1D class represents a one-dimensional interval.
 *  The interval is closed — it contains both endpoints.
 *  Intervals are immutable: their values cannot be changed after they are created.
 *  The class Interval1D includes methods for checking whether
 *  an interval contains a point and determining whether two intervals intersect.
"""
import math


class MinEndPointComparator:

    @staticmethod
    def compare(a, b):
        if a.get_mini() < b.get_mini():
            return -1
        elif a.get_mini() > b.get_mini():
            return +1
        elif a.get_maxi() < b.get_maxi():
            return -1
        elif a.get_maxi() > b.get_maxi():
            return +1
        else:
            return 0


class MaxEndPointComparator:

    def compare(self, a, b):

        if a.get_maxi() < b.get_maxi():
            return -1
        elif a.get_maxi() > b.get_maxi():
            return +1
        elif a.get_mini() < b.get_mini():
            return -1
        elif a.get_mini() > b.get_mini():
            return +1
        else:
            return 0


class LengthComparator:

    def compare(self, a, b):
        a_len, b_len = len(a), len(b)
        if a_len < b_len:
            return -1
        elif a_len > b_len:
            return +1
        else:
            return 0


class Interval1D:
    MIN_ENDPOINT_ORDER = MinEndPointComparator()
    MAX_ENDPOINT_ORDER = MaxEndPointComparator()
    LENGTH_ORDER = LengthComparator()

    def __init__(self, mini, maxi):
        self.set_mini_and_maxi(mini, maxi)

    def get_mini(self):
        return self._mini

    def get_maxi(self):
        return self._maxi

    def set_mini_and_maxi(self, mini, maxi):
        if math.isinf(mini) or math.isinf(maxi):
            raise AttributeError('Endpoints must be Finite')
        if math.isnan(mini) or math.isnan(maxi):
            raise AttributeError('Endpoints cannot be NaN')
        if mini == 0.0:
            mini = 0.0
        if maxi == 0.0:
            maxi = 0.0
        if mini <= maxi:
            self._mini = mini
            self._maxi = maxi
        else:
            raise AttributeError('Illegal Interval')

    def intersects(self, that):
        if self.get_maxi() < that.get_mini():
            return False
        if that.get_maxi() < self.get_mini():
            return False
        return True

    def contains(self, x):
        """
        :type x: float
        :param x: the value
        :return: True if this interval contains the value x;
     *          false otherwise
        """
        return self.get_mini() <= x <= self.get_maxi()

    def length(self):
        return self.get_maxi() - self.get_mini()

    @classmethod
    def get_class(cls):
        return cls.__name__

    def equals(self, other):
        if other == self:
            return True
        if other is None:
            return False
        if self.get_class() != other.get_class():
            return False
        that = other
        return self.get_mini() == that.get_mini() and self.get_maxi() == that.get_maxi()

    def hash_code(self):
        hash_one, hash_two = hash(self.get_mini()), hash(self.get_maxi())
        return 31 * hash_one + hash_two

    def __str__(self):
        return f'minimum {self.get_mini()}, maximum {self.get_maxi()}'

    def __repr__(self):
        return f'<Interval1D(mini={self.get_mini()}, maxi={self.get_maxi()})>'


def main():
    intervals = [Interval1D(15.0, 33.0), Interval1D(45.0, 60.0), Interval1D(20.0, 70.0),
                 Interval1D(46.0, 55.0)]
    print('Unsorted')
    for i in range(len(intervals)):
        print(intervals[i])
    print()

    print(f'intersects: {intervals[0].intersects(intervals[2])}')
    print(f'contains: {intervals[0].contains(33.0)}')


if __name__ == '__main__':
    main()
