"""
concordance.py
The Concordance class reads text input from a file and builds an index. Then it
processes queries and prints concordances:
$ Enter Query: worst
> it was the **worst** of times it

"""

from search.p_set import SET
from collections import defaultdict


class Concordance:

    @staticmethod
    def run():
        with open(f'../resources/tiny_tale.txt') as f:
            words = " ".join(f.read().split('\n')).split(' ')
            st = defaultdict(SET)  # symbol table
            for i, word in enumerate(words):
                if word not in st:
                    st[word] = SET()
                _set = st[word]
                _set.add(i)
        print(st)
        repeat = 1
        while repeat:
            query = input(
                'Enter Query: '
            )
            if query in st:
                _set = st[query]
                for k in _set.iterator():
                    print(
                        f'{words[k - 3]} '
                        f'{words[k - 2]} '
                        f'{words[k - 1]}'
                        f' **{words[k]}** '
                        f'{words[k + 1]} '
                        f'{words[k + 2]} '
                        f'{words[k + 3]}'
                    )
            else:
                print('Not found')
            inp = int(input('Press 1 to repeat the program or 0 to quit: '))
            repeat = inp


def main():
    Concordance.run()


if __name__ == '__main__':
    main()
