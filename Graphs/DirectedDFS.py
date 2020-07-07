"""
DirectedDFS.py
Determine single-source or multiple-source reachability in a digraph
 *  using depth first search.
 *  Runs in O(E + V) time.

The DirectedDFS class represents a data type for
 *  determining the vertices reachable from a given source vertex s
 *  (or set of source vertices) in a digraph. For versions that find the paths,
 *  see DepthFirstDirectedPaths and BreadthFirstDirectedPaths.
 *
 *  This implementation uses depth-first search.
 *  The constructor takes time proportional to V + E
 *  (in the worst case),
 *  where V is the number of vertices and E is the number of edges.
 *  Each instance method takes Theta(1) time.
 *  It uses Theta(V) extra space (not including the digraph).
"""
from Graphs.Digraph import Digraph
from Graphs.DepthFirstSearch import DepthFirstSearch


class DirectedDFS(DepthFirstSearch):

    def __init__(self, g, s):
        super().__init__(g, s)
        """
        :param g: the digraph  
        :param s: the source vertex
        """

    def __repr__(self):
        return f'<{self.__class__.__name__}(g={self.get_g()}, count={super().count()})>'


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
    s = 6
    dfs = DirectedDFS(graph, int(s))
    print(dfs)
    for v in range(graph.get_V()):
        if dfs.marked(v):
            print(f'{v} ')


if __name__ == '__main__':
    main()