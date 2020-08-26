"""
LinearProgramming.py
 *  Given an m-by-n matrix A, an m-length vector b, and an
 *  n-length vector c, solve the  LP { max cx : Ax <= b, x >= 0 }:
 *      (P)  max     c^Tx
 *           s. t.   Ax = b
 *                    x >= 0
 *  Assumes that b >= 0 so that x = 0 is a basic feasible solution.
 *
 *  Creates an (m+1)-by-(n+m+1) simplex tableaux with the
 *  Right Hand Side Coefficients Sensitivity (RHS) in column m+n, the objective function in row m, and
 *  slack variables in columns m through m+n-1.

 *  The LinearProgramming class represents a data type for solving a
 *  linear program of the form { max cx : Ax <= b, x >= 0 }, where A is a m-by-n
 *  matrix, b is an m-length vector, and c is an n-length vector. For simplicity,
 *  we assume that A is of full rank and that b >= 0 so that x = 0 is a basic
 *  feasible solution.
 *
 *  The data type supplies methods for determining the optimal primal and
 *  dual solutions.
 *
 *  This is a bare-bones implementation of the simplex algorithm.
 *  It uses Bland's rule to determining the entering and leaving variables.
 *  It is not suitable for use on large inputs. It is also not robust
 *  in the presence of floating-point round-off error.
"""


class LinearProgramming:
    EPSILON = 1.0E-10

    def __init__(self, A, b, c):
        self._m = len(b)
        self._n = len(c)
        for i in range(self._m):
            if not b[i] >= 0.0:
                raise ValueError('RHS must be non-negative')
        self._a = [[0.0 for j in range(self._n + self._m + 1)] for i in range(self._m + 1)]

        for i in range(self._m):
            for j in range(self._n):
                self._a[i][j] = A[i][j]
        for i in range(self._m):
            self._a[i][self._n + i] = 1
        for j in range(self._n):
            self._a[self._m][j] = c[j]
        for i in range(self._m):
            self._a[i][self._m + self._n] = b[i]
        self._basis = [self._n + i for i in range(self._m)]

        self._solve()
        # assert self._check(A, b, c)

    def _solve(self):
        # run simplex algo starting from initial BFS
        while True:
            # find entering column q
            q = self._bland()
            if q == -1:
                break
            # find leaving row p
            p = self._min_ratio_rule(q)
            if p == -1:
                raise ValueError('Linear problem is unbounded')
            # pivot
            self._pivot(p, q)
            # update basis
            self._basis[p] = q

    def _bland(self):
        # lowest index of a non-basic column with a positive cost
        for j in range(self._m + self._n):
            if self._a[self._m][j] > 0.0:
                return j
        return -1  # optimal

    def _dantzig(self):
        # index of a non-basic column with most positive cost
        q = 0.0
        for j in range(1, self._m + self._n):
            if self._a[self._m][j] > self._a[self._m][q]:
                q = j
        if self._a[self._m][q] <= 0.0:
            return -1  # optimal
        else:
            return q

    def _min_ratio_rule(self, q):
        # find row p using min ratio rule (-1 if no such row)
        # (smallest such index if there is a tie)
        p = -1
        for i in range(self._m):
            if self._a[i][q] <= self.EPSILON:
                continue
            elif p == -1:
                p = i
            elif (self._a[i][self._m + self._n] / self._a[i][q]) < (self._a[p][self._m + self._n] / self._a[p][q]):
                p = i
        return p

    def _pivot(self, p, q):
        # pivot on entry (p, q) using Gauss-Jordan elimination
        # everything but row p and column q
        for i in range(self._m + 1):
            for j in range(self._m + self._n + 1):
                if i != p and j != q:
                    self._a[i][j] -= self._a[p][j] * self._a[i][q] / self._a[p][q]
        # zero out column q
        for i in range(self._m + 1):
            if i != p:
                self._a[i][q] = 0.0
        # scale row p
        for j in range(self._m + self._n + 1):
            if j != q:
                self._a[p][j] /= self._a[p][q]
        self._a[p][q] = 1

    def value(self):
        # Returns the optimal value of this linear program.
        return -self._a[self._m][self._m + self._n]

    def primal(self):
        # Returns the optimal primal solution to this linear program.
        x = [0.0] * self._n
        for i in range(self._m):
            if self._basis[i] < self._n:
                x[self._basis[i]] = self._a[i][self._m + self._n]
        return x

    def dual(self):
        # Returns the optimal dual solution to this linear program
        y = [0.0] * self._m
        for i in range(self._m):
            y[i] = -self._a[self._m][self._n + i]
        return y

    def _show(self):
        # print table
        print(f'm = {self._m}')
        print(f'n = {self._n}')
        for i in range(self._m + 1):
            for j in range(self._n + self._m + 1):
                print(f'{self._a[i][j]}')
            print()
        print(f'value = {self.value()}')
        for i in range(self._m):
            if self._basis[i] < self._n:
                print(f'x_{self._basis[i]} = {self._a[i][self._m + self._n]}')
            print()

    def _is_primal_feasible(self, A, b):
        pass

    def _is_dual_feasible(self, A, c):
        pass

    def _is_optimal(self, b, c):
        pass

    def _check(self, A, b, c):
        pass



    @staticmethod
    def _test(A, b, c):
        try:
            lp = LinearProgramming(A, b, c)
        except ArithmeticError as e:
            print(e)
            return
        print(f'value = {lp.value()}')
        x = lp.primal()
        for i in range(len(x)):
            print(f'x[{i}] = {x[i]}')
        y = lp.dual()
        for j in range(len(y)):
            print(f'y[{j}] = {y[j]}')

    @staticmethod
    def test1():
        A = [
            [-1, 1, 0],
            [1, 4, 0],
            [2, 1, 0],
            [3, -4, 0],
            [0, 0, 1],
        ]
        c = [1, 1, 1]
        b = [5, 45, 27, 24, 4]
        LinearProgramming._test(A, b, c)


def main():
    import random as r
    print('----- test 1 --------------------')
    LinearProgramming.test1()
    print()
    print('----- test random ---------------')
    m = 5
    n = 8
    c = [0] * n
    b = [0] * m
    A = [[0]*n]*m
    for j in range(n):
        c[j] = r.uniform(0, 1000)
    for i in range(m):
        b[i] = r.uniform(0, 1000)
    for i in range(m):
        for j in range(n):
            A[i][j] = r.uniform(0, 100)
    lp = LinearProgramming(A, b, c)
    LinearProgramming._test(A, b, c)


if __name__ == '__main__':
    main()





