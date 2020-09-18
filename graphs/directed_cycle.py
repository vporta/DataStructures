"""
directed_cycle.py
Finds a directed cycle in a digraph.

"""
from graphs.digraph import Digraph
from collections import deque


class DirectedCycle:

    _cycle = None  # stack

    def __init__(self, g):
        self._g = g
        self._marked = [False for _ in range(g.get_V())]
        self._on_stack = [False for _ in range(g.get_V())]  # is there vertex on the stack?
        self._edge_to = [0 for _ in range(g.get_V())]
        for v in range(g.get_V()):
            if not self._marked[v] and self._cycle is None:
                self.__dfs(g, v)

    def get_g(self):
        return self._g

    def get_cycle(self):
        if list(self._cycle) is not None:
            return list(self._cycle)
        return None

    def get_edge_to(self):
        return self._edge_to

    def get_marked(self):
        return self._marked

    def __dfs(self, g, v):
        self._marked[v] = True
        self._on_stack[v] = True
        for w in g.adj_vertices(v):
            # directed cycle found
            if self._cycle is not None:
                return
            # found new vertex, recur
            elif not self._marked[w.item]:
                self._edge_to[w.item] = v
                self.__dfs(g, w.item)
            # trace back directed cycle
            elif self._on_stack[w.item]:
                self._cycle = deque()
                x = v
                while x != w.item:
                    self._cycle.append(x)
                    x = self._edge_to[x]
                self._cycle.append(w.item)
                self._cycle.append(v)
                assert self.__check()

        self._on_stack[v] = False

    def has_cycle(self):
        return self._cycle is not None

    def cycle(self):
        return self.get_cycle()

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
               f'cycle={self._cycle}\n' \
            f'edge_to={self.get_edge_to()}\n' \
        f'marked={self.get_marked()})>'


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

    finder = DirectedCycle(g)
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

