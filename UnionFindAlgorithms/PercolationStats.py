"""
/******************************************************************************
 *   Performs a series of computational experiments.
 *  Execution:    -
 *  Dependencies: - 
 ******************************************************************************/
"""
from Percolation import Percolation 
import random 
import math

class PercolationStats:
    """
    :param T: The number of times a computation experiment runs. 
    :type T: int. 
    :param N: elements {0} through {N-1} for an N-by-N grid. 
    :type N: int. 
    """

    def __init__(self, N: int, T: int):
        """
        Perform T independent experiments on an N-by-N grid.
        :param T: The number of times a computation experiment runs. 
        :type T: int. 
        :param N: elements {0} through {N-1} for an N-by-N grid. 
        :type N: int.
        """
        if N < 1 or T < 1: raise ValueError('N and T must be > 0.')
        self.t = T 
        self.N = N
        self.threshold = [self.calc_threshold(N) for _ in range(self.t)]

    def calc_threshold(self, n: int) -> float:
        """
        Find threshold value p*, probability the system will percolate. 
        :param n: n the value.
        :return: threshold value. 
        :rtype: float.
        """
        counter = 0 
        i, j = None, None 
        perc = Percolation(n)
        while not perc.percolates():
            i = random.randint(0, n-1)+1 
            j = random.randint(0, n-1)+1
            print(f'i: {i}\nj: {j}')  
            if not perc.is_open(i, j):
                counter += 1 
                perc.open(i, j)
        return counter / (n * n)


    def mean(self) -> float:
        """
        Sample mean of percolation threshold. 
        :return: mean. 
        :rtype: float. 
        """
        _sum = 0  
        for i in range(len(self.threshold)):
            _sum += self.threshold[i]
        return _sum / self.t

    def stddev(self) -> float:
        """
        Sample standard deviation of percolation threshold. 
        :return: standard deviation. 
        :rtype: float.
        """


        m = self.mean()
        _sum = 0 
        for i in range(len(self.threshold)):
            _sum += (self.threshold[i] - m) * (self.threshold[i] - m)
        if self.t == 1:
            return float('nan') 
        return _sum / (self.t - 1)


    def confidence_low(self) -> float:
        """
        Low endpoint of 95% confidence interval. 
        :return: low endpoint. 
        :rtype: float.
        """
        return self.mean() - (1.96 * self.stddev()) / (math.sqrt(self.t)) 

    def confidence_high(self) -> float:
        """
        High endpoint of 95% confidence interval. 
        :return: high endpoint. 
        :rtype: float.
        """
        return self.mean() + (1.96 * self.stddev()) / (math.sqrt(self.t))  

    def __repr__(self):
        return f'<PercolationStats(threshold={self.threshold}, T={self.t}, N={self.N})>'


def main():
    stats = PercolationStats(4, 20)
    print(stats)
    print(f'mean = {stats.mean()}')
    print(f'stddev = {stats.stddev()}')
    print(f'95% confidence interval = {stats.confidence_low()}, {stats.confidence_high()}')


if __name__ == '__main__':
    main()


