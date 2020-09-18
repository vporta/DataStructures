"""
eulerian_cycle.py

The Eulerian Cycle class represents a data type
 *  for finding an Eulerian cycle or path in a graph.
 *  is a cycle (not necessarily simple) that
 *  uses every edge in the graph exactly once.
 *  This implementation uses a non-recursive depth-first search.
 *  The constructor takes Theta(E + V) time in the worst
 *  case, where E is the number of edges and V is
 *  the number of vertices.
 *  Each instance method takes Theta(1) time.
 *  It uses Theta(E + V) extra space in the worst case
 *  (not including the digraph).
"""
from graphs.edge import Edge
from graphs.graph import Graph
from collections import deque


class EulerianCycle:

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
        # must have at least one edge
        if g.get_E() == 0:
            return
        self.g = g
        self._cycle = deque()  # stack
        self.__run(g)

    def __run(self, g):
        for v in range(g.get_V()):
            if g.degree(v) % 2 != 0:
                return
        adj = deque()
        for v in range(g.get_V()):
            adj.append(EulerianCycle.EEdge(v))
        for v in range(g.get_V()):
            self_loops = 0
            for w in g.adj_vertices(v):
                # careful with self loops
                if v == w.item:
                    if self_loops % 2 == 0:
                        e = EulerianCycle.EEdge(v, w.item)
                        adj[v].append(e)
                        adj[w.item].append(e)
                    self_loops += 1
                elif v < w.item:
                    e = EulerianCycle.EEdge(v, w.item)
                    adj[v].append(e)
                    adj[w.item].append(e)

        s = EulerianCycle.__non_isolated_vertex(g)
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
            self._cycle.append(v)

        # check if all edges are used
        if len(self._cycle) != g.get_E() + 1:
            self._cycle = None

    def get_cycle(self):
        return self._cycle

    def cycle(self):
        yield from list(self.get_cycle())

    def has_eulerian_cycle(self):
        return self.get_cycle() is not None

    @staticmethod
    def __non_isolated_vertex(g):
        for v in range(g.get_V()):
            if g.degree(v) > 0:
                return v
        return -1

    def __repr__(self):
        return f'<{self.__class__.__name__}(cycle={self.get_cycle()})>'


def main():
    g = Graph(13)
    with open("../resources/tinyG.txt", ) as f:
        for line in f.readlines():
            vertices = " ".join(line.splitlines()).split(' ')
            if len(vertices) < 2:
                continue
            else:
                v1, v2 = int(vertices[0]), int(vertices[1])
                g.add_edge(v1, v2)
    print(g)
    euler = EulerianCycle(g)
    print(euler)
    print('Eulerian cycle: ')
    if euler.has_eulerian_cycle():
        for v in euler.cycle():
            print(f'{v} ')
        print()
    else:
        print('None')
    print()


if __name__ == '__main__':
    main()


