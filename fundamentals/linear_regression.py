"""
linear_regression.py
 *  Compute least squares solution to y = beta * x + alpha.
 *  Simple linear regression.
 *  The LinearRegression class performs a simple linear regression
 *  on an set of n data points (y(i), x(i)).
 *  That is, it fits a straight line y = α + β x,
 *  (where y is the response variable, x is the predictor variable,
 *  α is the y-intercept, and β is the slope)
 *  that minimizes the sum of squared residuals of the linear regression model.
 *  It also computes associated statistics, including the coefficient of
 *  determination R2 and the standard deviation of the
 *  estimates for the slope and y-intercept.
"""
import math


class LinearRegression:

    def __init__(self, x, y):

        if len(x) != len(y):
            raise AttributeError('list lengths are not equal')
        n = len(x)
        sum_x, sum_y, sum_x2 = 0.0, 0.0, 0.0
        for i in range(n):
            sum_x += x[i]
            sum_x2 += x[i] * x[i]
            sum_y += y[i]
        x_bar, y_bar = sum_x / n, sum_y / n
        xx_bar, yy_bar, xy_bar = 0.0, 0.0, 0.0
        for i in range(n):
            xx_bar += (x[i] - x_bar) * (x[i] - x_bar)
            yy_bar += (y[i] - y_bar) * (y[i] - y_bar)
            xy_bar += (x[i] - x_bar) * (y[i] - y_bar)
        self._slope = xy_bar / xx_bar
        self._intercept = y_bar - self._slope * x_bar
        rss = 0.0  # residual sum of squares
        ssr = 0.0  # regression sum of squares
        for i in range(n):
            fit = self._slope * x[i] + self._intercept
            rss += (fit - y[i]) * (fit - y[i])
            ssr += (fit - y_bar) * (fit - y_bar)
        degrees_of_freedom = n - 2
        self._r2 = ssr / yy_bar
        s_var = rss / degrees_of_freedom
        self._s_var1 = s_var / xx_bar
        self._s_var0 = s_var / n + x_bar * x_bar * self._s_var1

    def intercept(self):
        return self._intercept

    def slope(self):
        return self._slope

    def r2(self):
        return self._r2

    def intercept_std_err(self):
        return math.sqrt(self._s_var0)

    def slope_std_err(self):
        return math.sqrt(self._s_var1)

    def predict(self, x):
        return self._slope * x + self._intercept

    def __str__(self):
        s = f''
        s += f'{self.slope()} + {self.intercept()}'
        s += f'     (R^2 = {self.r2()})'
        return s

    