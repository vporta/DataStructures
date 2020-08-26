"""
EdgeWeightedDirectedCycle.py
Finds a directed cycle in an edge-weighted digraph.
 *  Runs in O(E + V) time.
 * See DirectedCycle for analysis.
"""
from Graphs.EdgeWeightedDigraph import EdgeWeightedDigraph
from Graphs.DirectedEdge import DirectedEdge
from queue import LifoQueue


class EdgeWeightedDirectedCycle:



    def __init__(self, g):
        self._marked = [False for _ in range(g.get_V())]
        self._on_stack = [False for _ in range(g.get_V())]
        self._edge_to = [DirectedEdge() for _ in range(g.get_V())]
        self._cycle = None
        for v in range(g.get_V()):
            if not self._marked[v]:
                self.__dfs(g, v)

        assert self.__check()

    def __dfs(self, g: EdgeWeightedDigraph, v):
        self._on_stack[v] = True
        self._marked[v] = True
        for e in g.adj_vertices(v):
            w = e.item.head()
            # short circuit if directed cycle found
            if self._cycle is not None:
                return
            # found new vertex so recur
            elif not self._marked[w]:
                self._edge_to[w] = e
                self.__dfs(g, w)
            # trace back directed cycle
            elif self._on_stack[w]:
                self._cycle = LifoQueue()
                f = e
                while f.item.tail() != w:
                    self._cycle.put(f.item)
                    f = self._edge_to[f.item.tail()]
                self._cycle.put(f.item)
                return

        self._on_stack[v] = False

    def has_cycle(self):
        return self._cycle is not None

    def cycle(self):
        return self._cycle

    def __check(self):
        # edge weighted digraph is cyclic
        if self.has_cycle():
            # verify cycle
            first, last = None, None
            while not self.cycle().empty():
                e = self.cycle().get()
                if first is None:
                    first = e
                if last is not None:
                    if last.head() != e.tail():
                        print(f'cycle edges {last} and {e} not incident\n')
                        return False
                last = e
            if last.head() != first.tail():
                print(f'cycle edges {last} and {first} not incident\n')
                return False

        return True

    def __repr__(self):
        return f'<{self.__class__.__name__}(' \
               f'_marked={self._marked}, ' \
               f'_on_stack={self._on_stack}, ' \
               f'_edge_to={self._edge_to})>'


def main():
    g = EdgeWeightedDigraph(8)
    with open("../Resources/tinyEWD.txt", ) as f:
        for line in f.readlines():
            vertices = " ".join(line.splitlines()).split(' ')
            if len(vertices) < 3:
                continue
            else:
                v, w, weight = int(vertices[0]), int(vertices[1]), float(vertices[2])
                e = DirectedEdge(v, w, weight)
                g.add_edge(e)

    print(g)
    finder = EdgeWeightedDirectedCycle(g)
    print(finder)

    if finder.has_cycle():
        print('cycle')
        while not finder.cycle().empty():
            e = finder.cycle().get()
            print(f'{e} ')
        print()
    else:
        print('No directed cycle')


if __name__ == '__main__':
    main()
