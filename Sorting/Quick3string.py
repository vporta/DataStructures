"""
Quick3string.py
Reads string from standard input and 3-way string quicksort them.
"""
import random


class Quick3String:
    CUTOFF = 15

    @classmethod
    def sort(cls, a):
        random.shuffle(a)
        n = len(a)
        cls.__sort(a, 0, n - 1, 0)
        assert cls.__is_sorted(a)

    @classmethod
    def __sort(cls, a, lo, hi, d):
        if hi <= lo + cls.CUTOFF:
            cls.__insertion(a, lo, hi, d)
            return

        lt, gt = lo, hi
        v = cls.__char_at(a[lo], d)
        i = lo + 1
        while i <= gt:
            t = cls.__char_at(a[i], d)
            if t < v:
                lt += 1
                i += 1
                a[i], a[lt] = a[lt], a[i]
            elif t > v:
                gt -= 1
                a[i], a[gt] = a[gt], a[i]
            else:
                i += 1

        # a[lo..lt-1] < v = a[lt..gt] < a[gt+1..hi].
        cls.__sort(a, lo, lt-1, d)
        if v >= 0:
            cls.__sort(a, lt, gt, d+1)
        cls.__sort(a, gt+1, hi, d)

    @classmethod
    def __char_at(cls, s, d):
        assert 0 <= d <= len(s)
        if d == len(s):
            return -1
        return ord(s[d])

    @classmethod
    def __less(cls, v, w, d):
        i = d
        while i < min(len(v), len(w)):
            if v[i] < w[i]:
                return True
            if v[i] > w[i]:
                return False
            i += 1
        return len(v) < len(w)

    @classmethod
    def __insertion(cls, a, lo, hi, d):
        for i in range(lo, hi + 1):
            for j in range(i, lo, -1):
                if cls.__less(a[j], a[j - 1], d):
                    a[j], a[j - 1] = a[j - 1], a[j]

    @classmethod
    def __is_sorted(cls, a):
        for i in range(1, len(a)):
            if a[i] < a[i - 1]:
                return False
        return True


def main():
    with open("../resources/shells.txt", ) as f:
        a = "".join(f.readlines()).splitlines()
        words = []
        w = len(a[0].split(' '))
        for line in a:
            assert w == len(line.split(' '))
            words.extend(line.split())
        Quick3String.sort(words)
        for item in words:
            print(item)


if __name__ == '__main__':
    main()