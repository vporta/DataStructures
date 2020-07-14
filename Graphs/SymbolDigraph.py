"""
SymbolDigraph.py
The SymbolDigraph class represents a digraph, where the
 *  vertex names are arbitrary strings.
 *  By providing mappings between string vertex names and integers,
 *  it serves as a wrapper around the
 *  Digraph data type, which assumes the vertex names are integers
 *  between 0 and V - 1.
 *  It also supports initializing a symbol digraph from a file.
 *
 *  This implementation uses an ST to map from strings to integers,
 *  an array to map from integers to strings, and a Digraph to store
 *  the underlying graph.
 *  The index_of and contains operations take time
 *  proportional to log V, where V is the number of vertices.
 *  The name_of operation takes constant time.
"""
from collections import defaultdict
from Graphs.Digraph import Digraph


class SymbolDigraph:

    def __init__(self, file_name, delimiter=" "):
        self._st = defaultdict(int)

        # First pass builds the index by reading strings to associate
        # distinct strings with an index
        with open(f"../resources/{file_name}.txt", ) as f:
            for line in f.readlines():
                a = " ".join(line.splitlines()).split(delimiter)
                for i in range(len(a)):
                    if a[i] not in self._st:
                        self._st[a[i]] = len(self._st)

        # inverted index to get string keys in an array
        self._keys = ['' for _ in range(len(self._st))]
        for name in self._st.keys():
            self._keys[self._st.get(name)] = name

        # second pass builds the digraph by connecting first vertex on each
        # line to all others
        self._graph = Digraph(len(self._st))
        with open(f"../resources/{file_name}.txt", ) as f:
            for line in f.readlines():
                a = " ".join(line.splitlines()).split(delimiter)
                v = self._st.get(a[0])
                for i in range(1, len(a)):
                    w = self._st.get(a[i])
                    self._graph.add_edge(v, w)

    def contains(self, s):
        return s in self._st

    def index_of(self, s):
        return self._st.get(s)

    def name_of(self, v):
        self.__validate_vertex(v)
        if isinstance(v, int):
            return self._keys[v]
        else:
            return self._keys[v.item]

    def digraph(self):
        return self._graph

    def __validate_vertex(self, v):
        n = self._graph.get_V()
        if isinstance(v, int):
            if v < 0 or v >= n:
                raise ValueError(f'vertex {v} is not between 0 and {n - 1}')
        else:
            if v.item < 0 or v.item >= n:
                raise ValueError(f'vertex {v} is not between 0 and {n - 1}')

    def __repr__(self):
        return f'<{self.__class__.__name__}(_st={self._st}, _graph={self._graph}, _keys={self._keys})>'


def main():
    sg = SymbolDigraph('routes')
    print(sg)
    graph = sg.digraph()
    for v in graph.adj_vertices(sg.index_of('ORD')):
        print(f'     {sg.name_of(v)}')


if __name__ == '__main__':
    main()


