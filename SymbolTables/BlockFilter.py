"""
BlockFilter.py
The BlockFilter class provides a client for reading in an block_list
 *  of words from a file; then, reading in a sequence of words from standard input,
 *  printing out each word that appears in the file
"""
from SymbolTables.SET import SET


class BlockFilter:

    @staticmethod
    def run(*args):
        block_list, word_file = args[0], args[1]
        st = SET()
        with open(block_list) as f:
            for word in f.read().split(' '):
                # print(word)
                st.add(word)
        print()
        with open(word_file) as f1:
            for word in f1.read().split(' '):
                print(word)
                if not st.contains(word):
                    print(word)

        print(st)


def main():
    block_list = "../Resources/list.txt"
    word_file = "../Resources/tiny_tale.txt"
    BlockFilter.run(block_list, word_file)


if __name__ == '__main__':
    main()
