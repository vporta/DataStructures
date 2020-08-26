"""
DirectedEulerianCycle.py
Find an Eulerian cycle in a digraph, if one exists.
The DirectedEulerianCycle class represents a data type
 *  for finding an Eulerian cycle or path in a digraph.
 *  An Eulerian cycle is a cycle (not necessarily simple) that
 *  uses every edge in the digraph exactly once.
 *
 *  This implementation uses a nonrecursive depth-first search.
 *  The constructor takes Theta(E + V) time in the worst
 *  case, where E is the number of edges and V is the
 *  number of vertices
 *  Each instance method takes Theta(1) time.
 *  It uses Theta(V) extra space (not including the digraph).
"""
from Graphs.Digraph import Digraph
from Graphs.Graph import Graph
from Graphs.BreadthFirstPaths import BreadthFirstPaths
from collections import deque


class DirectedEulerianCycle:

    _cycle = None

    def __init__(self, g):
        self._g = g
        self.__run(g)

    def __run(self, g):
        if g.get_E() == 0:
            return
        for v in range(g.get_V()):
            if g.outdegree(v) != g.indegree(v):
                return
        adj = [g.adj_vertices(v) for v in range(g.get_V())]
        s = DirectedEulerianCycle.__non_isolated_vertex(g)
        stack = deque()
        stack.append(s)
        self._cycle = deque()
        while stack:
            v = stack.pop()
            while next(adj[v], None) is not None:
                stack.append(v)
                v = next(adj[v])
            self._cycle.append(v)
        if len(self._cycle) != g.get_E() + 1:
            self._cycle = None

        assert self.__certify_solution(g)

    def cycle(self):
        return self._cycle

    def has_eulerian_cycle(self):
        return self._cycle is not None

    @staticmethod
    def __non_isolated_vertex(g):
        for v in range(g.get_V()):
            if g.outdegree(v) > 0:
                return v
        return -1

    @staticmethod
    def __satisfies_necessary_and_sufficient_conditions(g):
        """
        Determines whether a digraph has an Eulerian cycle using necessary
        and sufficient conditions (without computing the cycle itself):
           - at least one edge
           - indegree(v) = outdegree(v) for every vertex
           - the graph is connected, when viewed as an undirected graph
             (ignoring isolated vertices)
        """
        # Condition 0: at least 1 Edge
        if g.get_E() == 0:
            return False
        # Condition 1: indegree(v) == outdegree(v) for every vertex
        for v in range(g.get_V()):
            if g.outdegree() != g.indegree(v):
                return False
        # Condition 2: graph is connected, ignoring isolated vertices
        h = Graph(g.get_V())
        for v in range(g.get_V()):
            for w in g.adj_vertices(v):
                h.add_edge(v, w)
        # check that all non-isolated vertices are connected
        s = DirectedEulerianCycle.__non_isolated_vertex(g)
        bfs = BreadthFirstPaths(h, s)
        for v in range(g.get_V()):
            if h.degree(v) > 0 and not bfs.has_path_to(v):
                return False
            return True

    def __certify_solution(self, g):
        if self.has_eulerian_cycle() == (self.cycle() is None):
            return False
        if self.has_eulerian_cycle() \
                != DirectedEulerianCycle.__satisfies_necessary_and_sufficient_conditions(g):
            return False
        if self._cycle is None:
            return True
        if len(self._cycle) != g.get_E() + 1:
            return False

        return True

    def __repr__(self):
        return f'<{self.__class__.__name__}(cycle={self._cycle}, g={self._g})>'


def main():
    g = Digraph(13)
    with open("../Resources/tinyDG.txt", ) as f:
        for line in f.readlines():
            vertices = " ".join(line.splitlines()).split(' ')
            if len(vertices) < 2:
                continue
            else:
                v1, v2 = int(vertices[0]), int(vertices[1])
                g.add_edge(v1, v2)
    print(g)
    euler = DirectedEulerianCycle(g)
    print(euler)
    print("Eulerian cycle: ")
    if euler.has_eulerian_cycle():
        for v in euler.cycle():
            print(v + " ")
        print()
    else:
        print("none")

    print()


if __name__ == '__main__':
    main()









