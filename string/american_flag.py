"""
american_flag.py
Sort an array of strings or integers in-place using American flag sort.
$ python string/american_flag.py < resources/shells.txt
"""
import sys
from typing import List
from queue import LifoQueue


class AmericanFlag:
    BITS_PER_BYTE = 8
    BITS_PER_INT = 32
    R = 256
    CUTOFF = 15

    @staticmethod
    def _char_at(s: str, d: int):
        assert 0 <= d <= len(s)
        if d == len(s):
            return -1
        return s[d]

    @staticmethod
    def sort_str(a: List[str]):
        AmericanFlag._sort_str(a, 0, len(a) - 1)

    @staticmethod
    def _sort_str(a: List[str], lo: int, hi: int):
        st: LifoQueue[int] = LifoQueue()
        first: List[int] = [0] * (AmericanFlag.R + 2)
        next_: List[int] = [0] * (AmericanFlag.R + 2)
        d = 0
        st.put(lo)
        st.put(hi)
        st.put(d)

        while not st.empty():
            d = st.get()
            hi = st.get()
            lo = st.get()
            if hi <= lo + AmericanFlag.CUTOFF:
                AmericanFlag._insertion(a, lo, hi, d)
                continue
            # compute freq counts
            for i in range(lo, hi+1):
                c = AmericanFlag._char_at(a[i], d) + 1
                first[c + 1] += 1

            # first[c] = location of first string whose dth character = c
            first[0] = lo
            for c in range(AmericanFlag.R + 1):
                first[c + 1] += first[c]
                if c > 0 and first[c + 1] - 1 > first[c]:
                    st.put(first[c])
                    st.put(first[c + 1] - 1)
                    st.put(d + 1)
            # next[c] = location to place next string whose dth character = c
            for c in range(AmericanFlag.R + 2):
                next_[c] = first[c]

            # permute data in place
            for k in range(lo, hi + 1):
                c: int = AmericanFlag._char_at(a[k], d) + 1
                while first[c] > k:
                    next_[c] += 1
                    AmericanFlag._exch(a, k, next_[c])
                    c = AmericanFlag._char_at(a[k], d) + 1
                next_[c] += 1

            # clear first[] and next[] arrays
            for c in range(AmericanFlag.R + 2):
                first[c] = 0
                next_[c] = 0

    @staticmethod
    def _insertion(a: List[str], lo: int, hi: int, d: int):
        for i in range(lo, hi + 1):
            for j in range(i, lo, -1):
                if AmericanFlag._less(a[j], a[j - 1], d):
                    AmericanFlag._exch(a, j, j - 1)

    @staticmethod
    def _exch(a: List[str], i: int, j: int):
        a[i], a[j] = a[j], a[i]

    @staticmethod
    def _less(v: str, w: str, d: int):
        for i in range(d, min(len(v), len(w))):
            if v[i] < w[i]:
                return True
            if v[i] > w[i]:
                return False
        return len(v) < len(w)


def main():
    while not sys.stdin.isatty():
        a: List[str] = "".join(sys.stdin.readlines()).split()
        AmericanFlag.sort_str(a)
        for i in range(len(a)):
            print(a[i])
        sys.exit()


if __name__ == '__main__':
    main()