"""
KosarajuSharirSCC.py
Compute the strongly-connected components of a digraph using the
 *  Kosaraju-Sharir algorithm.
 *  Runs in O (E + V ) time.
The KosarajuSharirSCC class represents a data type for
 *  determining the strong components in a digraph.
 *  The id operation determines in which strong component
 *  a given vertex lies; the strongly_connected operation
 *  determines whether two vertices are in the same strong component;
 *  and the count operation determines the number of strong
 *  components.
 *
 *  The component identifier of a component is one of the
 *  vertices in the strong component: two vertices have the same component
 *  identifier if and only if they are in the same strong component.
 *
 *  This implementation uses the Kosaraju-Sharir algorithm.
 *  The constructor takes Theta(V + E) time,
 *  where V is the number of vertices and E
 *  is the number of edges.
 *  Each instance method takes Theta(1) time.
 *  It uses Theta(V) extra space (not including the digraph).
 *  For alternative implementations of the same API
"""
from Graphs.DepthFirstOrder import DepthFirstOrder
from Graphs.Digraph import Digraph
from Graphs.TransitiveClosure import TransitiveClosure
from queue import Queue


class KosarajuSharirSCC:

    _count = 0

    def __init__(self, g):
        dfs = DepthFirstOrder(g.reverse())
        self._marked = [False for _ in range(g.get_V())]
        self._id = [0 for _ in range(g.get_V())]
        for v in dfs.reverse_post():
            if not self._marked[v]:
                self.__dfs(g, v)
                self._count += 1

        # check that id[] gives strong components
        assert self.__check(g)

    def __dfs(self, g, v):
        self._marked[v] = True
        self._id[v] = self._count
        for w in g.adj_vertices(v):
            if not self._marked[w.item]:
                self.__dfs(g, w.item)

    def count(self):
        return self._count

    def __validate_vertex(self, v):
        n = len(self._marked)
        if v < 0 or v >= n:
            raise ValueError(f'vertex {v} is not between 0 and {n - 1}')

    def is_strongly_connected(self, v, w):
        self.__validate_vertex(v)
        self.__validate_vertex(w)
        return self._id[v] == self._id[w]

    def id(self, v):
        self.__validate_vertex(v)
        return self._id[v]

    def __check(self, g):
        tc = TransitiveClosure(g)
        for v in range(g.get_V()):
            for w in range(g.get_V()):
                if self.is_strongly_connected(v, w) != tc.reachable(v, w) \
                        and self.is_strongly_connected(w, v) != tc.reachable(w, v):
                    return False
        return True


def main():
    file_name = '../resources/tinyDG.txt'
    with open(file_name) as f:
        ints = list()
        for line in f.read().split('\n'):
            ints.append(line)
        vertices, edges = int(ints[0]), int(ints[1])

    graph = Digraph(vertices)
    print(graph)
    inp = ints[2:]  # skip first 2 lines in tiny.DG.txt i.e. # of vertices and edges

    for i in range(edges):
        v, w = inp[i].split(' ')
        graph.add_edge(int(v), int(w))
    print(graph)

    scc = KosarajuSharirSCC(graph)
    m = scc.count()
    print(f'{m} strong components')
    components = [Queue() for _ in range(m)]
    for v in range(graph.get_V()):
        components[scc.id(v)].put(v)
    for i in range(m):
        for v in components[i].queue:
            print(f'{v} ', end="")
        print()


if __name__ == '__main__':
    main()




