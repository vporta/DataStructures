"""
/******************************************************************************
 *  Execution:    python BoyerMoore.py
 *
 *  Reads in two strings, the pattern and the input text, and
 *  searches for the pattern in the input text using the
 *  bad-character rule part of the Boyer-Moore algorithm.
 *  (does not implement the strong good suffix rule)
 ******************************************************************************/
/**
 *  The {@code BoyerMoore} class finds the first occurrence of a pattern string
 *  in a text string.
 *  <p>
 *  This implementation uses the Boyer-Moore algorithm (with the bad-character
 *  rule, but not the strong good suffix rule).
 *  <p>
 *  For additional documentation,
 *  see <a href="https://algs4.cs.princeton.edu/53substring">Section 5.3</a> of
 *  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.

 Time complexity: 
    Full algorithm: 
                avg  N / M
                guarantee  3N or N 
    Mismatched character heuristic only:
                avg  N / M
                guarantee  M * N  
    
 Space: R
 */
"""
# ord('A') == chr(65) //  ord('A') -> 65 ... chr(65) -> 'A'

class BoyerMoore:

    def __init__(self):
        self.NO_OF_CHARS = 256 

    def get_bad_char(self, string, size):
        """
        The preprocessing function for 
        Boyer Moore's bad character heuristic.
        :param string: string pattern 
        :param size: length of string pattern 
        """
        bad_char = [-1]*self.NO_OF_CHARS
        for i in range(size):
            bad_char[ord(string[i])] = i 
        print(bad_char)
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
        while(s <= n-m):  
            j = m-1  # start at last index of pattern string. 

            while j>=0 and pat[j] == txt[s+j]: 
                # move left in pattern string when a matched character is found. 
                j -= 1
            if j<0: 
                print(f"Pattern occur at shift = {s}") 
                s += (m-bad_char[ord(txt[s+m])] if s+m<n else 1) 
            else: 
                s += max(1, j-bad_char[ord(txt[s+j])]) 

    def __repr__(self):
        return str(self)

bm = BoyerMoore()
print(bm.search(txt='BCAABCABCBCA', pat='ABCABC'))
