"""
outcast.py
Outcast detection.
"""
from graphs.word_net import WordNet


class Outcast:

    def __init__(self, wordnet: WordNet):
        self._wordnet = wordnet

    def outcast(self, nouns):
        # which noun is the least related to the others?
        # compute the sum of the distances between each noun and every other one
        xt = None  # outcast noun
        dt = 0  # max(dt, di)
        for i in range(len(nouns)):
            di = 0  # distance(xi, x1)   +   distance(xi, x2)   +   ...   +   distance(xi, xn)
            for j in range(len(nouns)):
                xi, xj = nouns[i], nouns[j]
                di += self._wordnet.distance(xi, xj)
            if di > dt:
                dt = di
                xt = nouns[i]
        return xt

    def __repr__(self):
        return f'<{self.__class__.__name__}(wordnet={self._wordnet})>'


def main():
    nouns = ['horse', 'table', 'zebra', 'cat', 'bear']
    synsets, hypernyms = '../resources/synsets.txt', '../resources/hypernyms.txt'
    wordnet = WordNet(synsets, hypernyms)
    outcast = Outcast(wordnet)
    print(outcast)
    print(outcast.outcast(nouns))


if __name__ == '__main__':
    main()