"""
 **************************************************** 
 * Ported from Java to Python. Taken from https://algs4.cs.princeton.edu/41graph
 * Execution: python DepthFirstPaths.py 
 * Dependencies: Graph.py 
 ****************************************************

 **
 *  The {@code DepthFirstPaths} class represents a data type for finding
 *  paths from a source vertex <em>s</em> to every other vertex
 *  in an undirected graph.
 *  <p>
 *  This implementation uses depth-first search.
 *  The constructor takes &Theta;(<em>V</em> + <em>E</em>) time in the
 *  worst case, where <em>V</em> is the number of vertices and
 *  <em>E</em> is the number of edges.
 *  Each instance method takes &Theta;(1) time.
 *  It uses &Theta;(<em>V</em>) extra space (not including the graph).
 *  <p>
 *  For additional documentation, see
 *  <a href="https://algs4.cs.princeton.edu/41graph">Section 4.1</a>   
 *  of <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
 *
 *  @author Robert Sedgewick
 *  @author Kevin Wayne
 **
"""
from collections import deque 
from Graph import Graph

class DepthFirstPaths:

    def __init__(self, G, s):
        """
        Computes a path between :param s: and every other vertex in graph :param G:.
        :param G: G the graph 
        :param s: s the source vertex
        """
        self.s = s 
        self.edge_to = [-1 for _ in range(G.number_of_V())]
        self.marked = [False for _ in range(G.number_of_V())]
        self._validate_vertex(s)
        self._dfs(G, s)

    def _dfs(self, G, v):
        """
        depth first search from v
        :param G: G the graph 
        :param v: v the source vertex
        """
        self.marked[v] = True 
        for w in G.adj_vertices(v):
            if not self.marked[w.item]:
                self.edge_to[w.item] = v
                self._dfs(G, w.item)

    def has_path_to(self, v):
        """
        is there a path between the source vertex s and vertex :param v:?
        :param v: v the vertex 
        :returns: true if there is a path, false otherwise 
        """
        self._validate_vertex(v)
        return self.marked[v]

    def path_to(self, v):
        """
        Returns a path between the source vertex {s} and vertex {v}, or {None} if no such path.
        :param v: the vertex
        :returns: the sequence of vertices on a path between the source vertex {s} and vertex {v}, as an Iterable
        """
        self._validate_vertex(v)
        if not self.has_path_to(v): return f"No such path to {v}"
        path = deque()  # acts as a stack. Holds integers
        x = v 
        while x != self.s:
            path.append(x)
            x = self.edge_to[x]
        path.append(self.s)
        return path 

    def _validate_vertex(self, v):
        V = len(self.marked)
        if v < 0 or v >= V: raise ValueError(f'vertex {v} is not between 0 and {V-1}')

    def __repr__(self):
        return f'<Graph(s = {self.s}, marked={self.marked}, edge_to = {self.edge_to})>'


def main():
    g = Graph(6)
    print(g) 
    g.add_edge(0, 1)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 0)
    g.add_edge(0, 5)
    g.add_edge(5, 0)
    g.add_edge(1, 2)
    g.add_edge(2, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 2)
    g.add_edge(2, 4)
    g.add_edge(4, 2)
    g.add_edge(3, 4)
    g.add_edge(4, 3)
    g.add_edge(3, 5)
    g.add_edge(5, 3)

    print(g)
    dfs = DepthFirstPaths(g, 1)
    print(dfs)
    # print('has_path_to: %s' % dfs.has_path_to(2))
    print('path_to: %s' % dfs.path_to(0))

main()









