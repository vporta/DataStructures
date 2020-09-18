"""
inplace_msd.py
Sort an array of strings or integers using in-place MSD radix sort.
"""
from sorting.msd import MSD


class InplaceMSD:

    R = 256
    CUTOFF = 15
    
    @classmethod
    def sort(cls, a):
        n = len(a)
        cls.__sort(a, 0, n-1, 0)

    @classmethod
    def __sort(cls, a, lo, hi, d):

        # cutoff to insertion sort for small sub-arrays
        if hi <= lo + cls.CUTOFF:
            cls.__insertion(a, lo, hi, d)
            return

        # compute frequency counts
        heads = [0] * (cls.R + 2)
        tails = [0] * (cls.R + 1)
        for i in range(lo, hi+1):  # from lo to i <= hi
            c = cls._char_at(a[i], d)
            heads[c + 2] += 1

        # transform counts to indices
        heads[0] = lo
        for r in range(cls.R+1):
            heads[r + 1] = heads[r]
            tails[r] = heads[r + 1]

        # sort by d-th character in-place
        for r in range(cls.R + 1):
            while heads[r] < tails[r]:
                c = cls._char_at(a[heads[r]], d)
                while c + 1 != r:
                    a[heads[c + 1]] += 1
                    a[heads[r]], a[heads[c+1]] = a[heads[c+1]], a[heads[r]]
                    c = cls._char_at(a[heads[r]], d)
                heads[r] += 1

        # recursively sort for each character (excludes sentinel -1)
        for r in range(cls.R):
            cls.__sort(a, tails[r], tails[r + 1], d+1)

    @classmethod
    def _char_at(cls, s, d):
        assert 0 <= d <= len(s)
        if d == len(s):
            return -1
        return ord(s[d])

    @classmethod
    def __insertion(cls, a, lo, hi, d):
        for i in range(lo, hi + 1):
            for j in range(i, lo, -1):
                if cls.__less(a[j], a[j - 1], d):
                    a[j], a[j - 1] = a[j - 1], a[j]

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


def main():
    with open("../resources/shells.txt", ) as f:
        a = "".join(f.readlines()).splitlines()
        words = []
        w = len(a[0].split(' '))
        for line in a:
            words.extend(line.split())
        InplaceMSD.sort(words)
        for item in words:
            print(item)


if __name__ == '__main__':
    main()