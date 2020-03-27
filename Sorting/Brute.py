"""
Brute.py
Examines 4 points at a time and checks if they all lie on the same line segment, printing out any such line segments to standard output.
"""
from Point import Point

class Brute:
    
    @staticmethod
    def main(args):
        points = args 
        points.sort()
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                for k in range(j+1, len(points)):
                    for l in range(k+1, len(points)):
                        p = points[i]
                        q = points[j]
                        r = points[k]
                        s = points[l]
                        if p.slope_to(q) == q.slope_to(r) and q.slope_to(r) == r.slope_to(s):
                            print(f'{p} -> {q} -> {r} -> {s}')

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
Brute.main(points)


