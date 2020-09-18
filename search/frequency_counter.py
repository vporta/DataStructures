"""
frequency_counter.py
 *  Read in a list of words from standard input and print out
 *  the most frequently occurring word that has length greater than
 *  a given threshold.
 *
 $  python search/frequency_counter.py 1 < 'resources/tiny_tale.txt'
 *  it 10
 *
 *  The FrequencyCounter class provides a client for
 *  reading in a sequence of words and printing a word (exceeding
 *  a given length) that occurs most frequently. It is useful as
 *  a test client for various symbol table implementations.
"""
import sys
from search.st import ST


class FrequencyCounter:

    @staticmethod
    def main(*args):
        args = list(*args)
        distinct, words = 0, 0
        min_len = int(args[0])
        st = ST()
        while not sys.stdin.isatty():
            for key in sys.stdin.readline().split():
                if len(key) < min_len:
                    continue
                words += 1
                if st.contains(key):
                    st.put(key, st.get(key) + 1)
                else:
                    st.put(key, 1)
                    distinct += 1

            _max = ''
            st.put(_max, 0)
            for word in st.keys():
                if st.get(word) > st.get(_max):
                    _max = word
                print(f'{_max}     {st.get(_max)}')
                print(f'distinct = {distinct}')
                print(f'words = {words}')
            sys.exit()


if __name__ == '__main__':
    FrequencyCounter.main(sys.argv[1:])
