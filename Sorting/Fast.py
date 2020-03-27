"""
Fast.py
A program to recognize line patterns in a given set of points. 

The problem. Given a set of N feature points in the plane, draw every line segment that connects 4 or more distinct points in the set.

- Think of p as the origin.
- For each other point q, determine the angle it makes with p.
- Sort the points according to the angle each makes with p.
- Check if any 3 (or more) adjacent points in the sorted order have equal angles with p. If so, these points, together with p, are collinear.
"""
from Point import Point
import sys 
sys.path.append('../DataStructures')
import math 

class Fast:
    
    def __init__(self, points):
        self.n = len(points)
        self.points = points 
        self.a = list()
        for i in range(self.n):
            if points[i] is None: raise ValueError(f'points[{i}] is None.')
            self.a.append(points[i])
        for pivot in self.a:
            copy = self.a[:]
            copy.sort(key=lambda p: pivot.compare(p))
            # print(copy)
            j = 0 
            previous = 0 
            collinear = list()
            for p in copy:
                if j == 0 or p.slope_to(pivot) != previous:
                    if len(collinear) >= 3:
                        collinear.insert(0, pivot)
                        collinear.sort()
                        if pivot == collinear[0]:
                            self.print_points(collinear)
                    collinear.clear()
                collinear.insert(0, p)
                previous = p.slope_to(pivot)
                j += 1 

    def print_points(self, points):
        buff = list()
        for i in range(len(points)):
            buff.append(str(points[i]))
            if i < len(points) - 1: 
                buff.append(' --> ')
        print(buff)

    def __repr__(self):
        return f'<Fast(points={self.points}, a={self.a})>'






def main():
    import numpy as np 
    import matplotlib.pyplot as plt 

    # datapoints = [ 
    #     (19000, 10000),
    #     (18000, 10000),
    #     (32000, 10000),
    #     (21000, 10000),
    #     (1234, 5678),
    #     (14000, 10000),
    # ]
    datapoints = [ 
        (10000, 0),
        (0, 10000),
        (3000, 7000),
        (7000, 3000),
        (20000, 21000),
        (3000, 4000),
        (14000, 15000),
        (6000, 7000),
    ]
    points = [Point(x, y) for (x, y) in datapoints ]
    print()
    f = Fast(points)
    # print(f'Fast = {f}')
    # print()


    def plot():
        X = np.array([p.x for p in points])
        Y = np.array([p.y for p in points])
        plt.scatter(X, Y)
        plt.show()
    # plot()


if __name__ == '__main__':
    main()


