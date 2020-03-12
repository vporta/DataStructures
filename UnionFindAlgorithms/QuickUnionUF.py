"""
/******************************************************************************
 *  Ported from Java to Python from https://algs4.cs.princeton.edu/code/edu/princeton/cs/algs4/QuickUnionUF.java.html
 *  Execution:    python QuickUnionUF.py
 *  Dependencies: - 
 * Data files: tinyUF.txt
 *  Quick-union algorithm.
 ******************************************************************************/
"""
from typing import * 

class QuickUnionUF:
    """
    Class represents a union-find data type. It supports the classic union and find opertations, along with a count operation that returns the total number of sets. 

    :param n: elements {0} through {n-1}.
    :type n: int 
    
    :ivar _count: number of components initialized to n.
    :ivar _parent: _parent[i] = parent of i
    
    :vartype _count: int
    :vartype _parent: list[int]

    :py:func: count() 
    :py:func: find(p)
    :py:func: validate(p)
    :py:func: union(p, q)
    
    """
    from UF import IllegalArgumentException

    def __init__(self, n: int): 
        """
        Initializes an empty union-find data structure with
        {n} elements {0} through {n-1}.
        Initially, each elements is in its own set.
        :param n: the number of elements
        :raises IllegalArgumentException: if {n < 0}
        """
        self._count = n 
        self._parent = [i for i in range(n) ]

    def count(self) -> int:
        """
        Returns the number of sets. 
        :returns: the number of sets (between {1} and {n})
        :rtype: int 
        """
        return self._count 

    def find(self, p: int) -> List[int]: 
        """
        Returns the canonical element of the set containing element {p}.
        :param p: an element
        :raises IllegalArgumentException: unless {0 <= p < n}
        :returns: the canonical element of the set containing {p}
        :rtype: int 
        """
        self._validate(p)
        while p != self._parent[p]:
            p = self._parent[p]
        return p 

    def _validate(self, p: int):
        """
        Validate that p is a valid index.
        """
        n = len(self._parent)
        if p < 0 or p >= n: raise IllegalArgumentException(f'index {p} is not between 0 and {n-1}') 

    def union(self, p: int, q: int):
        """
        Merges the set containing element {p} with the set containing element {q}.
        :param  p: one element
        :param  q: the other element
        :raises IllegalArgumentException: unless both {0 <= p < n} and {0 <= q < n}
        """
        root_p = self.find(p)
        root_q = self.find(q)

        if root_p == root_q: return 
        self._parent[root_p] = root_q
        self._count -= 1 

    def __repr__(self):
        return f'<QuickUnionUF(_parent={self._parent}, _count={self._count})>'

def main():
    
    file_name = 'tinyUF.txt'
    with open(file_name) as f:
        lines = [line.strip() for line in f]

    quf = QuickUnionUF(int(lines[0]))  
    print(quf)
    for i in range(1, len(lines)):
        p, q = int(lines[i][0]), int(lines[i][2])
        if quf.find(p) == quf.find(q): continue 
        quf.union(p, q)
        print(f'{p} {q}')
    print(f'{quf.count()} components')
    print(lines)
    print(quf)

if __name__ == '__main__':
    main()





