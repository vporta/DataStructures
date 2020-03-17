"""
/******************************************************************************
 *  Estimate the value of the percolation threshold via Monte Carlo simulation.
 *  Execution:    -
 *  Dependencies: - 
 *  Implements the weighted Quick-union class.
 ******************************************************************************/
"""
from WeightedQuickUnionUF import WeightedQuickUnionUF

class Percolation:
    """
    :param N: elements {0} through {N-1} for an N-by-N grid.
    :type N: int.

    :ivar grid: N-by-N grid of integers 0 and 1. 
    :ivar uf: WeightedQuickUnionUF N*N + 2.
    :ivar uf_perc: WeightedQuickUnionUF N * N + 2. 
    :ivar top: virtual top.
    :ivar bottom: virtual bottom. 
    
    :vartype grid: list.
    :vartype uf: WeightedQuickUnionUF.
    :vartype uf_perc: WeightedQuickUnionUF.
    :vartype top: int.
    :vartype bottom: int.
    """

    def __init__(self, N: int):
        """
        Create an N-by-N grid, with all sites blocked. 
        1 is open site. 
        0 is blocked site.
        :param N: elements {0} through {N-1}.
        :type N: int. 
        """
        if N <= 0: raise ValueError('N must be greater than 0.')
        self.n = N 
        self.uf = WeightedQuickUnionUF(N*N + 2)
        self.uf_perc = WeightedQuickUnionUF(N*N + 2)
        self.grid = [0 for i in range(N*N)]
        self.top = N * N 
        self.bottom = N * N + 1 

    def open(self, i: int, j: int):
        """
        Open site (row i, column j) if it is not open already. 
        :param i: row i in grid. 
        :param j: column j in grid. 
        type i: int.
        type j: int.
        :raises IndexError: unless {0 <= index < n}.
        """
        self._validate(i, j)
        if self.is_open(i, j): return 
        current_site = self.convert2dto1dcoord(i, j)
        self.grid[current_site] = 1 

        # union with top virtual cell 
        if i == 1 and not self.uf.find(current_site) == self.uf.find(self.top):
            self.uf.union(current_site, self.top)
            self.uf_perc.union(current_site, self.top)

        # union with bottom artificial cell
        if i == self.n: 
            self.uf_perc.union(current_site, self.bottom)

        # union with bottom cell
        if i < self.n:
            if self.is_open(i+1, j):
                self.uf.union(current_site, self.convert2dto1dcoord(i+1, j))
                self.uf_perc.union(current_site, self.convert2dto1dcoord(i+1, j))

        # union with upper cell
        if i > 1: 
            if self.is_open(i-1, j):
                self.uf.union(current_site, self.convert2dto1dcoord(i-1, j))
                self.uf_perc.union(current_site, self.convert2dto1dcoord(i-1, j))

        # union with left cell 
        if j > 1:
            if self.is_open(i, j - 1):
                self.uf.union(current_site, self.convert2dto1dcoord(i, j - 1))
                self.uf_perc.union(current_site, self.convert2dto1dcoord(i, j - 1))

        # union with left cell
        if j < self.n:
            if self.is_open(i, j + 1):
                self.uf.union(current_site, self.convert2dto1dcoord(i, j+1))
                self.uf_perc.union(current_site, self.convert2dto1dcoord(i, j+1))

    def convert2dto1dcoord(self, i:int, j: int) -> int:
        """
        Converts coord in 2d array to coord in 1d array.
        :param i: i the index column.
        :param j: j the index row.
        :return: a 1d coordinate.
        :rtype: int 
        """
        return self.n * (i - 1) + j - 1 

    def is_open(self, i: int, j: int) -> bool:
        """
        Is site (row i, column j) open?
        :param i: row i in grid. 
        :param j: column j in grid. 
        type i: int.
        type j: int.
        :raises IndexError: unless {0 <= index < n}.
        :return: True if site is open, False otherwise. 
        :rtype: bool
        """
        self._validate(i, j)
        if self.grid[self.convert2dto1dcoord(i, j)] == 1:
            return True 
        return False  

    def is_full(self, i: int, j: int) -> bool:
        """
        Is site (row i, column j) full?
        :param i: row i in grid. 
        :param j: column j in grid. 
        type i: int.
        type j: int.
        :raises IndexError: unless {0 <= index < n}.
        :return: True if site is full, False otherwise. 
        :rtype: bool
        """
        self._validate(i, j)
        if not self.is_open(i, j):
            return False 
        current_site = self.convert2dto1dcoord(i, j)
        if self.uf.find(self.top) == self.uf.find(current_site):
            return True 
        return False  

    def percolates(self) -> bool: 
        """
        Does the system percolate?
        :return: True if system percolates, False otherwise. 
        :rtype: bool 
        """
        if self.uf_perc.find(self.top) ==  self.uf_perc.find(self.bottom):
            return True 
        return False 

    def _validate(self, i: int, j: int):
        """
        Validate that index is a valid index.
        """
        n = len(self.grid)
        print(f'n: {n}')
        if i < 1 or i > n or j < 1 or j > n: raise IndexError(f'i: {i} or j: {j} is not between 0 and {n-1}') 
        return True

    def __repr__(self):
        return f'<Percolation(grid={self.grid}, uf={self.uf}, uf_perc={self.uf_perc}, top={self.top}, bottom={self.bottom}, n={self.n})>'















