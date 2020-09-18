"""
cls.y
 *  Write binary data to standard output, either one 1-bit boolean,
 *  one 8-bit char, one 32-bit int, one 64-bit double, one 32-bit float,
 *  or one 64-bit long at a time.
 *
 *  The bytes written are not aligned.
"""
import sys
import struct


class BinaryStdOut:
    _out = sys.stdout.buffer
    _buffer = 0
    _n = 0
    _is_initialized = False

    @classmethod
    def __initialize(cls):
        cls._buffer = 0
        cls._n = 0
        cls._is_initialized = True

    @classmethod
    def __write_bit(cls, bit):
        if not cls._is_initialized:
            cls.__initialize()

        # add bit to buffer
        cls._buffer <<= 1
        if bit:
            cls._buffer |= 1

        # if buffer is full (8 bits), write out as a single byte
        cls._n += 1
        if cls._n == 8:
            cls.__clear_buffer()

    @classmethod
    def __write_byte(cls, x):
        if not cls._is_initialized:
            cls.__initialize()
        assert 0 <= x < 256

        # optimized if byte-aligned
        if cls._n == 0:
            cls._out.write(struct.pack("B", x))
            return

        # otherwise write one bit at a time
        for i in range(0, 8):
            bit = ((x >> (8 - i - 1)) & 1) == 1
            cls.__write_bit(bit)

    @classmethod
    def __clear_buffer(cls):
        if not cls._is_initialized:
            cls.__initialize()
        if cls._n == 0:
            return
        if cls._n > 0:
            cls._buffer <<= 8 - cls._n
        try:
            cls._out.write(struct.pack("B", cls._buffer))
        except IOError as e:
            print(e)

        cls._n = 0
        cls._buffer = 0

    @classmethod
    def flush(cls):
        cls.__clear_buffer()
        cls._out.flush()

    @classmethod
    def close(cls):
        cls.flush()
        try:
            cls._out.close()
            cls._is_initialized = False
        except IOError as e:
            print(e)

    @classmethod
    def write_bool(cls, x):
        cls.__write_bit(x)

    @classmethod
    def write_byte(cls, x):
        cls.__write_byte(x & 0xFF)

    @classmethod
    def write_int(cls, x, r=32):
        if r == 32:
            cls.__write_byte(((x >> 24) & 0xFF))
            cls.__write_byte(((x >> 16) & 0xFF))
            cls.__write_byte(((x >> 8) & 0xFF))
            cls.__write_byte(((x >> 0) & 0xFF))
            return
        if r < 1 or r > 16:
            raise ValueError(f'Illegal value for r = {r}')
        if x < 0 or x >= (1 << r):
            raise ValueError(f'Illegal {r}-bit char = {x}')
        for i in range(0, r):
            bit = ((x >> (r - i - 1)) & 1) == 1
            cls.__write_bit(bit)

    @classmethod
    def write_char(cls, x, r=8):
        if r == 8:
            if ord(x) < 0 or ord(x) >= 256:
                raise ValueError(f'Illegal 8-bit char = {x}')
            cls.__write_byte(ord(x))
            return
        if r < 1 or r > 16:
            raise ValueError(f'Illegal value for r = {r}')
        if ord(x) >= (1 << r):
            raise ValueError(f'Illegal {r}-bit char = {x}')
        for i in range(0, r):
            bit = ((x >> (r - i - 1)) & 1) == 1
            cls.__write_bit(bit)

    @classmethod
    def write_string(cls, s, r=8):
        for i in s:
            cls.write_char(i, r)


def main():
    print(sys.argv)
    for i in sys.argv[1]:
        BinaryStdOut.write_char(i)
    BinaryStdOut.close()


if __name__ == "__main__":
    main()