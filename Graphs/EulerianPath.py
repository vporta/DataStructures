"""
EulerianPath.py
An Eulerian path, also called an Euler chain, Euler trail, Euler walk, or "Eulerian" version of any of these
variants, is a walk on the graph edges of a graph which uses each graph edge in the original graph exactly once.
A connected graph has an Eulerian path iff it has at most two graph vertices of odd degree.

The EulerianPath class represents a data type
 *  for finding an Eulerian path in a graph.
 *  An Eulerian path is a path (not necessarily simple) that
 *  uses every edge in the graph exactly once.
 *  This implementation uses a non-recursive depth-first search.
 *  The constructor takes Theta(E + V) time in the worst
 *  case, where E is the number of edges and V is
 *  the number of vertices.
 *  Each instance method takes Theta(1) time.
 *  It uses Theta(E + V) extra space in the worst case
 *  (not including the digraph).
"""
from Graphs.Edge import Edge
from Graphs.Graph import Graph
from collections import deque, defaultdict


class EulerianPath:

    _path = deque()  # stack

    class EEdge(Edge):

        def __init__(self, v=0, w=0, is_used=False):
            super().__init__(v, w)
            self._is_used = is_used

        def get_is_used(self):
            return self._is_used

        def __repr__(self):
            return f'<{self.__class__.__name__}(' \
                   f'v={super().get_v()}, ' \
                   f'w={super().get_w()}, ' \
                   f'weight={super().weight()}, ' \
                   f'_is_used={self.get_is_used()})>'

    def __init__(self, g):
        # find vertex from which to start potential Eulerian path:
        # a vertex v with odd degree(v) if it exits;
        # otherwise a vertex with degree(v) > 0
        self.g = g
        odd_degree_vertices = 0
        self.adj = deque()
        for v in range(g.get_V()):
            self.adj.append(EulerianPath.EEdge(v))
        s = EulerianPath.__non_isolated_vertex(g)
        for v in range(g.get_V()):
            if g.degree(v) % 2 != 0:
                odd_degree_vertices += 1
                s = v
        # Eulerian path iff it has at most two graph vertices of odd degree
        if odd_degree_vertices > 2:
            return
        # special case for graph with 0 edges (has a degenerate Eulerian Path)
        if s == -1:
            s = 0

        adj = self.adj
        for v in range(g.get_V()):
            self_loops = 0
            for w in g.adj_vertices(v):
                # careful with self loops
                if v == w.item:
                    if self_loops % 2 == 0:
                        e = EulerianPath.EEdge(v, w.item)
                        adj[v].append(e)
                        adj[w.item].append(e)
                    self_loops += 1
                elif v < w.item:
                    e = EulerianPath.EEdge(v, w.item)
                    adj[v].append(e)
                    adj[w.item].append(e)
        stack = deque()
        stack.append(s)
        # greedily search through edges in iterative DFS style
        while stack is not None:
            v = stack.pop()
            while adj[v] is not None:
                edge = adj[v].popleft()
                print(edge)
                if edge.get_is_used():
                    continue
                edge._is_used = True
                stack.append(v)
                v = edge.other(v)
            # push vertex with no more leaving edges to path
            self.get_path().append(v)

        # check if all edges are used
        if len(self.get_path()) != g.get_E() + 1:
            self._path = None

    def get_path(self):
        return self._path

    def path(self):
        yield from list(self.get_path())

    def has_eulerian_path(self):
        return self.get_path() is not None

    @staticmethod
    def __non_isolated_vertex(g):
        for v in range(g.get_V()):
            if g.degree(v) > 0:
                return v
        return -1

    def __repr__(self):
        return f'adj = {self.adj}, \n' \
               f'path={self.get_path()}'


def main():
    g = Graph(13)
    with open("../Resources/tinyG.txt", ) as f:
        for line in f.readlines():
            vertices = " ".join(line.splitlines()).split(' ')
            if len(vertices) < 2:
                continue
            else:
                v1, v2 = int(vertices[0]), int(vertices[1])
                g.add_edge(v1, v2)
    print(g)
    euler = EulerianPath(g)
    print(euler)
    print('Eulerian path: ')
    if euler.has_eulerian_path():
        for v in euler.path():
            print(f'{v} ')
        print()
    else:
        print('None')
    print()


if __name__ == '__main__':
    main()


