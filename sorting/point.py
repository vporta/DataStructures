"""
point.py
A data type for points in the plane. 
"""
import math 

class Point:

    def __init__(self, x, y):
        if math.isinf(x) or math.isinf(y):
            raise ValueError('Coordinates must be finite.')
        if math.isnan(x) or math.isnan(y):
            raise ValueError('Coordinates cannot be NaN.')
        self.x = x 
        self.y = y 

    def draw(self):
        pass 

    def draw_to(self, that):
        pass 

    def slope_to(self, that):
        """
        Slope between this point and that point.
        """
        if that.x == self.x:
            if that.y == self.y:
                return float('-inf')
            return float('inf')
        if that.y == self.y: return 0 
        return (that.y - self.y) / (that.x - self.x)

    def angle_to(self, that):
        dx = that.x - self.x
        dy = that.y - self.y 
        return math.atan2(dy, dx) * (180 / math.pi)

    def dis(self, that):
        """
        Returns the Euclidean distance between this point and that point.
        """
        dx = self.x - that.x
        dy = self.y - that.y 
        return math.sqrt(dx*dx + dy*dy)

    def compare(self, that):
        slope1 = self.slope_to(that)
        slope2 = that.slope_to(self)
        if slope1 == slope2: return 0 
        if slope1 < slope2: return -1 
        return 1 

    def __lt__(self,other):
            if isinstance(other, Point):
                if (self.y != other.y): return self.y < other.y 
                elif (self.y == other.y): return self.x < other.x

    def __gt__(self,other):
        if isinstance(other, Point):
            if (self.y != other.y): return self.y > other.y 
            elif (self.y == other.y): return self.x > other.x

    def __eq__(self,other):
        if isinstance(other, Point):
            return self.y == other.y and self.x == other.x

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'<Point(x={self.x}, y={self.y})>'



