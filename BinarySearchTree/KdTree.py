"""
KdTree.py
Dependencies: Point2D, RectHV

Range search. To find all points contained in a given query rectangle, start at the root and recursively search
for points in both subtrees using the following pruning rule:
 * If the query rectangle does not intersect the
rectangle corresponding to a node, there is no need to explore that node (or its subtrees).
 * A subtree is searched
only if it might contain a point contained in the query rectangle.

Nearest-neighbor search.
To find a closest point to a given query point, start at the root and recursively search in both subtrees using
the following pruning rule: if the closest point discovered so far is closer than the distance between the query
point and the rectangle corresponding to a node, there is no need to explore that node (or its subtrees).
That is, search a node only only if it might contain a point that is closer than the best one found so far.
The effectiveness of the pruning rule depends on quickly finding a nearby point. To do this, organize the recursive
method so that when there are two possible subtrees to go down, you always choose the subtree that is on the same
side of the splitting line as the query point as the first subtree to explore—the closest point found while
exploring the first subtree may enable pruning of the second subtree.
"""
from BinarySearchTree.Point2D import Point2D
from BinarySearchTree.RectHV import RectHV
from collections import deque


class KdTree:
    XMIN = 0.0
    XMAX = 1.0
    YMIN = 0.0
    YMAX = 1.0
    _root = None

    class Node:
        _lb, _rt, = None, None  # left-bottom, right-top

        def __init__(self, p, rect, value=None):
            self._p = p  # Point2D
            self._rect = rect  # RectHV
            self._value = value

        def get_p(self):
            return self._p

        def get_rect(self):
            return self._rect

        def get_lb(self):
            return self._lb

        def get_rt(self):
            return self._rt

        def __repr__(self):
            return f'<Node(p={self._p}, ' \
                   f'rect={self._rect}, ' \
                   f'value = {self._value}, ' \
                   f'left-bottom={self._lb}, ' \
                   f'right-top={self._rt})>'

    def __init__(self):
        self._size = 0

    def is_empty(self):
        return self._root is None

    def size(self):
        return self._size

    def put(self, p):
        if p is None:
            raise ValueError('argument to put() is None')
        self._root = self.__put(self._root, p, KdTree.XMIN, KdTree.YMIN, KdTree.XMAX, KdTree.YMAX, 0)

    def __put(self, h, p, x_min, y_min, x_max, y_max, level):
        if h is None:
            self._size += 1
            return KdTree.Node(p, RectHV(x_min, x_max, y_min, y_max))
        cmp = self.__cmp(p, h.get_p(), level)
        if cmp < 0:
            if level % 2 == 0:
                level += 1
                h._lb = self.__put(h._lb, p, x_min, y_min, h.get_p().get_x(), y_max, level)
            else:
                level += 1
                h._lb = self.__put(h._lb, p, x_min, y_min, x_max, h.get_p().get_y(), level)
        elif cmp > 0:
            if level % 2 == 0:
                level += 1
                h._rt = self.__put(h._rt, p, h.get_p().get_x(), y_min, x_max, y_max, level)
            else:
                level += 1
                h._rt = self.__put(h._rt, p, x_min, h.get_p().get_y(), x_max, y_max, level)
        return h

    def __cmp(self, a, b, level):
        # even levels x-coord/vertical line
        if level % 2 == 0:
            cmp_result = a.compare_to(b)
            if cmp_result == 0:
                return a.compare_to(b)
            else:
                return cmp_result
        # odd levels y-coord/horizontal line
        else:
            cmp_result = a.compare_to(b)
            if cmp_result == 0:
                return a.compare_to(b)
            else:
                return cmp_result

    def contains(self, p):
        return self.__contains(self._root, p, 0) is not None

    def __contains(self, h, p, level):
        while h is not None:
            cmp = self.__cmp(p, h.get_p(), level)
            if cmp < 0:
                return self.__contains(h.get_lb(), p, level)
            elif cmp > 0:
                return self.__contains(h.get_rt(), p, level)
            else:
                return h.get_p()
        return None

    def range(self, rect):
        """
        Range Search - All points that are inside the rectangle (or on the boundary)
        :param rect: axis aligned rect
        :return: A list of tuples containing x,y coordinate points inside the rectangle
        """
        queue = deque()
        self.__range(self._root, rect, queue)
        return list(queue)

    def __range(self, h, rect, queue):
        if h is not None and rect.intersects(h.get_rect()):
            if rect.contains(h.get_p()):
                queue.append(h.get_p())
            self.__range(h.get_lb(), rect, queue)
            self.__range(h.get_rt(), rect, queue)

    def nearest(self, p):
        """
        A nearest neighbor search in the set to point p; null if the set is empty
        :param p: Query Point
        :return: The nearest point to Query Point
        :rtype: Point2D

        """
        if self.is_empty():
            return None
        else:
            return self.__nearest(self._root, p, None)

    def __nearest(self, h, p, mini):
        if h is not None:
            if mini is None:
                mini = h.get_p()
            if mini.distance_squared_to(p) >= h.get_rect().distance_squared_to(p):
                if h.get_p().distanceSquaredTo(p) < mini.distance_squared_to(p):
                    mini = h.get_p()
                if h.get_rt() is not None and h.get_rt().get_rect().contains(p):
                    mini = self.__nearest(h.get_rt(), p, mini)
                    mini = self.__nearest(h.get_lb(), p, mini)
                else:
                    mini = self.__nearest(h.get_lb(), p, mini)
                    mini = self.__nearest(h.get_rt(), p, mini)

        return mini

    def __repr__(self):
        return f'<KdTree(root={self._root}, size={self._size})>'


def main():
    tdt = KdTree()
    print(tdt)
    points = [(0.372, 0.497), (0.564, 0.413), (0.226, 0.577)]
    for i in range(len(points)):
        x, y = points[i]
        tdt.put(Point2D(x, y))
    print(tdt)
    print(tdt.range(RectHV(0.3, 0.8, 0.4, 0.6)))


main()
