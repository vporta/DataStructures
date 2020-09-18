"""
american_flag_x.py
Sort an array of strings or integers in-place using American flag sort. Non-recursive.
$ python string/american_flag_x.py < resources/shells.txt
"""
import sys
from typing import List
from queue import LifoQueue


class AmericanFlagX:
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
        AmericanFlagX._sort_str(a, 0, len(a) - 1)

    @staticmethod
    def _sort_str(a: List[str], lo: int, hi: int):
        st: LifoQueue[int] = LifoQueue()
        count: List[int] = [0] * (AmericanFlagX.R + 1)
        d = 0
        st.put(lo)
        st.put(hi)
        st.put(d)

        while not st.empty():
            d = st.get()
            hi = st.get()
            lo = st.get()
            if hi <= lo + AmericanFlagX.CUTOFF:
                AmericanFlagX._insertion(a, lo, hi, d)
                continue
            # compute freq counts
            for i in range(lo, hi + 1):
                c = AmericanFlagX._char_at(a[i], d) + 1
                count[c] += 1

            # accumulate counts relative to a[0], so that
            # count[c] is the number of keys <= c
            count[0] += lo
            for c in range(AmericanFlagX.R):
                count[c + 1] += count[c]
                if c > 0 and count[c + 1] - 1 > count[c]:
                    st.put(count[c])
                    st.put(count[c + 1] - 1)
                    st.put(d + 1)
            # next[c] = location to place next string whose dth character = c
            for r in range(hi, lo + 1, -1):
                # locate element that must be shifted right of r
                c: int = AmericanFlagX._char_at(a[r], d) + 1
                while r >= lo and count[c - 1] <= r:
                    if count[c] - 1 == r:
                        count[c] -= 1
                    r -= 1
                    if r >= lo:
                        c = AmericanFlagX._char_at(a[r], d) + 1
                # if r < lo the subarray is sorted
                if r < lo:
                    break
                # permute a[r] until correct element is in place
                # python v 3.8+ (count[c]:= count[c] - 1)
                count[c] -= 1
                while count[c] != r:
                    AmericanFlagX._exch(a, r, count[c])
                    c = AmericanFlagX._char_at(a[r], d) + 1

            # clear count[] and next[] arrays
            for c in range(AmericanFlagX.R + 1):
                count[c] = 0

    @staticmethod
    def _insertion(a: List[str], lo: int, hi: int, d: int):
        for i in range(lo, hi + 1):
            for j in range(i, lo, -1):
                if AmericanFlagX._less(a[j], a[j - 1], d):
                    AmericanFlagX._exch(a, j, j - 1)

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
        AmericanFlagX.sort_str(a)
        for i in range(len(a)):
            print(a[i])
        sys.exit()


if __name__ == '__main__':
    main()
