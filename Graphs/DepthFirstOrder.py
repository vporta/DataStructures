"""
Compute preorder and postorder for a digraph or edge-weighted digraph.
 *  Runs in O(E + V) time.
 The DepthFirstOrder class represents a data type for
 *  determining depth-first search ordering of the vertices in a digraph
 *  or edge-weighted digraph, including preorder, postorder, and reverse postorder.
 *
 *  This implementation uses depth-first search.
 *  Each constructor takes Theta(V + E) time,
 *  where V is the number of vertices and E is the
 *  number of edges.
 *  Each instance method takes Theta(1) time.
 *  It uses Theta(V) extra space (not including the digraph).
"""
from Graphs.DirectedEdge import DirectedEdge
from Graphs.Digraph import Digraph
from Graphs.EdgeWeightedDigraph import EdgeWeightedDigraph
from queue import Queue, LifoQueue


class DepthFirstOrder:
    _pre_counter, _post_counter = 0, 0

    def __init__(self, g):
        self._pre = [0 for _ in range(g.get_V())]  # pre[v]    = preorder  number of v
        self._post = [0 for _ in range(g.get_V())]  # post[v]   = postorder number of v
        self._postorder = Queue()  # queue
        self._preorder = Queue()  # queue
        self._marked = [False for _ in range(g.get_V())]
        for v in range(g.get_V()):
            if not self._marked[v]:
                self.__dfs(g, v)

        # assert self.__check()

    def __dfs(self, g, v):
        if isinstance(g, Digraph):
            self._marked[v] = True
            self._pre_counter += 1
            self._pre[v] = self._pre_counter
            self._preorder.put(v)
            for w in g.adj_vertices(v):
                if not self._marked[w.item]:
                    self.__dfs(g, w.item)
            self._postorder.put(v)
            self._post_counter += 1
            self._post[v] = self._post_counter
        else:
            self._marked[v] = True
            #  Preorder: Put the vertex on a queue before the recursive calls
            self._pre_counter += 1
            self._pre[v] = self._pre_counter
            self._preorder.put(v)
            for e in g.adj_vertices(v):
                #       tail()   weight        head()
                # e  =   v   -------------->   w
                w = e.item.head()
                if not self._marked[w]:
                    self.__dfs(g, w)
            # Postorder: Put the vertex on a queue after the recursive calls.
            self._postorder.put(v)
            self._post_counter += 1
            self._post[v] = self._post_counter

    def pre(self, v):
        self._validate_vertex(v)
        return self._pre[v]

    def post(self, v):
        self._validate_vertex(v)
        return self._post[v]

    def preorder_vertices(self):
        return list(self._preorder.queue)

    def postorder_vertices(self):
        return list(self._postorder.queue)

    def _validate_vertex(self, v):
        n = len(self._marked)
        if v < 0 or v >= n:
            raise ValueError(f'vertex {v} is not between 0 and {n - 1}')

    def reverse_post(self):
        # Reverse postorder: Put the vertex on a stack after the recursive calls.
        reverse = LifoQueue()  # stack
        for v in self.postorder_vertices():
            reverse.put(v)
        rp = list()
        while not reverse.empty():
            rp.append(reverse.get())
        return rp

    def __check(self):
        r = 0
        for v in self.postorder_vertices():
            if self.post(v) != r:
                print('post(v) and post() inconsistent')
                return False
            r += 1

        r = 0
        for v in self.preorder_vertices():
            if self.pre(v) != r:
                print('pre(v) and pre() inconsistent')
                return False
            r += 1

        return True

    def __repr__(self):
        return f'<{self.__class__.__name__}(' \
               f'_pre={self._pre}' \
               f'_post={self._post}' \
               f'_preorder={self._preorder.queue}' \
               f'_postorder={self._postorder.queue}' \
               f'_marked={self._marked}' \
               f'_pre_counter={self._pre_counter}' \
               f'_post_counter={self._post_counter} ' \
               f')>'


def main():
    g = Digraph(13)
    with open("../Resources/tinyDAG.txt", ) as f:
        for line in f.readlines():
            vertices = " ".join(line.splitlines()).split(' ')
            if len(vertices) < 2:
                continue
            else:
                v1, v2 = int(vertices[0]), int(vertices[1])
                g.add_edge(v1, v2)
    print(g)
    dfs = DepthFirstOrder(g)
    print(dfs)
    print("v    pre   post")
    print("--------------------")
    for v in range(g.get_V()):
        print(f'{v}     {dfs.pre(v)}     {dfs.post(v)}\n')

    print('Pre-order')
    for v in dfs.preorder_vertices():
        print(f'{v} ', end="")
    print()
    print('Post-order')
    for v in dfs.postorder_vertices():
        print(f'{v} ', end="")
    print()
    print(dfs.postorder_vertices())
    print('Reverse Post-order')
    q1 = dfs.reverse_post()
    for v in q1:
        print(f'{v} ', end="")


if __name__ == '__main__':
    main()




