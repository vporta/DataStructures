"""
allow_filter.py
The AllowFilter class provides a client for reading in an allow_list
 *  of words from a file; then, reading in a sequence of words from standard input,
 *  printing out each word that appears in the file
"""
from search.p_set import SET


class AllowFilter:

    @staticmethod
    def run(*args):
        allow_list, word_file = args[0], args[1]
        st = SET()
        with open(allow_list) as f:
            for word in f.read().split(' '):
                # print(word)
                st.add(word)
        print()
        with open(word_file) as f1:
            for word in f1.read().split(' '):
                print(word)
                if st.contains(word):
                    print(word)

        print(st)


def main():
    allow_list = "../resources/list.txt"
    word_file = "../resources/tiny_tale.txt"
    AllowFilter.run(allow_list, word_file)


if __name__ == '__main__':
    main()