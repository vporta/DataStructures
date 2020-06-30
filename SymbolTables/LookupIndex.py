"""
LookupIndex.py

The LookupIndex class provides a data-driven client for reading in a
 *  key-value pairs from a file; then, printing the values corresponding to the
 *  keys found on standard input. Keys are strings; values are lists of strings.
 *  The separating delimiter is taken as a command-line argument. This client
 *  is sometimes known as an inverted index
"""
from collections import deque, defaultdict


class LookupIndex:

    @staticmethod
    def run(*args):
        file_name = args[0]
        separator = args[1]
        st, ts = defaultdict(deque), defaultdict(deque)
        with open(file_name) as f:
            for line in f.readlines():
                fields = "".join(line.split('\n')).split(separator)
                print(fields)
                key = fields[0]
                for i in range(1, len(fields)):
                    val = fields[i]
                    if key not in st:
                        st[key] = deque()
                    if val not in ts:
                        ts[val] = deque()
                    st.get(key).appendleft(val)
                    ts.get(val).appendleft(key)
        print('Done indexing')
        repeat_int = 1
        while repeat_int:
            query = input('Enter query: ')
            if query in st:
                for vals in st.get(query):
                    print(' ', vals)
            elif query in ts:
                for keys in st.get(query):
                    print(' ', keys)
            else:
                print('Not found')
            q = int(input('Press 1 to continue or 0 to quit: '))
            repeat_int = q
"""
LookupIndex.py

The LookupIndex class provides a data-driven client for reading in a
 *  key-value pairs from a file; then, printing the values corresponding to the
 *  keys found on standard input. Keys are strings; values are lists of strings.
 *  The separating delimiter is taken as a command-line argument. This client
 *  is sometimes known as an inverted index
"""
from collections import deque, defaultdict


class LookupIndex:

    @staticmethod
    def run(*args):
        file_name = args[0]
        separator = args[1]
        st, ts = defaultdict(deque), defaultdict(deque)
        with open(file_name) as f:
            for line in f.readlines():
                fields = "".join(line.split('\n')).split(separator)
                print(fields)
                key = fields[0]
                for i in range(1, len(fields)):
                    val = fields[i]
                    if key not in st:
                        st[key] = deque()
                    if val not in ts:
                        ts[val] = deque()
                    st.get(key).appendleft(val)
                    ts.get(val).appendleft(key)
        print('Done indexing')
        repeat_int = 1
        while repeat_int:
            query = input('Enter query: ')
            if query in st:
                for values in list(st[query]):
                    print(' ', values)
            elif query in ts:
                for keys in list(ts[query]):
                    print(' ', keys)
            else:
                print('Not found')
            q = int(input('Press 1 to continue or 0 to quit: '))
            repeat_int = q


def main():
    LookupIndex.run("../resources/ip.csv", ',')


if __name__ == '__main__':
    main()

