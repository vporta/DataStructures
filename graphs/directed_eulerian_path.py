"""
directed_eulerian_path.py
Find an Eulerian path in a digraph, if one exists.

The DirectedEulerianPath class represents a data type
 *  for finding an Eulerian path in a digraph.
 *  An Eulerian path is a path (not necessarily simple) that
 *  uses every edge in the digraph exactly once.
 *
 *  This implementation uses a nonrecursive depth-first search.
 *  The constructor take Theta(E + V) time
 *  in the worst case, where E is the number of edges and
 *  V is the number of vertices.
 *  It uses Theta(V) extra space (not including the digraph).
"""

from graphs.digraph import Digraph
from graphs.graph import Graph
from graphs.breadth_first_paths import BreadthFirstPaths
from collections import deque


class DirectedEulerianPath:

    _path = None

    def __init__(self, g):
        self._g = g
        self.__run(g)

    def __run(self, g):
        deficit = 0
        s = DirectedEulerianPath.__non_isolated_vertex(g)
        for v in range(g.get_V()):
            if g.outdegree(v) > g.indegree(v):
                deficit += (g.outdegree(v) - g.indegree(v))
                s = v
        if deficit > 1:
            return
        if s == -1:
            s = 0

        adj = [g.adj_vertices(v) for v in range(g.get_V())]
        stack = deque()
        stack.append(s)
        self._path = deque()
        while stack:
            v = stack.pop()
            while next(adj[v], None) is not None:
                stack.append(v)
                v = next(adj[v])
            self._path.append(v)
        if len(self._path) != g.get_E() + 1:
            self._path = None

        assert self.__check(g)

    def path(self):
        return self._path

    def has_eulerian_path(self):
        return self._path is not None

    @staticmethod
    def __non_isolated_vertex(g):
        for v in range(g.get_V()):
            if g.outdegree(v) > 0:
                return v
        return -1

    @staticmethod
    def __satisfies_necessary_and_sufficient_conditions(g):
        """
        Determines whether a digraph has an Eulerian path using necessary
        and sufficient conditions (without computing the path itself):
            - indegree(v) = outdegree(v) for every vertex,
              except one vertex v may have outdegree(v) = indegree(v) + 1
              (and one vertex v may have indegree(v) = outdegree(v) + 1)
            - the graph is connected, when viewed as an undirected graph
              (ignoring isolated vertices)
        """
        # Condition 0: at least 1 Edge
        if g.get_E() == 0:
            return True
        # Condition 1: indegree(v) == outdegree(v) for every vertex,
        # except one vertex may have outdegree(v) = indegree(v) + 1
        deficit = 0
        for v in range(g.get_V()):
            if g.outdegree() > g.indegree(v):
                deficit += (g.outdegree() - g.indegree(v))
        if deficit > 1:
            return False
        # Condition 2: graph is connected, ignoring isolated vertices
        h = Graph(g.get_V())
        for v in range(g.get_V()):
            for w in g.adj_vertices(v):
                h.add_edge(v, w)
        # check that all non-isolated vertices are connected
        s = DirectedEulerianPath.__non_isolated_vertex(g)
        bfs = BreadthFirstPaths(h, s)
        for v in range(g.get_V()):
            if h.degree(v) > 0 and not bfs.has_path_to(v):
                return False
            return True

    def __check(self, g):
        if self.has_eulerian_path() == (self.path() is None):
            return False
        if self.has_eulerian_path() \
                != DirectedEulerianPath.__satisfies_necessary_and_sufficient_conditions(g):
            return False
        if self._path is None:
            return True
        if len(self._path) != g.get_E() + 1:
            return False

        return True

    def __repr__(self):
        return f'<{self.__class__.__name__}(path={self._path}, g={self._g})>'


def main():
    g = Digraph(13)
    with open("../resources/tinyDG.txt", ) as f:
        for line in f.readlines():
            vertices = " ".join(line.splitlines()).split(' ')
            if len(vertices) < 2:
                continue
            else:
                v1, v2 = int(vertices[0]), int(vertices[1])
                g.add_edge(v1, v2)
    print(g)
    euler = DirectedEulerianPath(g)
    print(euler)
    print("Eulerian path: ")
    if euler.has_eulerian_path():
        for v in euler.path():
            print(v + " ")
        print()
    else:
        print("none")

    print()


if __name__ == '__main__':
    main()









