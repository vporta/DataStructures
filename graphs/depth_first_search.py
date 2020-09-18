"""
depth_first_search.py
Run depth first search on an undirected graph.
 *  Runs in O(E + V) time.

 ../resources/tinyG.txt
 *  13 vertices, 13 edges
 *  0: 6 2 1 5
 *  1: 0
 *  2: 0
 *  3: 5 4
 *  4: 5 6 3
 *  5: 3 4 0
 *  6: 0 4
 *  7: 8
 *  8: 7
 *  9: 11 10 12
 *  10: 9
 *  11: 9 12
 *  12: 11 9
"""
from graphs.bag import Bag
from graphs.graph import Graph


class DepthFirstSearch:
    _count = 0

    def __init__(self, g, s):
        """
        :param g: the graph
        :param s: the source vertex
        """
        self._marked = [False for _ in range(g.get_V())]
        self.g = g
        if isinstance(s, Bag):
            assert isinstance(s, Bag)
            self.__validate_vertices(s)
            for v in s:
                if not self._marked[v.item]:
                    self.__dfs(g, v.item)
        else:
            self.__validate_vertex(s)
            self.__dfs(g, s)

    def get_g(self):
        return self.g

    def __dfs(self, g, v):
        """
        :param g: the Graph
        :param v: the vertex
        """
        self._count += 1
        self._marked[v] = True
        for w in g.adj_vertices(v):
            # print('item', w.item, w)
            if not self._marked[w.item]:
                self.__dfs(g, w.item)

    def marked(self, v):
        """
        Is there a path between the source vertex s and vertex v?
        :param v: the vertex
        :return:  True if there is a path, False otherwise
        """
        self.__validate_vertex(v)
        return self._marked[v]

    def __validate_vertex(self, v):
        """
        :param v: v the vertex
        :return: throw an AttributeError unless 0 <= v < V
        """
        marked_vertices = len(self._marked)
        if v < 0 or v >= marked_vertices:
            raise AttributeError(f'vertex {v} is not between 0 and {marked_vertices-1}')

    def __validate_vertices(self, vertices):
        if vertices is None:
            raise AttributeError('argument is None')
        for v in vertices:
            if v is None:
                raise ValueError('vertex is None')
            self.__validate_vertex(v.item)

    def count(self):
        return self._count


def main(s):
    file_name = '../resources/tinyG.txt'
    with open(file_name) as f:
        ints = list()
        for line in f.read().split('\n'):
            ints.append(line)
        vertices, edges = int(ints[0]), int(ints[1])
    graph = Graph(vertices)
    print(graph)
    inp = ints[2:]  # skip first     lines vertices and edges

    for i in range(edges):
        v, w = inp[i].split(' ')
        graph.add_edge(int(v), int(w))
    print(graph)

    search = DepthFirstSearch(graph, int(s))
    for v in range(graph.get_V()):
        if search.marked(v):
            print(f'{v} ')
    print()
    if search.count() != graph.get_V():
        print('Not connected.')
    else:
        print('Connected')


if __name__ == '__main__':
    main(input('Enter: '))

