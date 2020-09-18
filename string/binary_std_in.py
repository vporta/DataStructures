"""
binary_std_in.py
*  Reads binary data from an input stream.
"""
import struct
import sys
from string.BinaryStdOut import BinaryStdOut


class BinaryStdIn:

    EOF = -1
    _in = sys.stdin.buffer
    _buffer = 0
    _n = 0
    _is_initialized = False

    @classmethod
    def __initialize(cls):
        cls._buffer = 0
        cls._n = 0
        cls.__fill_buffer()
        cls._is_initialized = True

    @classmethod
    def __fill_buffer(cls):
        x = cls._in.read(1)
        if x == b"":
            cls._buffer = cls.EOF
            cls._n = -1
            return
        cls._buffer = struct.unpack("B", x)[0]
        cls._n = 8

    @classmethod
    def close(cls):
        if not cls._is_initialized:
            cls.__initialize()
        cls._in.close()
        cls._is_initialized = False

    @classmethod
    def is_empty(cls):
        if not cls._is_initialized:
            cls.__initialize()
        return cls._buffer == cls.EOF

    @classmethod
    def read_bool(cls):
        if cls.is_empty():
            raise ValueError('Reading from empty input stream')
        cls._n -= 1
        bit = ((cls._buffer >> cls._n) & 1) == 1
        if cls._n == 0:
            cls.__fill_buffer()
        return bit

    @classmethod
    def read_char(cls):
        if cls.is_empty():
            raise ValueError('Reading from empty input stream')

        # special case when aligned byte
        if cls._n == 8:
            x = cls._buffer
            cls.__fill_buffer()
            return chr(x & 0xff)

        # combine last n bits of current buffer with first 8-n bits of new buffer
        x = cls._buffer
        x <<= (8 - cls._n)
        old_n = cls._n
        cls.__fill_buffer()
        if cls.is_empty():
            raise ValueError('Reading from empty input stream')
        cls._n = old_n
        x |= cls._buffer >> cls._n
        return chr(x & 0xff)

    @classmethod
    def read_char_r(cls, r):
        if r < 1 or r > 16:
            raise AttributeError(f'Illegal value of r = {r}')
        # optimize r = 8 case
        if r == 8:
            return cls.read_char()
        x = 0
        for i in range(r):
            x <<= 1
            bit = cls.read_bool()
            if bit:
                x |= 1
        return x

    @classmethod
    def read_str(cls):
        if cls.is_empty():
            raise EOFError('Reading from empty input stream')
        s = ""
        while not cls.is_empty():
            s += cls.read_char()
        return s

    @classmethod
    def read_int(cls):
        x = 0
        for i in range(4):
            b = cls.read_char()
            x <<= 8
            x |= ord(b)
        return x

    @classmethod
    def read_int_r(cls, r):
        if r < 1 or r > 16:
            raise AttributeError(f'Illegal value of r = {r}')
        if r == 32:
            return cls.read_int()
        if r < 1 or r > 32:
            raise ValueError(f'Illegal value for r = {r}')
        x = 0
        for _ in range(r):
            x <<= 1
            bit = cls.read_bool()
            if bit:
                x |= 1
        return x

    @classmethod
    def read_byte(cls):
        c = cls.read_char()
        return ord(c) & 0xff

    def __repr__(self):
        return f'<{self.__class__.__name__}(buffer={self._buffer}, n={self._n}, EOF={self.EOF})>'


def main():
    while not BinaryStdIn.is_empty():
        BinaryStdOut.write_char(BinaryStdIn.read_char())


if __name__ == '__main__':
    main()