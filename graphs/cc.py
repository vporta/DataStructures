"""
cc.py
The CC class represents a data type for
determining the connected components in an undirected graph.
The id operation determines in which connected component
a given vertex lies; the connected operation
determines whether two vertices are in the same connected component;
the count operation determines the number of connected
components; and the size operation determines the number
of vertices in the connect component containing a given vertex.

The component identifier of a connected component is one of the
vertices in the connected component: two vertices have the same component
identifier if and only if they are in the same connected component.


This implementation uses depth-first search.
The constructor takes Theta;(V + E) time,
where V is the number of vertices and E is the
number of edges.
Each instance method takes Theta;(1) time.
It uses Theta;(V) extra space (not including the graph).

"""
from collections import deque
from graphs.graph import Graph


class CC:

    def __init__(self, g):
        """
        :param g: the Graph
        """
        self._g = g
        self._id = [0 for _ in range(g.get_V())]
        self._marked = [False for _ in range(g.get_V())]
        self._size = [0 for _ in range(g.get_V())]
        self._count = 0
        for v in range(g.get_V()):
            if not self.get_marked()[v]:
                self.__dfs(g, v)
                self._count += 1

    def get_g(self):
        return self._g

    def get_id(self):
        return self._id

    def get_marked(self):
        return self._marked

    def get_size(self):
        return self._size

    def get_count(self):
        return self._count

    def __dfs(self, g, v):
        self.get_marked()[v] = True
        self.get_id()[v] = self.get_count()
        self.get_size()[self.get_count()] += 1
        for w in g.adj_vertices(v):
            if not self.get_marked()[w.item]:
                self.__dfs(g, w.item)

    # Returns the component id of the connected component containing vertex v
    def id(self, v):
        self.validate_vertex(v)
        return self.get_id()[v]

    # Returns the number of vertices in the connected component containing vertex v
    def size(self, v):
        self.validate_vertex(v)
        return self.get_size()[self.get_id()[v]]

    # Returns true if vertices v and w are in the same connected component.
    def connected(self, v, w):
        self.validate_vertex(v)
        self.validate_vertex(w)
        return self.id(v) == self.id(w)

    def validate_vertex(self, v):
        n = len(self.get_marked())
        if v < 0 or v >= n:
            raise AttributeError(f'vertex {v} is not between 0 and {n-1}')

    def __repr__(self):
        return f'<{self.__class__.__name__}(\n' \
               f'g={self.get_g()}, \n' \
               f'id={self.get_id()}, \n' \
               f'size={self.get_size()}\n' \
               f'count={self.get_count()}\n' \
               f'marked={self.get_marked()})>'


def main():
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    cc = CC(g)
    print(cc)
    m = cc.get_count()
    print(f'{m} components')
    components = deque([deque() for _ in range(m)])

    for v in range(g.get_V()):
        components[cc.id(v)].append(v)
    for i in range(m):
        for v in components[i]:
            print(f'{v} ')
        print()


if __name__ == '__main__':
    main()

