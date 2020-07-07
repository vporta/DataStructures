"""
Cycle.py
The Cycle class represents a data type for
 *  determining whether an undirected graph has a simple cycle.
 *  The has_cycle operation determines whether the graph has
 *  a cycle and, if so, the cycle operation returns one.
 *
 *  This implementation uses depth-first search.
 *  The constructor takes Theta(V + E) time in the
 *  worst case, where V is the number of vertices and
 *  E is the number of edges.
 *  (The depth-first search part takes only O(V) time
 *  however, checking for self-loops and parallel edges takes
 *  Theta(V + E) time in the worst case.)
 *  Each instance method takes Theta(1) time.
 *  It uses Theta(V) extra space (not including the graph).
"""
from Graphs.Graph import Graph
from collections import deque


class Cycle:
    _cycle = None

    def __init__(self, g):
        """
        :param g: the Graph
        """
        if self.__has_self_loop(g):
            return
        if self.__has_parallel_edges(g):
            return
        self._g = g
        self._marked = [False for _ in range(g.get_V())]
        self._edge_to = [False for _ in range(g.get_V())]
        for v in range(g.get_V()):
            if not self._marked[v]:
                self.__dfs(g, -1, v)

    def get_g(self):
        return self._g

    def get_marked(self):
        return self._marked

    def get_edge_to(self):
        return self._edge_to

    def get_cycle(self):
        return self._cycle

    def __has_self_loop(self, g):
        for v in range(g.get_V()):
            for w in g.adj_vertices(v):
                if v == w:
                    self._cycle = deque()
                    self._cycle.append(v)
                    self._cycle.append(v)
                    return True
        return False

    def __has_parallel_edges(self, g):
        marked = [False for _ in range(g.get_V())]
        for v in range(g.get_V()):
            for w in g.adj_vertices(v):
                if marked[w.item]:
                    self._cycle.append(v)
                    self._cycle.append(w.item)
                    self._cycle.append(v)
                    return True
                marked[w.item] = True
            for w in g.adj_vertices(v):
                marked[w.item] = False

        return False

    def __dfs(self, g, u, v):
        self.get_marked()[v] = True
        for w in g.adj_vertices(v):
            # short circuit if cycle already found
            if self.get_cycle() is not None:
                return
            if not self.get_marked()[w.item]:
                self.get_edge_to()[w.item] = v
                self.__dfs(g, v, w.item)
            # check for cycle (but disregard reverse of edge leading to v)
            elif w.item != u:
                x = v
                while x != w.item:
                    self._cycle = deque()
                    self._cycle.append(x)
                    x = self.get_edge_to()[x]
                self._cycle.append(w)
                self._cycle.append(v)

    def has_cycle(self):
        return self.get_cycle() is not None

    def __repr__(self):
        return f'<{self.__class__.__name__}(\n' \
               f'g={self.get_g()}, \n' \
               f'cycle={self.get_cycle()}\n' \
               f'edge_to={self.get_edge_to()}\n' \
               f'marked={self.get_marked()})>'


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

    finder = Cycle(g)
    print(finder)
    if finder.has_cycle():
        for v in finder.get_cycle():
            print(f'cycle: {v} ')
        print()
    else:
        print('Graph is acyclic')


if __name__ == '__main__':
    main()

