"""
RectHV.py
"""
import math
from Fundamentals.Point2D import Point2D


class RectHV:

    def __init__(self, xmin, xmax, ymin, ymax):
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax
        if math.isnan(xmin) or math.isnan(xmax):
            raise ValueError('x-coordinates cannot be NaN.')
        if math.isnan(ymin) or math.isnan(ymax):
            raise ValueError('y-coordinates cannot be NaN.')
        if xmax < xmin:
            raise ValueError(f'xmax < xmin')
        if ymax < ymin:
            raise ValueError(f'ymax < ymin')

    def xmin(self):
        return self.xmin

    def xmax(self):
        return self.xmax

    def ymin(self):
        return self.ymin

    def ymax(self):
        return self.ymax

    def contains(self, p: Point2D):
        return (p.get_x() >= self.xmin) \
               and (p.get_x() <= self.xmax) \
               and (p.get_y() >= self.ymin) \
               and (p.get_y() <= self.ymax)

    def intersects(self, that):
        return self.xmax >= that.xmin \
               and self.ymax >= that.ymin \
               and that.xmax >= self.xmin \
               and that.ymax >= self.ymin

    def distance_to(self, p: Point2D):
        return math.sqrt(self.distance_squared_to(p))

    def distance_squared_to(self, p: Point2D):
        dx = 0.0
        dy = 0.0
        if p.get_x() < self.xmin:
            dx = p.get_x() - self.xmin
        elif p.get_x() > self.xmax:
            dx = p.get_x() - self.xmax
        if p.get_y() < self.ymin:
            dy = p.get_y() - self.ymin
        elif p.get_y() > self.ymax:
            dy = p.get_y() - self.ymax
        return dx * dx + dy * dy

    @classmethod
    def get_class(cls):
        return cls.__name__

    def equals(self, other):
        if other == self:
            return True
        if other is None:
            return False
        if self.get_class() != other.get_class():
            return False
        that = other
        if self.xmin != that.xmin:
            return False
        if self.ymin != that.ymin:
            return False
        if self.xmax != that.xmax:
            return False
        if self.ymax != that.ymax:
            return False
        return True

    def __repr__(self):
        return f'[{self.xmin}, {self.xmax}] x [{self.ymin}, {self.ymax}]'
