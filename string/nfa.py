"""
nfa.py
Input: "(A*B|AC)D" 'AAAABD'
Output: True

 *  The  NFA class provides a data type for creating a
 *  non-deterministic finite state automaton (NFA) from a regular
 *  expression and testing whether a given string is matched by that regular
 *  expression.
 *  It supports the following operations: concatenation,
 *  closure, binary or, and parentheses.
 *  It does not support multi-way or, character classes,
 *  metacharacters (either in the text or pattern),
 *  capturing capabilities, greedy or reluctant
 *  modifiers, and other features in industrial-strength implementations.
 *  This implementation builds the NFA using a digraph and a stack
 *  and simulates the NFA using digraph search (see the textbook for details).
 *  The constructor takes time proportional to m, where m
 *  is the number of characters in the regular expression.
 *  The recognizes method takes time proportional to m * n,
 *  where n is the number of characters in the text.
"""

from graphs.bag import Bag
from graphs.digraph import Digraph
from graphs.directed_dfs import DirectedDFS
from queue import LifoQueue


class NFA:

    def __init__(self, regex):
        m = len(regex)
        graph = Digraph(m + 1)
        ops = LifoQueue()  # stack of states

        for i in range(m):
            lp = i
            # for left parentheses add Epsilon transition to next state, and push state index to stack
            if regex[i] == '(' or regex[i] == '|':  # '|' is operator for or
                # if the regex has left parentheses '(' or the '|' meta-characters,
                # push the *state index [i]* of the meta-character on the stack
                ops.put(i)

            # if we encounter a right parentheses, pop the corresponding left parentheses and/or '|'
            elif regex[i] == ')':
                _or = ops.get()
                # 2-way or operator
                if regex[_or] == '|':
                    lp = ops.get()
                    graph.add_edge(lp, _or + 1)
                    graph.add_edge(_or, i)

                else:
                    lp = _or
                # else:
                #     assert False

            # closure operator * (uses 1-character lookahead)
            if i < m - 1 and regex[i + 1] == '*':
                graph.add_edge(lp, i + 1)
                graph.add_edge(i + 1, lp)
            if regex[i] in ("(", "*", ")"):
                graph.add_edge(i, i + 1)
        if ops.qsize() != 0:
            raise ValueError('Invalid regular expression')
        self._m = m
        self._graph = graph
        self._regex = regex

    def recognizes(self, txt):
        # first create a digraph starting from state 0
        dfs = DirectedDFS(self._graph, 0)
        pc = Bag()
        # find a set of states reachable from start 0
        for v in range(self._graph.get_V()):
            if dfs.marked(v):
                pc.add(v)

        # Compute possible NFA states for txt[i+1]
        for i in range(len(txt)):
            # read next input character
            if txt[i] == '*' or txt[i] == '|' or txt[i] == '(' or txt[i] == ')':
                raise ValueError(f'text contains the meta-character "{txt[i]}"')
            match = Bag()
            for v in pc:
                if v.item == self._m:
                    continue
                if self._regex[v.item] == txt[i] or self._regex[v.item] == '.':
                    match.add(v.item + 1)
            dfs = DirectedDFS(self._graph, match)
            # print('dfs',dfs)
            pc = Bag()
            for v in range(self._graph.get_V()):
                if dfs.marked(v):
                    pc.add(v)
            if pc.size() == 0:
                return False

        # check for accept state
        for v in pc:
            if v.item == self._m:
                return True
        return False

    def __repr__(self):
        return f'<{self.__class__.__name__}(' \
               f'm={self._m} ' \
               f'regex={self._regex} ' \
               f'graph={self._graph})>'


def main():
    regex = "(A*B|AC)D"
    txt = "AAAAC"
    nfa = NFA(regex)
    print(nfa)
    print(nfa.recognizes(txt))
    print(nfa)


if __name__ == '__main__':
    main()
