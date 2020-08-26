"""
TwoPersonZeroSumGame.py
 *  Solve an m-by-n two-person zero-sum game by reducing it to
 *  linear programming. Assuming A is a strictly positive payoff
 *  matrix, the optimal row and column player strategies are x* an y*,
 *  scaled to be probability distributions.
 *
 *  (P)  max  y^T 1         (D)  min   1^T x
 *       s.t  A^T y <= 1         s.t   A x >= 1
 *                y >= 0                 x >= 0
 *
 *  Row player is x, column player is y.
"""
from Context.LinearProgramming import LinearProgramming


class TwoPersonZeroSumGame:

    EPSILON = 1E-8

    def __init__(self, payoff):
        self._m = len(payoff)
        self._n = len(payoff[0])
        c = [1.0 for _ in range(self._n)]
        b = [1.0 for _ in range(self._m)]

        # find smallest entry
        self._constant = float('inf')
        for i in range(self._m):
            for j in range(self._n):
                if payoff[i][j] < self._constant:
                    self._constant = payoff[i][j]
        # add constant to every entry to make strictly positive
        if self._constant <= 0:
            self._constant = -self._constant + 1
        else:
            self._constant = 0
        A = [[payoff[i][j] + self._constant for j in range(self._n)] for i in range(self._m)]

        self._lp = LinearProgramming(A, b, c)

    def value(self):
        return 1.0 / self._scale() - self._constant

    def _scale(self):
        # sum of x[j]
        x = self._lp.primal()
        _sum = 0.0
        for j in range(self._n):
            _sum += x[j]
        return _sum

    def row(self):
        # Returns the optimal row strategy of this two-person zero-sum game
        scale = self._scale()
        x = self._lp.primal()
        for j in range(self._n):
            x[j] /= scale
        return x

    def column(self):
        # Returns the optimal column strategy of this two-person zero-sum game.
        scale = self._scale()
        y = self._lp.dual()
        for i in range(self._m):
            y[i] /= scale
        return y

    def _is_primal_feasible(self):
        pass

    def _is_dual_feasible(self):
        pass

    def _is_nash_equilibrium(self, payoff):
        pass

    def _certify_solution(self, payoff):
        pass

    @staticmethod
    def test(description, payoff):
        print()
        print(description)
        print('------------------------------------')
        m, n, zerosum = len(payoff), len(payoff[0]), TwoPersonZeroSumGame(payoff)
        x, y = zerosum.row(), zerosum.column()
        print('x[] = [')
        for j in range(n - 1):
            print(x[j])
        print(f'\n{x[n - 1]}')

        print('y[] = [')
        for i in range(m - 1):
            print(y[i])
        print(f'\n{y[m - 1]}')
        print(f'values = {zerosum.value()}')

    @staticmethod
    def test1():
        # row = [ 4/7, 3/7 ], column = [ 0, 4/7, 3/7 ], value = 20/7
        # http://en.wikipedia.org/wiki/Zero-sum
        payoff = [
            [30, -10, 20],
            [10, 20, -20]
        ]
        TwoPersonZeroSumGame.test('wikipedia', payoff)

    @staticmethod
    def test5():
        # rock, paper, scissors
        # row    = [ 1/3, 1/3, 1/3 ]
        # column = [ 1/3, 1/3, 1/3 ]
        payoff = [
            [0, -1, 1],
            [1, 0, -1],
            [-1, 1, 0]
        ]
        TwoPersonZeroSumGame.test('rock, paper, scissors', payoff)


def main():
    import random as r
    TwoPersonZeroSumGame.test1()
    TwoPersonZeroSumGame.test5()

    m, n = 3, 3
    payoff = [[r.uniform(-0.5, 0.5) for _ in range(n)] for _ in range(m)]
    TwoPersonZeroSumGame.test(f'random {m}-by-{n}', payoff)


if __name__ == '__main__':
    main()