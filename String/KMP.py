"""
 *  KMP.py
 *  Reads in two strings, the pattern and the input text, and
 *  searches for the pattern in the text using the
 *  KMP algorithm.
 *  The KMP class finds the first occurrence of a pattern string
 *  in a text string.
 *  This implementation uses a version of the Knuth-Morris-Pratt substring search
 *  algorithm. The version takes time proportional to N + M * R
 *  in the worst case, where n is the length of the text string,
 *  m is the length of the pattern, and R is the alphabet size.
 *  It uses extra space proportional to M * R.
"""


class KMP:

    def __init__(self, pat):
        self.R = 256
        self.pat = pat
        m = len(self.pat)
        self.dfa = [[0 for _ in range(m)] for _ in range(self.R)]
        self.dfa[ord(self.pat[0])][0] = 1
        x, j = 0, 1
        while j < m:
            c = 0
            while c < self.R:
                self.dfa[c][j] = self.dfa[c][x]  # Copy mismatch cases.
                c += 1
            self.dfa[ord(self.pat[j])][j] = j + 1  # Set the match case.
            x = self.dfa[ord(self.pat[j])][x]  # Update restart state.  
            j += 1

    def search(self, txt):
        # simulate operation of DFA text 
        m, n, i, j = len(self.pat), len(txt), 0, 0
        while i < n and j < m:
            j = self.dfa[ord(txt[i])][j]
            print(f'j = {j}')
            i += 1
        if j == m:
            return i - m  # found
        return n  # not found 

    def __repr__(self):
        return f'<KMP(R={self.R}, pat={self.pat}, dfa={self.dfa})>'


def main():
    pat, txt = 'rab', 'abacadabrabracabracadabrabrabracad'
    kmp = KMP(pat)
    print(kmp)
    offset = kmp.search(txt)
    print(f'text:       {txt}')
    print(f'pattern:       {pat}')
    print(offset)
    for i in range(offset):
        print(' ')
    print(pat)


main()
