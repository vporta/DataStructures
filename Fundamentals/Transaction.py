"""
Transaction.py
 *  The Transaction class is an immutable data type to encapsulate a
 *  commercial transaction with a customer name, date, and amount.
"""
import math
from functools import cmp_to_key
from Fundamentals.Date import Date


class Transaction:

    def __init__(self, who, when, amount):
        if math.isnan(amount) or math.isinf(amount):
            raise AttributeError('Amount cannot be NaN or infinite')
        self._who = who
        self._when = when
        self._amount = float(amount)

    def who(self):
        return self._who

    def when(self):
        return self._when

    def amount(self):
        return self._amount

    def __str__(self):
        return f'{self._who} {self._when} {self._amount}'

    def __repr__(self):
        return f'{self._who} {self._when} {self._amount}'

    def __lt__(self, other):
        return self._amount < other.amount()

    def __gt__(self, other):
        return self._amount > other.amount()

    def __eq__(self, other):
        return self._amount == other.amount()

    def __ne__(self, other):
        return self._amount != other.amount()

    def __hash__(self):
        _hash = 1
        _hash = 31 * _hash + hash(self._who)
        _hash = 31 * _hash + hash(self._when)
        _hash = 31 * _hash + hash(self._amount)
        return _hash

    class WhoOrder:

        @staticmethod
        def compare(v, w):
            if v.who() < w.who():
                return -1
            elif v.who() > w.who():
                return +1
            else:
                return 0

    class WhenOrder:

        @staticmethod
        def compare(v, w):
            if v.when() < w.when():
                return -1
            elif v.when() > w.when():
                return +1
            else:
                return 0

    class HowMuchOrder:

        @staticmethod
        def compare(v, w):
            pass


def main():
    a = [None] * 4
    a[0] = Transaction('Turing',   Date(6, 17, 1990),  644.08)
    a[1] = Transaction('Tarjan',   Date(3, 26, 2002), 4121.85)
    a[2] = Transaction('Knuth',    Date(6, 14, 1999),  288.34)
    a[3] = Transaction('Dijkstra', Date(8, 22, 2007), 2678.40)

    print('Unsorted')
    for i in range(len(a)):
        print(a[i])
    print()
    print('Sort by date')
    a = sorted(a, key=cmp_to_key(lambda item1, item2: Transaction.WhenOrder.compare(item1, item2)))
    print(a)


if __name__ == '__main__':
    main()


