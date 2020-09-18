"""
alphabet.py
 *  A data type for alphabets, for use with string-processing code
 *  that must convert between an alphabet of size R and the integers
 *  0 through R-1.
"""
import sys


class Alphabet:

    @staticmethod
    def base64():
        return Alphabet("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")

    def __init__(self, alpha):
        unicode = [False] * sys.maxunicode
        for i in range(len(alpha)):
            c = ord(alpha[i])
            if unicode[c]:
                raise ValueError(f'Illegal alphabet: repeated character = {c}')
            unicode[c] = True
        self._alphabet = [ord(c) for c in alpha]
        self._R = len(alpha)
        self._inverse = [-1 for _ in range(sys.maxunicode)]
        for c in range(self._R):
            self._inverse[self._alphabet[c]] = c

    def contains(self, c):
        return self._inverse[ord(c)] != -1

    def radix(self):
        return self._R

    def lg_r(self):
        lg_r = 0
        t = self._R - 1
        while t >= 1:
            lg_r += 1
            t /= 2
        return lg_r

    def to_index(self, c):
        if ord(c) >= len(self._inverse) or self._inverse[ord(c)] == -1:
            raise AttributeError(f'character {c} is not in the alphabet')
        return self._inverse[ord(c)]

    def to_indices(self, s):
        source = list(s)
        target = [0] * len(s)
        for i in range(len(source)):
            target[i] = self.to_index(source[i])
        return target

    def to_char(self, index):
        if index < 0 or index >= self._R:
            raise AttributeError(f'index must be between 0 and {self._R}: {index}')
        return chr(self._alphabet[index])

    def to_chars(self, indices):
        s = ''
        for i in range(len(indices)):
            s += self.to_char(indices[i])
        return s


def main():
    encoded = Alphabet.base64().to_indices('NowIsTheTimeForAllGoodMen')
    print(encoded)
    decoded = Alphabet.base64().to_chars(encoded)
    print(decoded)


if __name__ == '__main__':
    main()