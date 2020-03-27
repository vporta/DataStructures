"""
GrahamScan.py 
Create points from standard input and compute the convex hull using
Graham scan algorithm. 
May be floating-point issues if x- and y-coordinates are not integers.
Dependencies: Point2D.py 
"""
import math 
from collections import deque
from Point2D import Point2D

class GrahamScan:
    _hull = deque()  # stack of Point2D objects
    
    def __init__(self, points):
        """
        Computes the convex hull of the specified array of points. 
        """
        if points is None: raise ValueError('argument is None.')
        if len(points) == 0: raise ValueError('list is of length 0.')
        self.n = len(points)
        self.a = list()
        for i in range(self.n):
            if points[i] is None: raise ValueError(f'points[{i}] is None.')
            self.a.append(points[i])

         # Find the smallest left point and remove it from points
        start = min(self.a, key=lambda p: (p.x, p.y))
        self.a.pop(self.a.index(start))

        # Sort points so that traversal is from start in a ccw circle.
        points_slopes = [(p, p.slope(start)) for p in self.a]
        points_slopes.sort(key=lambda e: e[1])

        _points = []
        i = 0 

        for j in range(1, len(points_slopes)):
            if points_slopes[j][1] != points_slopes[i][1]:
                if j-i == 1:
                    _points.append(points_slopes[i])
                else:
                    points_cl = sorted(points_slopes[i:j], key=lambda e: start.dis(e[0]))
                    _points.extend(points_cl)
                i = j
        points_cl = sorted(points_slopes[i:], key=lambda e: -start.dis(e[0]))
        _points.extend(points_cl)
        _points = [p[0] for p in _points]

        self._hull = [start]
        for p in _points:
            self._hull.append(p)
            while len(self._hull) > 2 and Point2D.ccw(self._hull[-3], self._hull[-2], self._hull[-1]) < 0:
                self._hull.pop(-2)

    def hull(self):
        s = deque()
        for p in self._hull:
            s.append(p)
        return s  

    def _is_convex(self):
        n = len(self._hull)
        if n <= 2: return True 
        points = list()
        k = 0 
        for p in self.hull():
            points.append(p)
        for i in range(n):
            if Point2D.ccw(points[i], points[(i+1) % n], points[(i+2) % n]) <= 0:
                return False 
        return True 

    def __repr__(self):
        return f'<GrahamScan(a={self.a}, _hull={self._hull})>'



def main():
    datapoints = [ 
        (7486.0, 422.0),
        (29413.0, 596.0),
        (32011.0, 3140.0),
        (30875.0, 28560.0),
        (28462.0, 32343.0),
        (15731.0, 32661.0),
        (822.0, 32301.0),
        (823.0, 15895.0),
        (1444.0, 10362.0),
        (4718.0, 4451.0)]
    n = len(datapoints)
    points = list()
    for i in range(n):
        x = datapoints[i][0]
        y = datapoints[i][1]
        points.append(Point2D(x, y))
    graham = GrahamScan(points)
    print(graham)
    print()
    for p in graham.hull():
        print(p)

if __name__ == '__main__':
    main()










