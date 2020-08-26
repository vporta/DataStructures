"""
Huffman.py
  * Compress or expand a binary input stream using the Huffman algorithm.
  * $ python String/Huffman.py - < Resources/abra.txt | python String/BinaryDump.py 60
  *  010100000100101000100010010000110100001101010100101010000100
  *  000000000000000000000000000110001111100101101000111110010100
  *  120 bits
  *
  * $ python String/Huffman.py - < Resources/abra.txt | python String/Huffman.py +
  *  ABRACADABRA!
"""
from Queues.MinPQ import MinPQ
from String.BinaryStdIn import BinaryStdIn
from String.BinaryStdOut import BinaryStdOut
import sys


class Node:

    def __init__(self, ch, freq, left, right):
        self._ch = ch
        self._freq = freq
        self._left = left
        self._right = right

    def is_leaf(self):
        return self.__is_leaf()

    def __is_leaf(self):
        return self._left is None and self._right is None

    def __gt__(self, other):
        return self._freq > other._freq


class Huffman:
    R = 256

    @classmethod
    def compress(cls):
        s = BinaryStdIn.read_str()
        # Tabulate frequency counts
        freq = [0 for _ in range(cls.R)]
        for i in range(len(s)):
            freq[ord(s[i])] += 1

        # Build Huffman Trie
        root = cls.__build_trie(freq)

        # Build code table
        st = [None for _ in range(0, cls.R)]
        cls.__build_code(st, root, '')

        # print trie for decoder
        cls.__write_trie(root)

        # print number of bytes in original uncompressed message
        BinaryStdOut.write_int(len(s))

        # use Huffman code to encode input
        for i in range(len(s)):
            code = st[ord(s[i])]
            for j in range(len(code)):
                if code[j] == '0':
                    BinaryStdOut.write_bool(False)
                elif code[j] == '1':
                    BinaryStdOut.write_bool(True)
                else:
                    raise ValueError('Illegal state')
        BinaryStdOut.close()

    @classmethod
    def __build_trie(cls, freq):
        pq = MinPQ()
        for c in range(cls.R):
            if freq[c] > 0:
                pq.insert(Node(chr(c), freq[c], None, None))
        if pq.size() == 0:
            raise ValueError('Cannot be empty')
        if pq.size() == 1:
            if freq[ord("\0")] == 0:
                pq.insert(Node("\0", 0, None, None))
            else:
                pq.insert(Node("\1", 0, None, None))
        while pq.size() > 1:
            left = pq.del_min()
            right = pq.del_min()
            parent = Node("\0", left._freq + right._freq, left, right)
            pq.insert(parent)
        return pq.del_min()

    @classmethod
    def __build_code(cls, st, x, s):
        if not x.is_leaf():
            cls.__build_code(st, x._left, s + '0')
            cls.__build_code(st, x._right, s + '1')
        else:
            st[ord(x._ch)] = s

    @classmethod
    def __write_trie(cls, root):
        if root.is_leaf():
            BinaryStdOut.write_bool(True)
            BinaryStdOut.write_char(root._ch)
            return
        BinaryStdOut.write_bool(False)
        cls.__write_trie(root._left)
        cls.__write_trie(root._right)

    @classmethod
    def expand(cls):
        # read in Huffman trie from input stream
        root = cls.__read_trie()

        # number of bytes to write
        length = BinaryStdIn.read_int()

        # decode using the Huffman Trie
        for i in range(length):
            x = root
            while not x.is_leaf():
                bit = BinaryStdIn.read_bool()
                if bit:  # if bit == 1
                    x = x._right
                else:  # bit == 0
                    x = x._left
            BinaryStdOut.write_char(x._ch, 8)
        BinaryStdOut.close()

    @classmethod
    def __read_trie(cls):
        is_leaf = BinaryStdIn.read_bool()
        if is_leaf:
            return Node(BinaryStdIn.read_char(), -1, None, None)
        else:
            return Node('\0', -1, cls.__read_trie(), cls.__read_trie())


def main():
    if sys.argv[1] == "-":
        Huffman.compress()
    elif sys.argv[1] == "+":
        Huffman.expand()
    else:
        raise ValueError("Illegal command line argument")


if __name__ == '__main__':
    main()
