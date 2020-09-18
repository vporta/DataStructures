"""
cpm.py
Critical path method
The CPM class provides a client that solves the
 *  parallel precedence-constrained job scheduling problem
 *  via the critical path method. It reduces the problem
 *  to the longest-paths problem in edge-weighted DAGs.
 *  It builds an edge-weighted digraph (which must be a DAG)
 *  from the job-scheduling problem specification,
 *  finds the longest-paths tree, and computes the longest-paths
 *  lengths (which are precisely the start times for each job).
 *
 *  This implementation uses AcyclicLP to find a longest
 *  path in a DAG.
 *  The program takes Theta(V + E) time in
 *  the worst case, where V is the number of jobs and
 *  E is the number of precedence constraints.
"""
from graphs.acyclic_lp import AcyclicLP
from graphs.directed_edge import DirectedEdge
from graphs.edge_weighted_digraph import EdgeWeightedDigraph


class CPM:

    @staticmethod
    def run():
        with open("../resources/jobsPC.txt", ) as f:
            values = "".join(f.readlines()).splitlines()
            print(values)
            n = int(values[0])
            source, sink = 2*n, 2*n + 1
            durations = list()
            for x in values[1:]:
                durations.append(float(x.split(' ')[0]))
            precedent = list()
            print(values[1:])
            for prec in values[1:]:
                if prec.split('  ')[-1] == '0':
                    precedent.append([])
                else:
                    precedent.append("".join(prec.split('  ')[-1]).split(' '))

            print(n, durations, precedent)
            g = EdgeWeightedDigraph(2*n + 2)
            for i in range(n):
                g.add_edge(DirectedEdge(source, i, 0.0))
                g.add_edge(DirectedEdge(i + n, sink, 0.0))
                g.add_edge(DirectedEdge(i, i+n, durations[i]))

                m = len(precedent[i])
                for j in range(m):
                    p = int(precedent[i][j])
                    g.add_edge(DirectedEdge(n + i, p, 0.0))
            print(g)
        lp = AcyclicLP(g, source)
        print('job start finish')
        print('----------------')
        for i in range(n):
            print(f'{i}, {lp.dist_to(i)}, {lp.dist_to(i+n)}')
        print(f'finish time {lp.dist_to(sink)}')


def main():
    CPM.run()


if __name__ == '__main__':
    main()