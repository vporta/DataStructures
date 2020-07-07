"""
NonrecursiveDirectedDFS.py
Run nonrecurisve depth-first search on an directed graph.
 *  Runs in O(E + V) time.
"""
from Graphs.Digraph import Digraph
from collections import deque
import sys


class NonrecursiveDirectedDFS:

    def __init__(self, g, s):
        """
        :param g: the Digraph
        :param s: the source vertex
        """
        self._marked = [False for _ in range(g.get_V())]
        self.__validate_vertex(s)
        adj = [0 for _ in range(g.get_V())]
        for v in range(g.get_V()):
            adj[v] = g.adj_vertices(v).__iter__()

        stack = deque()
        self._marked[s] = True
        stack.append(s)
        while stack:
            v = stack[-1]  # peek
            try:
                n = next(adj[v])
                if n.next:
                    w = n.next.item
                    if not self._marked[w]:
                        self._marked[w] = True
                        stack.append(w)
                else:
                    stack.pop()
            except StopIteration:
                print(StopIteration('stop'))
                break

    def get_marked(self):
        return self._marked

    def marked(self, v):
        self.__validate_vertex(v)
        return self.get_marked()[v]

    def __validate_vertex(self, v):
        n = len(self.get_marked())
        if v < 0 or v >= n:
            raise AttributeError(f'vertex {v} is not between 0 and {n-1}')

    def __repr__(self):
        return f'<{self.__class__.__name__}()>'


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
    s = 2
    dfs = NonrecursiveDirectedDFS(graph, s)
    print(dfs)
    for v in range(graph.get_V()):
        if dfs.marked(v):
            print(f'{s} is connected to {v} ')
        else:
            print(f'{s} not connected to {v}')


if __name__ == '__main__':
    main()