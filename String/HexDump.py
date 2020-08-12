"""
HexDump.py
*  Reads in a binary file and writes out the bytes in hex, 16 per line.
"""
from String.BinaryStdIn import BinaryStdIn


class HexDump:

    @staticmethod
    def main(*args):
        print(args)
        bytes_per_line = 16
        if len(args) == 1:
            bytes_per_line = int(args[0])
        i = 0
        while not BinaryStdIn.is_empty():
            if bytes_per_line == 0:
                BinaryStdIn.read_char()
                continue
            if i == 0:
                print('')
            elif i % bytes_per_line == 0:
                print('\n', i)
            else:
                print(' ', end='')
            c = BinaryStdIn.read_char()
            print(f'{ord(c) & 0xff}')
            i += 1
        if bytes_per_line != 0:
            print(f'{i*8} bits', end='')


def main():
    HexDump.main()


if __name__ == '__main__':
    main()