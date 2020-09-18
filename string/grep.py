"""
grep.py
 *  This program takes an RE as a command-line argument and prints
 *  the lines from standard input having some substring that
 *  is in the language described by the RE.
 *  The GREP class provides a client for reading in a sequence of
 *  lines and printing to standard output those lines
 *  that contain a substring matching a specified regular expression.
"""
from string.NFA import NFA


class GREP:

    @staticmethod
    def main(**kwargs):
        file = kwargs.get('file')
        regex = kwargs.get('regex')
        nfa = NFA(regex)
        with open(f'../resources/{file}') as f:
            for line in f.readlines():
                if nfa.recognizes(line):
                    print(line)


if __name__ == '__main__':
    GREP.main(regex="(A*B|AC)D", file='tinyL.txt')

