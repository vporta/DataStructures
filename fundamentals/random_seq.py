"""
random_seq.py
$ python fundamentals/random_seq.py 5 100.0 200.0
"""
import random as r
import sys


class RandomSeq:

    @staticmethod
    def main(*args):
        a = list(*args)
        n = int(a[0])
        if len(a) == 1:
            for i in range(n):
                x = r.uniform(0, 1)
                print(x)
        elif len(a) == 3:
            lo = float(a[1])
            hi = float(a[2])
            for i in range(n):
                x = r.uniform(lo, hi)
                print(x)
        else:
            raise AttributeError('Invalid number of arguments')


if __name__ == '__main__':
    RandomSeq.main(sys.argv[1:])