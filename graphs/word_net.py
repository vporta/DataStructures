"""
word_net.py
synset: as set of synonyms
 * hyponym: specific synset
 * hypernym: more general synset
 WordNet also describes semantic relationships between synsets.
 One such relationship is the is-a relationship, which connects a hyponym (more specific synset)
 to a hypernym (more general synset). For example, the synset { gate, logic gate } is a hypernym
 of { AND circuit, AND gate } because an AND gate is a kind of logic gate.
"""
from collections import defaultdict
from graphs.bag import Bag
from graphs.digraph import Digraph
from graphs.sap import SAP
from graphs.directed_cycle import DirectedCycle


class WordNet:

    def __init__(self, synsets=None, hypernyms=None):
        self._nouns_dict = defaultdict(Bag)
        self._reverse_nouns_dict = defaultdict(str)
        max_id = 0

        with open(synsets) as f:
            lines = f.readlines()
            for line in lines:
                items = "".join(line.splitlines()).split(',')
                nouns = items[1].split(' ')

                for i in range(len(nouns)):
                    if nouns[i] not in self._nouns_dict:
                        nouns_list = Bag()
                    else:
                        nouns_list = self._nouns_dict.get(nouns[i])
                    nouns_list.add(int(items[0]))
                    self._nouns_dict[nouns[i]] = nouns_list
                self._reverse_nouns_dict[int(items[0])] = items[1]
                max_id = max(max_id, int(items[0]))

        self._dg = Digraph(max_id + 1)

        with open(hypernyms) as f1:
            lines = f1.readlines()
            for line in lines:
                items = "".join(line.splitlines()).split(',')
                v = int(items[0])
                for i in range(1, len(items)):
                    w = int(items[i])
                    self._dg.add_edge(v, w)

        # if not self._is_dag(self._dg):
        #     raise AttributeError('digraph is not acyclic')
        self._sap = SAP(self._dg)

    def nouns_dict(self):
        return self._nouns_dict

    def rev_nouns_dict(self):
        return self._reverse_nouns_dict

    def _is_dag(self, dg):
        dc = DirectedCycle(dg)
        return dc.has_cycle()

    def nouns(self):
        # returns all WordNet nouns
        return list(self._nouns_dict.keys())

    def is_noun(self, word):
        # is the word a WordNet noun?
        return True if word in self._nouns_dict else False

    def distance(self, noun_a, noun_b):
        # distance between noun_a and noun_b
        if not self.is_noun(noun_a) or not self.is_noun(noun_b):
            raise AttributeError(f'noun arguments to distance() not found')
        return self._sap.length(self._nouns_dict.get(noun_a).first.item, self._nouns_dict.get(noun_b).first.item)

    def sap(self, noun_a, noun_b):
        # a synset (second field of synsets.txt) that is the common ancestor of noun_a and noun_b
        # in a shortest ancestral path (defined below)
        if not self.is_noun(noun_a) or not self.is_noun(noun_b):
            raise AttributeError(f'noun arguments to distance() not found')
        _id = self._sap.ancestor(
            self._nouns_dict.get(noun_a).first.item,
            self._nouns_dict.get(noun_b).first.item)
        return self._reverse_nouns_dict.get(_id)

    def __repr__(self):
        return f'<{self.__class__.__name__}(' \
               f'_dg={self._dg})>'


def main():
    synsets, hypernyms = '../resources/synsets.txt', '../resources/hypernyms.txt'
    wordnet = WordNet(synsets, hypernyms)
    print(wordnet.nouns_dict())
    # print(wordnet.rev_nouns_dict())
    print(wordnet.distance('velum', 'soft_option'))
    print(wordnet.sap('velum', 'soft_option'))


if __name__ == '__main__':
    main()
