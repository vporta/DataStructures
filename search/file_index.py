"""
file_index.py

"""

from search.p_set import SET
from collections import defaultdict


class FileIndex:

    @staticmethod
    def run(*args):
        args = str(*args).split(' ')
        st = defaultdict(SET)
        print(
            'Indexing Files ...'
        )
        print(args)
        for file_name in args[0:len(args)-1]:
            print(f' {file_name}')
            with open(f'../resources/{file_name}.txt') as f:
                for word in f.read().split(' '):
                    print(word)
                    if word not in st:
                        st[word] = SET()
                    _set = st[word]
                    _set.add(f.name)
        repeat = 1
        while repeat:
            query = input(
                'Enter Query:  '
            )
            # global cont
            if query in st:
                _set = st[query]
                print(_set)
                for file in _set.iterator():
                    print(file)
            else:
                print('Not found')
            inp = int(input('Press 1 to repeat the program or 0 to quit.'))
            repeat = inp


def main():
    inp = input('Enter:  ')
    FileIndex.run(inp)


if __name__ == '__main__':
    main()
