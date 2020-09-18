"""
run_length.py
 *  Compress or expand binary input from standard input using
 *  run-length encoding.

 * This has runs of 15 0s, 7 1s, 7 0s, and 11 1s.
 * $ python string/run_length.py - < resources/4runs.bin | python string/hex_dump.py
"""
from string.BinaryStdIn import BinaryStdIn
from string.BinaryStdOut import BinaryStdOut
import sys


class RunLength:
    R = 256
    LG_R = 8

    @classmethod
    def expand(cls):
        b = False
        while not BinaryStdIn.is_empty():
            run = BinaryStdIn.read_int_r(cls.LG_R)
            for i in range(run):
                BinaryStdOut.write_bool(b)
            b = not b
        BinaryStdOut.close()

    @classmethod
    def compress(cls):
        run = 0
        old = False

        while not BinaryStdIn.is_empty():
            b = BinaryStdIn.read_bool()
            if b != old:
                BinaryStdOut.write_int(run, cls.LG_R)
                run = 1
                old = not old
            else:
                if run == cls.R - 1:
                    BinaryStdOut.write_int(run, cls.LG_R)
                    run = 0
                    BinaryStdOut.write_int(run, cls.LG_R)
                run += 1

        BinaryStdOut.write_int(run, cls.LG_R)
        BinaryStdOut.close()


def main():
    if sys.argv[1] == '-':
        RunLength.compress()
    elif sys.argv[1] == '+':
        RunLength.expand()
    else:
        raise Exception(f'Illegal commandline argument.  {sys.argv[1]}')


if __name__ == '__main__':
    main()
