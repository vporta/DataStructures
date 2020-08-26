"""
BellmanFordSP.py
"""
import math
from queue import LifoQueue

from Graphs.DirectedEdge import DirectedEdge
from Graphs.EdgeWeightedDigraph import EdgeWeightedDigraph
from Graphs.EdgeWeightedDirectedCycle import EdgeWeightedDirectedCycle
from Queues.Queue import Queue


class BellmanFordSP:
    _cost = 0

    def __init__(self, g: EdgeWeightedDigraph, s: int):
        self._dist_to = [math.inf] * g.get_V()
        self._edge_to = [None] * g.get_V()
        self._g = g
        self._s = s
        self._cycle = None
        self.__validate_vertex(s)
        self._on_queue = [False] * g.get_V()
        self._dist_to[s] = 0.0

        # Bellman-Ford Algorithm
        self._queue = Queue()
        self._queue.enqueue(s)
        self._on_queue[s] = True

        while not self._queue.is_empty() and not self.has_negative_cycle():
            v = self._queue.dequeue()
            self._on_queue[v] = False
            self.__relax(g, v)

        assert self.__check(g, s)

    # relax vertex v and put other endpoints on queue if changed
    def __relax(self, g, v):
        for e in g.adj_vertices(v):
            w = e.item.head()

            if self._dist_to[w] > self._dist_to[v] + e.item.weight():
                self._dist_to[w] = self._dist_to[v] + e.item.weight()
                self._edge_to[w] = e.item
                if not self._on_queue[w]:
                    self._queue.enqueue(w)
                    self._on_queue[w] = True

            # repeat V times
            # check each time for a negative cycle
            # v1 % V = v1, v2 % V = v2, ...
            # 1 % 8 = 1, 2 % 8 = 2, ... 8 % 8 = 0
            cost = self.inc_cost()
            if cost % g.get_V() == 0:
                print(w, self._on_queue[w])
                print(self._cost)
                self.__find_negative_cycle()
                if self.has_negative_cycle():
                    return

    def inc_cost(self):
        self._cost += 1
        return self._cost

    def has_negative_cycle(self):
        return self._cycle is not None

    def negative_cycle(self):
        return self._cycle

    def __find_negative_cycle(self):
        V = len(self._edge_to)
        spt = EdgeWeightedDigraph(V)

        for v in range(V):
            if self._edge_to[v] is not None:
                spt.add_edge(self._edge_to[v])

        finder = EdgeWeightedDirectedCycle(spt)
        self._cycle = finder.cycle()

    def dist_to(self, v):
        self.__validate_vertex(v)
        if self.has_negative_cycle():
            raise Exception('Negative cost cycle exists')
        return self._dist_to[v]

    def has_path_to(self, v):
        self.__validate_vertex(v)
        return self._dist_to[v] < math.inf

    def path_to(self, v):
        self.__validate_vertex(v)
        if self.has_negative_cycle():
            raise Exception('Negative cost cycle exists')

        path = LifoQueue()
        if not self.has_path_to(v):
            return None
        e = self._edge_to[v]
        while e is not None:
            path.put(e)
            e = self._edge_to[e.tail()]
        return path

    def __validate_vertex(self, v):
        n = len(self._dist_to)
        if v < 0 or v >= n:
            raise AttributeError(f'vertex {v} is not between 0 and {n - 1}')

    def __check(self, g, s):
        # either (1) there exists a negative cycle reachable from s ...
        if self.has_negative_cycle():
            weight = 0.0
            while not self.negative_cycle().empty():
                weight += self.negative_cycle().get().weight()
            if weight >= 0.0:
                print(f'error: weight of negative cycle = {weight}')
            return False
        # or ...
        # (2) for all edges e = v->w:   dist_to[w] <= dist_to[v] + e.weight()
        # (2`) for all edges e = v->w on the SPT: dist_to[w] == dist_to[v] + e.weight()

        # no negative cycle reachable from source
        else:
            # are dist_to[v] and edge_to[v] consistent?
            if self._dist_to[s] != 0.0 and self._edge_to[s] is not None:
                print('distanceTo[] and edgeTo[] inconsistent')
                return False
            for v in range(g.get_V()):
                if v == s:
                    continue
                if self._edge_to[v] is None and self._dist_to[v] is not math.inf:
                    print('distanceTo[] and edgeTo[] inconsistent')
                    return False
            # check (2)
            for v in range(g.get_V()):
                for e in g.adj_vertices(v):
                    w = e.item.head()
                    if self._dist_to[v] + e.item.weight() < self._dist_to[w]:
                        print(f'edge {e} is not relaxed')
                        return False
            # check (2`)
            for w in range(g.get_V()):
                if self._edge_to[w] is None:
                    continue
                e = self._edge_to[w]
                v = e.tail()
                if w != e.head():
                    return False
                if self._dist_to[v] + e.weight() != self._dist_to[w]:
                    print(f'edge {e} on shortest path not tight')
                    return False
        print('satisfies optimality conditions')
        print()
        return True

    def __repr__(self):
        return f'<{self.__class__.__name__}(\n' \
               f'_dist_to={self._dist_to}, \n' \
               f'_edge_to={self._edge_to})>'


def run_n():
    with open("../Resources/tinyEWDn.txt", ) as f:
        values = "".join(f.readlines()).splitlines()
        V, E = int(values[0]), int(values[1])
        g = EdgeWeightedDigraph(V)
        for line in values[2:]:
            vertices = line.split(' ')
            v, w, weight = int(vertices[0]), int(vertices[1]), float(vertices[2])
            e = DirectedEdge(v, w, weight)
            g.add_edge(e)
    s = 0
    sp = BellmanFordSP(g, s)

    if sp.has_negative_cycle():
        q = sp.negative_cycle()
        while not q.empty():
            print(q.get())
    else:
        for t in range(g.get_V()):
            if sp.has_path_to(t):
                print(f'{s} to {t} ({sp.dist_to(t)}) ', end="")
                q = sp.path_to(t)
                while not q.empty():
                    print(q.get())
                print()
            else:
                print(f'{s} to {t} no path\n')


def run_nc():
    with open("../Resources/tinyEWDnc.txt", ) as f:
        values = "".join(f.readlines()).splitlines()
        V, E = int(values[0]), int(values[1])
        g = EdgeWeightedDigraph(V)
        for line in values[2:]:
            vertices = line.split(' ')
            v, w, weight = int(vertices[0]), int(vertices[1]), float(vertices[2])
            e = DirectedEdge(v, w, weight)
            g.add_edge(e)
    s = 0
    sp = BellmanFordSP(g, s)

    if sp.has_negative_cycle():
        print('negative cycle')
        q = sp.negative_cycle()
        while not q.empty():
            print(q.get())
    else:
        for t in range(g.get_V()):
            if sp.has_path_to(t):
                print(f'{s} to {t} ({sp.dist_to(t)}) ', end="")
                q = sp.path_to(t)
                while not q.empty():
                    print(q.get())
                print()
            else:
                print(f'{s} to {t} no path\n')


def main():
    # run_n()
    run_nc()


if __name__ == '__main__':
    main()
