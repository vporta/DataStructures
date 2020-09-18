"""
point2d.py
Point data type for points in the plane.
"""
import math 

class Point2D:

    def __init__(self, x, y):
        if math.isinf(x) or math.isinf(y):
            raise ValueError('Coordinates must be finite.')
        if math.isnan(x) or math.isnan(y):
            raise ValueError('Coordinates cannot be NaN.')
        if x == 0.0: self.x = 0.0 
        else: self.x = x 
        if y == 0.0: self.y = 0.0 
        else: self.y = y  

    @staticmethod
    def ccw(a, b, c):
        """
        Returns true if a→b→c is a counterclockwise turn.
        :param a: first point
        :param b: second point
        :param c: third point
        :returns: { -1, 0, +1 } if a→b→c is a { clockwise, collinear; counterclocwise } turn.
        """
        return (b.x-a.x)*(c.y-a.y) - (b.y-a.y)*(c.x-a.x)

    def slope(self, p2):
        if self.x != p2.x:
            return 1.0*(self.y-p2.y)/(self.x-p2.x)
        else: 
            float('inf')

    def dis(self, that):
        """
        Returns the Euclidean distance between this point and that point.
        """
        dx = self.x - that.x
        dy = self.y - that.y 
        return math.sqrt(dx*dx + dy*dy)

    def __repr__(self):
        return f'<Point2D(x={self.x}, y={self.y})>'

