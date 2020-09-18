"""
suffix_array.py
A data type that computes the suffix array of a string.
The SuffixArray class represents a suffix array of a string of
 *  length n.
 *  It supports the selecting the ith smallest suffix,
 *  getting the index of the ith smallest suffix,
 *  computing the length of the longest common prefix between the
 *  ith smallest suffix and the i-1st smallest suffix,
 *  and determining the rank of a query string (which is the number
 *  of suffixes strictly less than the query string).
 *
 *  This implementation uses a nested class Suffix to represent
 *  a suffix of a string (using constant time and space)
 *  The index and length operations takes constant time
 *  in the worst case.
 *  The lcp operation takes time proportional to the
 *  length of the longest common prefix.
 *  The select operation takes time proportional
 *  to the length of the suffix and should be used primarily for debugging.
 *
"""


class SuffixArray:

    def __init__(self, text):
        n = len(text)
        self._suffixes = [SuffixArray._Suffix()] * n
        for i in range(n):
            self._suffixes[i] = SuffixArray._Suffix(text, i)

        self._suffixes.sort()

    class _Suffix:

        def __init__(self, text=None, index=None):
            self.text = text
            self.index = index

        def length(self):
            return len(self.text) - self.index

        def char_at(self, i):
            return self.text[self.index + i]

        def __lt__(self, other):
            n = min(self.length(), other.length())
            for i in range(n):
                if self.char_at(i) < other.char_at(i):
                    return True
            return False

        def __gt__(self, other):
            n = min(self.length(), other.length())
            for i in range(n):
                if self.char_at(i) > other.char_at(i):
                    return True
            return False

        def __eq__(self, other):
            n = min(self.length(), len(other))
            for i in range(n):
                if self.char_at(i) == other[i]:
                    return True
            return False

        def __repr__(self):
            return f'<{self.__class__.__name__}(text={self.text}, index={self.index})>'

        def __str__(self):
            return self.text[self.index]

    def length(self):
        return len(self._suffixes)

    def index(self, i):
        if i < 0 or i >= len(self._suffixes):
            raise AttributeError(f'i cannot be less than 0 or greater than or equal to length of {self._suffixes}')
        return self._suffixes[i].index

    def lcp(self, i):
        # the length of the longest common prefix of the i-th smallest suffix
        if i < 1 or i >= len(self._suffixes):
            raise AttributeError(f'i {i} must be between 1 and {len(self._suffixes)}')
        return self.__lcp_suffix(self._suffixes[i], self._suffixes[i - 1])

    def __lcp_suffix(self, s, t):
        n = min(s.length(), t.length())
        for i in range(n):
            if s.char_at(i) != t.char_at(i):
                return i
        return n

    def select(self, i):
        if i < 0 or i >= len(self._suffixes):
            raise AttributeError(f'i {i} must be between 1 and {len(self._suffixes)}')
        return self._suffixes[i]

    def rank(self, query):
        lo, hi = 0, len(self._suffixes) - 1
        while lo <= hi:
            mid = (hi + lo) // 2
            cmp = self.__compare(query, self._suffixes[mid])
            if cmp < 0:
                hi = mid - 1
            elif cmp > 0:
                lo = mid + 1
            else:
                return mid
        return lo

    def __compare(self, query, suffix):
        n = min(len(query), suffix.length())
        for i in range(n):
            if query[i] < suffix.char_at(i):
                return -1
            if query[i] > suffix.char_at(i):
                return 1
        return len(query) - suffix.length()

    def __repr__(self):
        return f'<{self.__class__.__name__}(_suffixes={self._suffixes})>'


def main():
    s = 'ABRACADABRA!'
    suffix = SuffixArray(s)
    print(suffix)
    print('i ind lcp rnk select')
    print('--------------------')

    for i in range(len(s)):
        index = suffix.index(i)
        ith = f'{s[index: min(index + 50, len(s))]}'
        assert s[index:] == suffix.select(i)
        rank = suffix.rank(s[index])

        if i == 0:
            print(f'{i}, {index}, "-", {rank}, {ith}')
        else:
            lcp = suffix.lcp(i)
            print(f'{i}, {index}, {lcp}, {rank}, {ith}')


if __name__ == '__main__':
    main()