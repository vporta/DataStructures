"""
directed_cycle_x.py
Find a directed cycle in a digraph, using a nonrecursive, queue-based
 *  algorithm. Runs in O(E + V) time.
"""
from collections import deque
from graphs.digraph import Digraph


class DirectedCycleX:

    _cycle = None

    def __init__(self, g):
        self._g = g
        self._marked = [False for _ in range(g.get_V())]
        self._edge_to = [0 for _ in range(g.get_V())]
        # indegrees of remaining vertices
        indegree = [g.indegree(v) for v in range(g.get_V())]
        # initialize queue to contain all vertices with indegree = 0
        queue = deque()
        for v in range(g.get_V()):
            if indegree[v] == 0:
                queue.appendleft(v)
        while queue:
            v = queue.pop()
            for w in g.adj_vertices(v):
                indegree[w.item] -= 1
                if indegree[w.item] == 0:
                    queue.appendleft(w)

        # there is a directed cycle in subgraph of vertices with indegree >= 1
        edge_to = [0 for _ in range(g.get_V())]
        root = -1  # any vertex with indegree >= -1
        for v in range(g.get_V()):
            if indegree[v] == 0:
                continue
            else:
                root = v
            for w in g.adj_vertices(v):
                if indegree[w.item] > 0:
                    edge_to[w.item] = v
        if root != -1:
            visited = [False for _ in range(g.get_V())]
            while not visited[root]:
                visited[root] = True
                root = edge_to[root]
            self._cycle = deque()  # stack
            v = root
            while v != root:
                self._cycle.append(v)
                v = edge_to[v]
            self._cycle.append(root)
        assert self.__check()

    def get_g(self):
        return self._g

    def get_cycle(self):
        return list(self._cycle)

    def cycle(self):
        return self.get_cycle()

    def has_cycle(self):
        return self.get_cycle() is not None

    def __check(self):
        if self.has_cycle():
            first, last = -1, -1
            for v in self.cycle():
                if first == -1:
                    first = v
                last = v
            if first != last:
                print(f'cycle begins with {first} and ends with {last}')
                return False

        return True

    def __repr__(self):
        return f'<{self.__class__.__name__}(\n' \
               f'g={self.get_g()}, \n' \
               f'cycle={self.get_cycle()}\n' \



def main():
    g = Digraph(13)
    with open("../resources/tinyDG.txt", ) as f:
        for line in f.readlines():
            vertices = " ".join(line.splitlines()).split(' ')
            if len(vertices) < 2:
                continue
            else:
                v1, v2 = int(vertices[0]), int(vertices[1])
                g.add_edge(v1, v2)

    finder = DirectedCycleX(g)
    print(finder)
    if finder.has_cycle():
        print('Directed cycle')
        for v in finder.get_cycle():
            print(f'{v} ', end="")
        print()
    else:
        print('No directed cycle')



if __name__ == '__main__':
    main()

