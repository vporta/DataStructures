"""
Topological.py
Compute topological ordering of a DAG or edge-weighted DAG.
 *  Runs in O(E + V) time.

 The Topological class represents a data type for
 *  determining a topological order of a directed acyclic graph (DAG).
 *  A digraph has a topological order if and only if it is a DAG.
 *  The has_order operation determines whether the digraph has
 *  a topological order, and if so, the order operation
 *  returns one.
 *
 *  This implementation uses depth-first search.
 *  The constructor takes Theta(V + E) time in the
 *  worst case, where V is the number of vertices and E
 *  is the number of edges.
 *  Each instance method takes Theta(1) time.
 *  It uses Theta(V) extra space (not including the digraph).
"""
from Graphs.Digraph import Digraph
from Graphs.EdgeWeightedDigraph import EdgeWeightedDigraph
from Graphs.EdgeWeightedDirectedCycle import EdgeWeightedDirectedCycle
from Graphs.DepthFirstOrder import DepthFirstOrder
from Graphs.DirectedCycle import DirectedCycle
from Graphs.SymbolDigraph import SymbolDigraph


class Topological:

    _order = None
    _rank = None

    def __init__(self, g):
        if isinstance(g, Digraph):
            print('g is a Digraph')
            finder = DirectedCycle(g)
            if not finder.has_cycle():
                dfs = DepthFirstOrder(g)
                self._order = dfs.reverse_post()
                self._rank = [0 for _ in range(g.get_V())]
                i = 0
                for v in self._order:
                    i += 1
                    self._rank[v] = i
        if isinstance(g, EdgeWeightedDigraph):
            print('g is an EdgeWeightedDigraph')
            finder = EdgeWeightedDirectedCycle(g)
            print(finder)
            if not finder.has_cycle():
                dfs = DepthFirstOrder(g)
                self._order = dfs.reverse_post()

    def order(self):
        return self._order

    def has_order(self):
        return self._order is not None

    def rank(self, v):
        self.__validate_vertex(v)
        if self.has_order():
            return self._rank[v]
        else:
            return -1

    def __validate_vertex(self, v):
        n = len(self._rank)
        if v < 0 or v >= n:
            raise ValueError(f'vertex {v} is not between 0 and {n - 1}')

    def __repr__(self):
        return f'<{self.__class__.__name__}(_order={self.order()}, _rank={self._rank})>'


def main():
    sg = SymbolDigraph('jobs', '/')
    print(sg)
    topological = Topological(sg.digraph())
    print(topological)
    for v in topological.order():
        print(sg.name_of(v))


if __name__ == '__main__':
    main()








