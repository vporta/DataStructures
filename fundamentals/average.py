"""
average.py
$ python fundamentals/average.py 10.0 5.0 6.0
"""
import sys


class Average:

    @staticmethod
    def main(*args):
        count, _sum = 0, 0.0
        a = list(*args)
        while count < len(a):
            value = float(a[count])
            _sum += value
            count += 1
        average = _sum / count
        print(f'average is {average}')


if __name__ == '__main__':
    Average.main(sys.argv[1:])