"""
 **************************************************** 
 * Ported from Java to Python. Taken from https://algs4.cs.princeton.edu/41graph
 * Execution: python depth_first_paths.py
 * Dependencies: graph.py
 ****************************************************

 **
 *  The DepthFirstPaths class represents a data type for finding
 *  paths from a source vertex s to every other vertex
 *  in an undirected graph.
 *
 *  This implementation uses depth-first search.
 *  The constructor takes Theta;(V + E) time in the
 *  worst case, where V is the number of vertices and
 *  E is the number of edges.
 *  Each instance method takes Theta(1) time.
 *  It uses Theta(V) extra space (not including the graph).
 **
"""
from collections import deque 
from graphs.graph import Graph


class DepthFirstPaths:

    def __init__(self, g, s):
        """
        Computes a path between :param s: and every other vertex in graph :param g:.
        :param g: g the graph
        :param s: s the source vertex
        """
        self._g = g
        self._s = s
        self._edge_to = [0 for _ in range(g.get_V())]
        self._marked = [False for _ in range(g.get_V())]
        self._validate_vertex(s)
        # self.__non_recursive(g, s)
        self._dfs(g, s)

    def get_g(self):
        return self._g

    def get_s(self):
        return self._s

    def get_edge_to(self):
        return self._edge_to

    def get_marked(self):
        return self._marked

    def _dfs(self, g, v):
        """
        depth first search from v
        :param g: g the graph
        :param v: v the source vertex
        """
        self.get_marked()[v] = True
        for w in g.adj_vertices(v):
            if not self.get_marked()[w.item]:
                self.get_edge_to()[w.item] = v
                self._dfs(g, w.item)

    def has_path_to(self, v):
        """
        is there a path between the source vertex s and vertex :param v:?
        :param v: v the vertex 
        :returns: True if there is a path, False otherwise
        """
        self._validate_vertex(v)
        return self.get_marked()[v]

    def path_to(self, v):
        """
        Returns a path between the source vertex {s} and vertex {v}, or {None} if no such path.
        :param v: the vertex
        :returns: the sequence of vertices on a path between the source vertex {s} and vertex {v}, as an Iterable
        """
        self._validate_vertex(v)
        if not self.has_path_to(v):
            return None
        path = deque()  # acts as a stack. Holds integer vertices
        x = v 
        while x != self.get_s():
            path.append(x)
            x = self.get_edge_to()[x]
        path.append(self.get_s())
        return list(path)

    def _validate_vertex(self, v):
        marked_len = len(self.get_marked())
        if v < 0 or v >= marked_len:
            raise AttributeError(f'vertex {v} is not between 0 and {marked_len-1}')

    def __non_recursive(self, g, s):
        self._validate_vertex(s)
        stack = deque()
        self.get_marked()[s] = True
        stack.append(s)
        while stack:
            v = stack.pop()
            for w in g.adj[v]:
                if w.next is not None:
                    w = w.next
                    if not self.get_marked()[w.item]:
                        self.get_marked()[w.item] = True
                        self.get_edge_to()[w.item] = v
                        stack.append(w.item)
                else:
                    stack.pop()

    def __repr__(self):
        return f'<DepthFirstPaths(s = {self.get_s()}, marked={self.get_marked()}, edge_to = {self.get_edge_to()})>'


def main():
    g = Graph(6)
    print(g)
    g.add_edge(0, 5)
    g.add_edge(2, 4)
    g.add_edge(2, 3)
    g.add_edge(1, 2)
    g.add_edge(0, 1)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    g.add_edge(0, 2)

    print(g)
    s = 0
    dfs = DepthFirstPaths(g, s)
    print(dfs)
    for v in range(g.get_V()):
        if dfs.has_path_to(v):
            print(f'{s} to {v}')
            for x in reversed(dfs.path_to(v)):
                if x == s:
                    print(x, end="")
                else:
                    print(f' - {x}', end="")
            print()
        else:
            print(f'{s} to {v}: not connected\n')


if __name__ == '__main__':
    main()









