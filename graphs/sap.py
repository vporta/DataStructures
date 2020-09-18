"""
sap.py
Shortest Ancestral Path
An ancestral path between two vertices v and w in a digraph is a directed path from v to a common ancestor x,
together with a directed path from w to the same ancestor x. A shortest ancestral path is an ancestral path of
minimum total length. We refer to the common ancestor in a shortest ancestral path as a shortest common ancestor.
Note also that an ancestral path is a path, but not a directed path.
"""
from graphs.digraph import Digraph
from collections import defaultdict
from queue import Queue


class SAP:

    def __init__(self, g: Digraph):
        self._g = g

    def get_ancestors(self, v):
        q = Queue()
        m = defaultdict(int)
        q.put(v)
        m[v] = 0
        while not q.empty():
            to = q.get()
            current_distance = m.get(to)
            for w in self._g.adj_vertices(to):
                if w.item not in m or m[w.item] > current_distance + 1:
                    q.put(w.item)
                    m[w.item] = current_distance + 1
        return m

    def length(self, v, w):
        # length of shortest ancestral path between v and w; -1 if no such path
        self.__validate_vertex(v)
        self.__validate_vertex(w)
        ancestor_v = self.get_ancestors(v)
        ancestor_w = self.get_ancestors(w)
        distance = -1
        for key, value in ancestor_v.items():
            if key in ancestor_w:
                current_distance = ancestor_w.get(key) + value
                if distance < 0 or current_distance < distance:
                    distance = current_distance
        return distance

    def ancestor(self, v, w):
        # a common ancestor of v and w that participates in a shortest ancestral path; -1 if no such path
        self.__validate_vertex(v)
        self.__validate_vertex(w)
        ancestor_v = self.get_ancestors(v)
        ancestor_w = self.get_ancestors(w)
        distance, ancestor = -1, -1
        for key, value in ancestor_v.items():
            if key in ancestor_w:
                current_dist = ancestor_w.get(key) + value
                if distance < 0 or current_dist < distance:
                    distance = current_dist
                    ancestor = key
        return ancestor

    def any_length(self, v, w):
        # length of shortest ancestral path between any vertex in v and any vertex in w; -1 if no such path
        distance = -1
        for i in v:
            for j in w:
                current_distance = self.length(i, j)
                if current_distance > 0:
                    if distance < 0 or current_distance < distance:
                        distance = current_distance
        return distance

    def any_ancestor(self, v, w):
        # a common ancestor that participates in shortest ancestral path; -1 if no such path
        distance, ancestor = -1, None
        for i in v:
            for j in w:
                current_distance = self.length(i, j)
                if current_distance > 0:
                    if distance < 0 or current_distance < distance:
                        distance = current_distance
                        ancestor = self.ancestor(i, j)
        return ancestor

    def __validate_vertex(self, v):
        n = self._g.get_V()
        if v < 0 or v >= n:
            raise AttributeError(f'vertex {v} is not between 0 and {n - 1}')

    def __repr__(self):
        return f'<{self.__class__.__name__}(_g={self._g})>'


def main():
    with open("../resources/digraph1.txt") as f:
        values = "".join(f.readlines()).split('\n')
        V, E = int(values[0]), int(values[1])
        g = Digraph(V)
        sap = SAP(g)
        for line in values:
            vertices = "".join(line).split(' ')
            if len(vertices) < 2:
                continue
            else:
                v, w = int(vertices[0]), int(vertices[1])
                g.add_edge(v, w)
                length = sap.length(v, w)
                ancestor = sap.ancestor(v, w)
                print(f'length = {length}, ancestor={ancestor}')
    # sap = SAP(g)
    print(g)
    print(sap)
    # print(sap.get_ancestors(3))
    # print(sap.get_ancestors(2))
    # print(sap.ancestor(3, 2))


if __name__ == '__main__':
    main()
