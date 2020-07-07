# Graph API for an undirected graph
# uses an adjacency list representation 
# Uses Theta(E + V) space
# All instance methods take Theta(1) time 
from collections import defaultdict, deque
from Graphs.Bag import Bag


class Graph:

    def __init__(self, v):
        """
        Initializes an empty graph with V vertices and 0 edges.
        :param v: the number of vertices
        """
        if v < 0:
            raise ValueError('Number of vertices must be non-negative')
        self.V = v + 1
        self.E = 0
        # self.adj = defaultdict(deque)  /* without LinkedList */
        self.adj = defaultdict(Bag)
        for v in range(v):
            # self.adj[v] = deque()  /* without LinkedList */
            self.adj[v] = Bag()

    def get_V(self):
        """
        :returns: the number of vertices in this graph
        """
        return self.V

    def get_E(self):
        """
        :returns: the number of edges in this graph
        """
        return self.E

    def _validate_vertex(self, v):
        """
        Throw a ValueError exception if 0 <= v < V
        :param v: vertex v 
        """
        if v < 0 or v >= self.V:
            raise ValueError(f'vertex {v} is not between 0 and {self.V - 1}')

    def add_edge(self, v, w):
        self._validate_vertex(v)
        self._validate_vertex(w)
        self.E += 1
        self.adj[v].add(w)
        self.adj[w].add(v)

    def adj_vertices(self, v):
        """
        Returns the vertices adjacent to the vertex {v}
        :param v: v the vertex 
        :returns: the vertices adjacent to vertex {v} 
        """
        self._validate_vertex(v)
        return self.adj[v]

    def degree(self, v):
        self._validate_vertex(v)
        return self.adj[v].size()
        # return len(self.adj[v])

    def __repr__(self):
        return f"<Graph(V={self.V}, adj={self.adj})>"


def main():
    g = Graph(4)
    print(g)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    print(g)
    print(g.get_V())
    print(f'adjacent vertices of 2 are: {g.adj_vertices(2)}')
    print(f'degree of 2 is: {g.degree(2)}')

# main()
