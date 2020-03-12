"""
/******************************************************************************
 *  Ported from Java to Python. Taken from https://algs4.cs.princeton.edu/code/edu/princeton/cs/algs4/UF.java.html
 *  Execution:    python UF.py
 *  Dependencies: - 
 *  Weighted quick-union by rank with path compression by halving.
* This implementation uses weighted quick union by rank with path compression by halving.
 ******************************************************************************/
"""
from typing import * 

class IllegalArgumentException(Exception):
    pass 

class UF:
    """
    This class represents a union–find data type
    (also known as the disjoint-sets data type).
    It supports the classic union and find operations,
    along with a count operation that returns the total number
    of sets.

    :param n: elements {0} through {n-1}.
    :type n: int 

    :ivar _count: number of components initialized to n. 
    :ivar _parent: _parent[i] = parent of i
    :ivar _rank: _rank[i] = rank of subtree rooted at i (never more than 31)

    :vartype _count: int  
    :vartype _parent: list[int]
    :vartype _rank: list[int]  
    """


    def __init__(self, n: int):
        """
        Initializes an empty union-find data structure with
        {n} elements {0} through {n-1}.
        Initially, each elements is in its own set.
        :param n: the number of elements
        :raises IllegalArgumentException: if {n < 0}
        """
        if n < 0: raise IllegalArgumentException('The number of elements must be greater than 0')
        self._count = n 
        self._parent = [i for i in range(n)]
        self._rank = [0 for _ in range(n)]

    def find(self, p: int) -> int:
        """
        Returns the canonical element of the set containing element {p}.
        :param p: an element
        :raises IllegalArgumentException: unless {0 <= p < n}
        :return: the canonical element of the set containing {p}
        :rtype: int 
        """
        self._validate(p)
        while p != self._parent[p]: 
            self._parent[p] = self._parent[self._parent[p]]  # path compression by halving 
            p = self._parent[p]
        return p 

    def _validate(self, p: int):
        """ Validate that p is a valid index. """
        n = len(self._parent)
        if p < 0 or p >= n: raise IllegalArgumentException(f'index {p} is not between 0 and {n-1}')

    def count(self) -> int:
        """
        Returns the number of sets. 
        :return: the number of sets (between {1} and {n})
        :rtype: int
        """
        return self._count

    def connected(self, p: int, q: int) -> bool:
        """
        Returns True if the two elements are in the same set. 
        :param p: one element 
        :param q: the other element 
        :raises IllegalArgumentException: unless both {0 <= p < n} and {0 <= q < n}.  
        :return: {True} if {p} and {q} are in the same set; {False} otherwise. 
        :rtype: bool 
        """
        return self.find(p) == self.find(q)

    def union(self, p, q):
        """
        Merges the set containing element {p} with the set containing element {q}.
        :param  p: one element
        :param  q: the other element
        :raises IllegalArgumentException: unless both {0 <= p < n} and {0 <= q < n}
        """
        root_p, root_q = self.find(p), self.find(q)
        if root_p == root_q: return 
        # make root of smaller rank point to root of larger rank 
        if self._rank[root_p] < self._rank[root_q]: 
            self._parent[root_p] = root_q
        elif self._rank[root_p] > self._rank[root_q]:
            self._parent[root_q] = root_p 
        else:
            self._parent[root_q] = root_p
            self._rank[root_p] += 1 
        self._count -= 1 

    def __repr__(self):
        return f'<UF(_parent={self._parent}, _count={self._count}, _rank={self._rank})>'


def main():
    # ** uncomment below and run code to download data locally into a file ** 
    # import urllib.request
    # import shutil
    # url = 'https://algs4.cs.princeton.edu/15uf/tinyUF.txt'
    # # Download the file from `url` and save it locally under `file_name`:
    # with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
    #     shutil.copyfileobj(response, out_file)

    
    file_name = 'tinyUF.txt'
    with open(file_name) as f:
        lines = [line.rstrip() for line in f]

    print(lines)
    uf = UF(int(lines[0])) 
   
    # for i in range(1, len(lines)):
    #     p, q = lines[i][0], lines[i][2]
    #     if uf.connected(p, q): 
    #         continue 
    #     uf.union(p, q)
    #     print(f'{p} {q}')
    # print(f'{uf.count()} components')

if __name__ == '__main__':
    main()












