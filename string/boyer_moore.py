"""
 boyer_moore.py
 *  Reads in two strings, the pattern and the input text, and
 *  searches for the pattern in the input text using the
 *  bad-character rule part of the Boyer-Moore algorithm.
 *  (does not implement the strong good suffix rule)
 *  The BoyerMoore class finds the first occurrence of a pattern string
 *  in a text string.
 *  This implementation uses the Boyer-Moore algorithm (with the bad-character
 *  rule, but not the strong good suffix rule).
 * Time complexity:
    Full algorithm: 
                avg  N / M
                guarantee  3N or N 
    Mismatched character heuristic only:
                avg  N / M
                guarantee  M * N
 * Space: R

"""


class BoyerMoore:

    def __init__(self):
        self.NO_OF_CHARS = 256

    def get_bad_char(self, string, size):
        """
        The pre-processing function for
        Boyer Moore's bad character heuristic.
        :param string: string pattern 
        :param size: length of string pattern 
        """
        bad_char = [-1] * self.NO_OF_CHARS
        for i in range(size):
            # ord('A') == chr(65)
            bad_char[ord(string[i])] = i

        return bad_char

    def search(self, txt, pat):
        """
        A pattern searching function that uses Bad Character 
        Heuristic of Boyer Moore Algorithm.
        :param txt: txt string 
        :param pat: pat pattern string  
        """
        m, n, = len(pat), len(txt)
        bad_char = self.get_bad_char(pat, m)
        s = 0

        while s <= n - m:
            j = m - 1  # start at last index of pattern string.

            # move left in pattern string when a matched character is found.
            while j >= 0 and pat[j] == txt[s + j]:
                j -= 1

            if j < 0:
                print(f"Pattern occur at shift = {s}")
                s += (m - bad_char[ord(txt[s + m])] if s + m < n else 1)
            else:
                s += max(1, j - bad_char[ord(txt[s + j])])

        return n

    def __repr__(self):
        return str(self)


def main():
    bm = BoyerMoore()
    print(bm.search(txt='BCAABCABCBCA', pat='ABCABC'))


if __name__ == '__main__':
    main()
