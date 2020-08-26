"""
Cat.py
"""
import sys


class Cat:

    @staticmethod
    def main(*args):
        a = list(*args)
        out = a[len(a) - 1]
        h = open(f'../Resources/{out}', 'w')
        for i in range(len(a) - 1):
            with open(f'../Resources/{a[i]}') as f:
                s = f.read()
                h.write(s)
                f.close()
        h.close()


if __name__ == '__main__':
    Cat.main(sys.argv[1:])
