"""
 * RabinKarp.py
 * Time complexity for Monte Carlo and Las Vegas versions:
    *    7N or O(N) average and guaranteed runtime/operation count
    *    O(1) space
 * Monte Carlo does not do backup in input.
 * Las Vegas version does backup in input.
 * Las Vegas in guaranteed to be correct, but runs in M*N worst case.
 * Monte Carlo is likely to be correct for a large enough prime Q. 1/Q probability of a collision to occur.
"""


class RabinKarp:

    def __init__(self, pat):
        """
        Pre-processes the pattern string
        :param pat: pat the pattern string 
        """
        self.pat = pat
        self.R = 256
        self.m = len(pat)
        self.q = 101  # prime (not long enough for practical purposes)

        # pre-compute R ^ (m-1) % q for use in removing leading digit
        self.RM = 1
        self.pat_hash = None
        i = 1
        while i <= self.m - 1:
            self.RM = (self.R * self.RM) % self.q
            i += 1
        self.pat_hash = self._hash(pat, self.m)

    def _hash(self, key, m):
        """
        Compute hash for key[0..m-1]
        :param key: key string pattern 
        :param m: m length of pattern 
        """
        h = 0
        for j in range(m):
            h = (self.R * h + ord(key[j])) % self.q
        return h

    def _check(self, txt, i):
        """
        Las Vegas version: does pat match txt[i..i-m+1]
        :param txt: txt the string text to be compared 
        :param i: i the index of string txt 
        :returns: true, if there's a match, otherwise false
        """
        for j in range(self.m):
            if self.pat[j] != txt[i + j]:
                return False
        return True

        # Monte Carlo Version: always returns True

    # def _check(self, i):
    #     return True 

    def search(self, txt):
        """
        Returns the index of the first occurrence of the pattern string
        in the text string.
        :param txt: txt the text string 
        :returns: the index of the first occurrence of the pattern string in the text string; n if no such match
        """
        n = len(txt)
        if n < self.m:
            return n
        txt_hash = self._hash(txt, self.m)

        # check for match at offset 0 
        if self.pat_hash == txt_hash and self._check(txt, 0):
            return 0
        i = self.m
        while i < n:
            # remove leading digit, add trailing digit, check for match 
            txt_hash = (txt_hash + self.q - self.RM * ord(txt[i - self.m]) % self.q) % self.q
            txt_hash = (txt_hash * self.R + ord(txt[i])) % self.q

            # match 
            offset = i - self.m + 1
            if self.pat_hash == txt_hash and self._check(txt, offset):
                return offset
            i += 1
            # no match
        return n

    def __repr__(self):
        return f'<RabinKarp(pat={self.pat})>'


def main():
    import sys
    print(sys.argv)
    pat, txt = None, None
    if len(sys.argv) == 3:
        pat, txt = sys.argv[1], sys.argv[2]
    else:
        pat, txt = 'abracadabra', 'abacadabrabracabracadabrabrabracad'
    searcher = RabinKarp(pat)
    offset = searcher.search(txt)
    print(f'text: {txt}')
    for i in range(offset):
        print(txt[i])
    print(pat)
    print(offset)


main()
