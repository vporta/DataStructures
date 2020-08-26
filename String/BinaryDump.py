"""
BinaryDump.py
 *  Reads in a binary file and writes out the bits, n per line.
 *  python String/BinaryDump.py 16 < Resources/abra.txt
"""
from String.BinaryStdIn import BinaryStdIn


class BinaryDump:

    @staticmethod
    def main(*args):
        print(args)
        bits_per_line = 16
        if len(args) == 1:
            bits_per_line = int(args[0])
        i = 0
        while not BinaryStdIn.is_empty():
            if bits_per_line == 0:
                BinaryStdIn.read_bool()
                continue
            elif i != 0 and i % bits_per_line == 0:
                print('')
            if BinaryStdIn.read_bool():
                print(1, end='')
            else:
                print(0, end='')
            i += 1
        if bits_per_line != 0:
            print('\n')
        print(f'{i} bits')


def main():
    BinaryDump.main()


if __name__ == '__main__':
    main()