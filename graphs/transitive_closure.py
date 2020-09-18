"""
transitive_closure.py
Compute transitive closure of a digraph and support
 *  reachability queries.
 *  Preprocessing time: O(V(E + V)) time.
 *  Query time: O(1).
 *  Space: O(V^2).
"""
from graphs.digraph import Digraph
from graphs.directed_dfs import DirectedDFS


class TransitiveClosure:

    def __init__(self, g: Digraph):
        self._tc = [DirectedDFS(g, v) for v in range(g.get_V())]

    def reachable(self, v, w):
        self.__validate_vertex(v)
        self.__validate_vertex(w)
        return self._tc[v].marked(w)

    def __validate_vertex(self, v):
        n = len(self._tc)
        if v < 0 or v >= n:
            raise ValueError(f'vertex {v} is not between 0 and {n - 1}')