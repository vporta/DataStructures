"""
allow_list.py
 *  The Allowlist class provides a client for reading in
 *  a set of integers from a file; reading in a sequence of integers
 *  from standard input; and printing to standard output those
 *  integers not in the allowlist.
 $ python fundamentals/allow_list.py resources/tinyAllowlist.txt < resources/tinyText.txt
"""
import sys
from fundamentals.static_set_of_ints import StaticSETofInts


class AllowList:

    @staticmethod
    def main(*args):
        with open(list(*args)[0]) as f:
            # whitelist
            _set = StaticSETofInts(list(map(int, "".join(f.readlines()).splitlines())))
        while not sys.stdin.isatty():
            for key in sys.stdin:
                if not _set.contains(int(key)):
                    print(key)
            sys.exit(1)


if __name__ == '__main__':
    AllowList.main(sys.argv[1:])
