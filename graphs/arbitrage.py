"""
arbitrage.py
Arbitrage detection.
The Arbitrage class provides a client that finds an arbitrage
 *  opportunity in a currency exchange table by constructing a
 *  complete-digraph representation of the exchange table and then finding
 *  a negative cycle in the digraph.
 *
 *  This implementation uses the Bellman-Ford algorithm to find a
 *  negative cycle in the complete digraph.
 *  The running time is proportional to V 3in the
 *  worst case, where V is the number of currencies.
"""
from graphs.bellman_ford_sp import BellmanFordSP
from graphs.edge_weighted_digraph import EdgeWeightedDigraph
from graphs.directed_edge import DirectedEdge
import math


class Arbitrage:

    @staticmethod
    def run():
        V = 5
        names = ['USD', 'EUR', 'GBP', 'CHF', 'CAD']
        rates = [[1, 0.741, 0.657, 1.061, 1.005],
                 [1.349, 1, 0.888, 1.433, 1.366],
                 [1.521, 1.126, 1, 1.614, 1.538],
                 [0.942, 0.698, 0.619, 1, 0.953],
                 [0.995, 0.732, 0.650, 1.049, 1]]

        g = EdgeWeightedDigraph(V)

        for v in range(V):
            for w in range(V):
                e = DirectedEdge(v, w, -math.log(rates[v][w]))
                g.add_edge(e)
        # print(g)
        spt = BellmanFordSP(g, 0)
        # print(spt)
        print(spt.negative_cycle().queue)
        print(spt.has_negative_cycle())
        if spt.has_negative_cycle():
            print('hit')
            stake = 1000.0
            for e in spt.negative_cycle().queue:
                print(e)
                print(f'{stake} {names[e.tail()]}')
                stake *= math.exp(-e.weight())
                print(f'= {stake}\n {names[e.head()]}')
        else:
            print('No arbitrage opportunity')


def main():
    Arbitrage.run()


if __name__ == '__main__':
    main()














