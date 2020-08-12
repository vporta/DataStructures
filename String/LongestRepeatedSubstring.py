"""
LongestRepeatedSubstring.py
 *  Reads a text string, then computes the longest
 *  repeated substring in that text using a suffix array.
"""


class LongestRepeatedSubstring:

    @classmethod
    def lcp(cls, i, suffixes):
        # the length of the longest common prefix of the i-th smallest suffix
        if i < 1 or i >= len(suffixes):
            raise AttributeError(f'i {i} must be between 1 and {len(suffixes)}')
        return cls.__lcp_suffix(suffixes[i], suffixes[i - 1])

    @classmethod
    def __lcp_suffix(cls, s, t):
        n = min(len(s), len(t))
        for i in range(n):
            if s[i] != t[i]:
                return i
        return n

    @classmethod
    def lrs(cls, text):
        # longest repeated substring
        n = len(text)
        # create suffixes array and sort it in asc order
        suffixes = sorted([text[i:n] for i in range(n)])
        # find longest common prefix between adjacent suffixes
        lrs = ''
        for i in range(1, n-1):
            length = cls.lcp(i, suffixes)
            if length > len(lrs):
                lrs = suffixes[i][0:length]
        return lrs


def main():
    s = 'ABRACADABRA!'
    print(f'  {LongestRepeatedSubstring.lrs(s)}  ')


if __name__ == '__main__':
    main()

