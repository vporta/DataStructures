"""
Date.py
 *  The Date class is an immutable data type to encapsulate a
 *  date (day, month, and year).
"""


class Date:

    DAYS = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, month, day, year):
        if not Date._is_valid(month, day, year):
            raise AttributeError('Invalid date')
        self._month = month
        self._day = day
        self._year = year 

    def month(self):
        return self._month

    def day(self):
        return self._day

    def year(self):
        return self._year

    @staticmethod
    def _is_valid(m, d, y):
        if m < 1 or m > 12:
            return False
        if d < 1 or d > Date.DAYS[m]:
            return False
        if m == 2 and d == 29 and not Date.is_leap_year(y):
            return False
        return True

    @staticmethod
    def is_leap_year(y):
        if y % 400 == 0:
            return True
        if y % 100 == 0:
            return False
        return y % 4 == 0

    def nxt(self):
        if Date._is_valid(self._month, self._day + 1, self._year):
            return Date(self._month, self._day + 1, self._year)
        elif Date._is_valid(self._month + 1, 1, self._year):
            return Date(self._month + 1, 1, self._year)
        else:
            return Date(1, 1, self._year + 1)

    def is_after(self, other):
        return self > other

    def is_before(self, other):
        return self < other

    def __lt__(self, other):
        if self._year < other.year() or \
                self._month < other.month() or \
                self._day < other.day():
            return -1

    def __gt__(self, other):
        if self._year > other.year() or \
                self._month > other.month() or \
                self._day > other.day():
            return +1

    def __eq__(self, other):
        if self._year == other.year() and \
                self._month == other.month() and \
                self._day == other.day():
            return 0

    def __str__(self):
        return f'{self._month}/{self._day}/{self._year}'

    def __hash__(self):
        return self._day + 31 * self._month + 31 * 12 * self._year


def main():
    month, day, year = 8, 24, 2020
    today = Date(month, day, year)
    print(today)
    print(f'hash = {day} + 31 * {month} + 31 * 12 * {year} = {hash(today)}')
    for _ in range(10):
        today = today.nxt()
        print(today)
    print(today.is_after(today.nxt()))
    print(today.is_after(today))
    print(today.nxt().is_after(today))


if __name__ == '__main__':
    main()