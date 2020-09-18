"""
longest_common_substring.py
 *  Read in two text files and find the longest substring that
 *  appears in both texts.
"""
from string.SuffixArray import SuffixArray


class LongestCommonSubstring:

    @classmethod
    def __lcp(cls, s, p, t, q):
        # return the longest common prefix of suffix s[p..] and suffix t[q..]
        n = min(len(s) - p, len(t) - q)
        for i in range(n):
            if s[p + i] != t[q + i]:
                return s[p:p + i]
        return s[p:p + n]

    @classmethod
    def __compare(cls, s, p, t, q):
        n = min(len(s) - p, len(t) - q)
        for i in range(n):
            if s[p + i] != t[q + i]:
                return s.index(s[p + i]) - t.index(t[q + i])
        if len(s) - p < len(t) - q:
            return -1
        elif len(s) - p > len(t) - q:
            return 1
        else:
            return 0

    @classmethod
    def lcs(cls, s, t):
        n = len(s)
        m = len(t)
        suffix1 = sorted([s[i:n] for i in range(n)])
        suffix2 = sorted([t[i:m] for i in range(m)])
        lcs = ''
        i, j = 0, 0
        while i < n and j < m:
            p = suffix1.index(suffix1[i])
            q = suffix2.index(suffix2[j])
            x = cls.__lcp(s, p, t, q)
            if len(x) > len(lcs):
                lcs = x
            if cls.__compare(s, p, t, q) < 0:
                i += 1
            else:
                j += 1

        return lcs


def main():
    s = 'jdnjncdn cjencjne seemed on the point of being ewnencnecece'
    t = 'gnrtnvrnvnnvr ccc seemed on the point of being mkmkmkvnbvvt'
    print(LongestCommonSubstring.lcs(s, t))


if __name__ == '__main__':
    main()