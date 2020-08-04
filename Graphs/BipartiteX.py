"""
Bipartite.py
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
 *  This implementation uses breadth-first search.
 *  The constructor takes Theta (V + E) time in
 *  the worst case, where V is the number of vertices and E
 *  is the number of edges.
 *  Each instance method takes Theta(1) time.
 *  It uses Theta V) extra space (not including the graph).
"""
from Graphs.Graph import Graph
from collections import deque
from queue import Queue, LifoQueue


class BipartiteX:
    _cycle = Queue()
    WHITE = False
    BLACK = True

    def __init__(self, g):
        """
        :param g: the Graph
        """
        self._g = g
        self.__set_is_bipartite(True)
        self._color = [False for _ in range(g.get_V())]
        self._marked = [False for _ in range(g.get_V())]
        self._edge_to = [0 for _ in range(g.get_V())]
        print(self.__is_bipartite())
        for v in range(g.get_V()):
            if self.__is_bipartite():
                if not self._marked[v]:
                    self.__bfs(g, v)

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

    def __bfs(self, g, s):
        q = Queue()  # the queue
        self.get_color()[s] = BipartiteX.WHITE
        self.get_marked()[s] = True  # mark vertex as visited
        q.put(s)
        while not q.empty():
            v = q.get()
            for w in g.adj_vertices(v):
                # found uncolored vertex, so recur
                if not self.get_marked()[w.item]:
                    self.get_marked()[w.item] = True
                    self.get_edge_to()[w.item] = v
                    self.get_color()[w.item] = not self.get_color()[v]
                    q.put(w.item)
                # if v-w create an odd-length cycle, find it
                elif self.get_color()[w.item] == self.get_color()[v]:
                    self._is_bipartite = False
                    # to form odd cycle, consider s-v path and s-w path
                    # and let x be closest node to v and w common to two paths
                    # then (w-x path) + (x-v path) + (edge v-w) is an odd-length cycle
                    # Note: dist_to[v] == dist_to[w]
                    stack = LifoQueue()
                    x, y = v, w
                    while x != y:
                        stack.put(x)
                        self._cycle.put(y)
                        x = self.get_edge_to()[x]
                        y = self.get_edge_to()[y]
                    stack.put(x)
                    while not stack.empty():
                        self._cycle.put(stack.get())
                    self._cycle.put(w)
                    return

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
            for v in range(g.get_V()):
                for w in g.adj_vertices(v):
                    if self.get_color()[v] == self.get_color()[w.item]:
                        print(
                            f'edge {v}-{w} with {v} and {w} in same side of '
                            f'bi-partition\n')
                        return False
        else:
            first, last = -1, -1
            for v in self.odd_cycle().queue:
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
            raise AttributeError(f'vertex {v} is not between 0 and {n - 1}\n')

    def __repr__(self):
        return f'<{self.__class__.__name__}(' \
               f'g={self.get_g()}, ' \
               f'cycle={self.get_cycle()}, ' \
               f'is_bi_partite={self.get_is_bipartite()})>' \
               f'edge_to={self.get_edge_to()}' \
               f'color={self.get_color()}\n'


