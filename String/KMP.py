"""
/******************************************************************************
 *  Ported from Java to Python. Taken from https://algs4.cs.princeton.edu/41graph
 *  Execution:    python KMP.py
 *  Dependencies: - 
 *  Reads in two strings, the pattern and the input text, and
 *  searches for the pattern in the text using the
 *  KMP algorithm.
 ******************************************************************************/
 **
 *  The {@code KMP} class finds the first occurrence of a pattern string
 *  in a text string.
 *  <p>
 *  This implementation uses a version of the Knuth-Morris-Pratt substring search
 *  algorithm. The version takes time proportional to <em>n</em> + <em>m R</em>
 *  in the worst case, where <em>n</em> is the length of the text string,
 *  <em>m</em> is the length of the pattern, and <em>R</em> is the alphabet size.
 *  It uses extra space proportional to <em>m R</em>.
 *  <p>
 *  For additional documentation,
 *  see <a href="https://algs4.cs.princeton.edu/53substring">Section 5.3</a> of
 *  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
 *
 Time complexity                  |         Space
 
    full deterministic finitie state automaton (DFA):  
        guarantee: 2 N
        typical:   1.1 N          |          M * R 
    mismatch transitions only: 
        guarantee: 3 N
        typical:   1.1 N          |          M  
"""


class KMP:

    def __init__(self, pat):
        """
        Preprocesses the pattern string. 
        :param pat: pat the pattern string 
        """
        self.R = 256 
        self.pat = pat 
        m = len(self.pat)
        self.dfa = [[0 for col in range(m)] for row in range(self.R)]
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
        """
        Returns the index of the first occurence of the pattern string
        in the text string.
        :param txt: txt the text string
        :returns: the index of the first occurence of the patterns string in the text string; N if no such match 
        """
        # simulate operation of DFA text 
        m, n, i, j = len(self.pat), len(txt), 0, 0 
        while i < n and j < m:
            j = self.dfa[ord(txt[i])][j]
            print(f'j = {j}')
            i += 1 
        if j == m: return i - m  # found  
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






