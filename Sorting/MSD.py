"""
MSD.py
Sort an array of strings or integers using MSD radix sort.

"""


class MSD:
    BITS_PER_BYTE = 8
    BITS_PER_INT = 32
    R = 256
    CUTOFF = 15  # cutoff to insertion sort
    count = None

    @classmethod
    def sort(cls, a):
        n = len(a)
        aux = [''] * n
        cls.__sort(a, 0, n-1, 0, aux)

    @classmethod
    def __sort(cls, a, lo, hi, d, aux=None):
        if hi <= lo + cls.CUTOFF:
            cls.__insertion(a, lo, hi, d)
            return
        cls.count = [0 for _ in range(cls.R+2)]
        # compute frequency counts
        for i in range(lo, hi+1):
            c = cls._char_at(a[i], d)
            cls.count[c+2] += 1

        # transform counts to indices
        for r in range(cls.R+1):
            cls.count[r+1] = cls.count[r]

        # distribute
        for i in range(lo, hi+1):
            c = cls._char_at(a[i], d)
            aux[cls.count[c+1]] = a[i]
            cls.count[c + 1] += 1

        # copy back
        for i in range(lo, hi + 1):
            a[i] = aux[i - lo]

        for r in range(cls.R):
            cls.__sort(a, lo + cls.count[r], lo + cls.count[r+1], d+1, aux)

    @classmethod
    def _char_at(cls, s, d):
        assert 0 <= d <= len(s)
        if d == len(s):
            return -1
        return ord(s[d])

    @classmethod
    def __insertion(cls, a, lo, hi, d):
        for i in range(lo, hi+1):
            for j in range(i, lo, -1):
                if cls.__less(a[j], a[j - 1], d):
                    a[j], a[j-1] = a[j-1], a[j]

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
    with open("../Resources/shells.txt", ) as f:
        a = "".join(f.readlines()).splitlines()
        words = []
        w = len(a[0].split(' '))
        for line in a:
            assert w == len(line.split(' '))
            words.extend(line.split())
        MSD.sort(words)
        for item in words:
            print(item)


if __name__ == '__main__':
    main()