"""
bipartite.py
Given a graph, find either (i) a bi-partition or (ii) an odd-length cycle.
 *  Runs in O(E + V) time.
The Bipartite class represents a data type for
 *  determining whether an undirected graph is bipartite or whether
 *  it has an odd-length cycle.
 *  A graph is bipartite if and only if it has no odd-length cycle.
 *  The is_bipartite operation determines whether the graph is
 *  bipartite. If so, the color operation determines a
 *  bi-partition; if not, the odd_cycle operation determines a
 *  cycle with an odd number of edges.
 *
 *  This implementation uses depth-first search.
 *  The constructor takes Theta V + E) time in
 *  the worst case, where V is the number of vertices and E
 *  is the number of edges.
 *  Each instance method takes Theta(1) time.
 *  It uses Theta V) extra space (not including the graph).
"""
from graphs.graph import Graph
from collections import deque


class Bipartite:

    _cycle = list()

    def __init__(self, g):
        """
        :param g: the Graph
        """
        self._g = g
        self.__set_is_bipartite(True)
        self._color = [False for _ in range(g.get_V())]
        self._marked = [False for _ in range(g.get_V())]
        self._edge_to = [0 for _ in range(g.get_V())]
        for v in range(g.get_V()):
            if not self._marked[v]:
                self.__dfs(g, v)

        assert self.__check(g)

    def get_g(self):
        return self._g

    def get_is_bipartite(self):
        return self._is_bipartite

    def get_color(self):
        return self._color

    def get_marked(self):
        return self._marked

    def get_edge_to(self):
        return self._edge_to

    def get_cycle(self):
        return self._cycle

    def __set_is_bipartite(self, bip):
        self._is_bipartite = bip
        return

    def __dfs(self, g, v):
        self.get_marked()[v] = True

        for w in g.adj_vertices(v):
            if self.get_cycle() is not None:
                return
            # found uncolored vertex, so recur
            if not self.get_marked()[w.item]:
                self.get_edge_to()[w.item] = v
                self.get_color()[w] = not self.get_color()[v]
                self.__dfs(g, w)
            # if v-w create an odd-length cycle, find it
            elif self.get_color()[w] == self.get_color()[v]:
                self.__set_is_bipartite(False)
                cycle = self.get_cycle()
                cycle.append(w)
                x = v
                while x != w:
                    cycle.append(x)
                    x = self.get_edge_to()[x]
                cycle.append(w)

    def __is_bipartite(self):
        return self.get_is_bipartite()

    def color(self, v):
        self.validate_vertex(v)
        if not self.__is_bipartite():
            raise Exception('graph is not bipartite')
        return self.get_color()[v]

    def odd_cycle(self):
        return self.get_cycle()

    def __check(self, g):
        if self.get_is_bipartite():
            for v in range(g.get_V):
                for w in g.adj_vertices(v):
                    if self.get_color()[v] == self.get_color()[w]:
                        print(
                            f'edge {v}-{w} with {v} and {w} in same side of '
                            f'bi-partition\n')
                        return False
        else:
            first, last = -1, -1
            for v in self.odd_cycle():
                if first == -1:
                    first = v
                last = v
            if first != last:
                print(f'cycle begins with {first} and ends with {last}\n')
                return False
        return True

    def validate_vertex(self, v):
        n = len(self.get_marked())
        if v < 0 or v >= n:
            raise AttributeError(f'vertex {v} is not between 0 and {n-1}\n')

    def __repr__(self):
        return f'<{self.__class__.__name__}(' \
               f'g={self.get_g()}, ' \
               f'cycle={self.get_cycle()}, ' \
               f'is_bi_partite={self.get_is_bipartite()})>' \
               f'edge_to={self.get_edge_to()}' \
               f'color={self.get_color()}\n'

    
