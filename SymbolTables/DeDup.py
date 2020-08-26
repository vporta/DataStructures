"""
The DeDup class provides a client for reading in a sequence of
 *  words from standard input and printing each word, removing any duplicates.
 *  It is useful as a test client for various symbol table implementations.
"""


class DeDup:

    @staticmethod
    def run():
        _set = set()
        with open("../Resources/tiny_tale.txt") as f:
            words = " ".join(f.read().split('\n')).split(' ')
            print(words)
            for key in words:
                if key not in _set:
                    _set.add(key)
                print(key)


def main():
    DeDup.run()


if __name__ == '__main__':
    main()