"""
Interval2D.py
The  Interval2D class represents a closed two-dimensional interval,
 *  which represents all points (x, y) with both  xmin <= x <= xmax and
 *   ymin <= y <= ymax.
 *  Two-dimensional intervals are immutable: their values cannot be changed
 *  after they are created.
 *  The class Interval2D includes methods for checking whether
 *  a two-dimensional interval contains a point and determining whether
 *  two two-dimensional intervals intersect.
"""


from Interval.Interval1D import Interval1D
from BinarySearchTree.Point2D import Point2D


class Interval2D:

    def __init__(self, x, y):
        """
        :type x: Interval1D
        :type y: Interval1D
        :param x: x the one-dimensional interval of x-coordinates
        :param y: y the one-dimensional interval of y-coordinates
        """
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def intersects(self, that):
        if not self.get_x().intersects(that.get_x()):
            return False
        if not self.get_y().intersects(that.get_y()):
            return False
        return True

    def contains(self, p: Point2D):
        """
        :param p: the two-dimensional point
        :return: true if this two-dimensional interval contains the point p; false otherwise
        """
        return self.get_x().contains(p.get_x()) and self.get_y().contains(p.get_y())

    def area(self):
        return self.get_x().length() * self.get_y().length()


def main():
    import random
    xmin, xmax, ymin, ymax, trials = 0.10, 0.99, 0.15, 0.85, 5
    x_interval, y_interval = Interval1D(xmin, xmax), Interval1D(ymin, ymax)
    box = Interval2D(x_interval, y_interval)
    counter = 0
    for t in range(trials):
        x, y = random.uniform(0.0, 1.0), random.uniform(0.0, 1.0)
        point = Point2D(x, y)
        if box.contains(point):
            counter += 1
    print(counter)




if __name__ == '__main__':
    main()
