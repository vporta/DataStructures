"""
count.py
 *  Create an alphabet specified on the command line, read in a
 *  sequence of characters over that alphabet (ignoring characters
 *  not in the alphabet), computes the frequency of occurrence of
 *  each character, and print out the results.

 $ python string/count.py ABCDR < 'resources/abra.txt'
 *  A 5
 *  B 2
 *  C 1
 *  D 1
 *  R 2
"""
import sys
from string.Alphabet import Alphabet


class Count:

    @staticmethod
    def main(*args):
        args = list(*args)
        alphabet = Alphabet(args[0])
        R = alphabet.radix()
        count = [0] * R

        while not sys.stdin.isatty():
            for char in sys.stdin.readline():
                print(char)
                if alphabet.contains(char):
                    count[alphabet.to_index(char)] += 1
            for c in range(R):
                print(f'{alphabet.to_char(c)} {count[c]}')

            sys.exit()


if __name__ == '__main__':
    Count.main(sys.argv[1:])