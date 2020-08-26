"""
LSD.py
*  LSD radix sort
 *
 *    - Sort a String[] array of n extended ASCII strings (R = 256), each of length w.
 *
 *    - Sort an int[] array of n 32-bit integers, treating each integer as
 *      a sequence of w = 4 bytes (R = 256).
 *
 *  Uses extra space proportional to n + R.
"""


class LSD:
    BITS_PER_BYTE = 8
    R = 256  # extend ASCII alphabet size
    count = None
    aux = None

    @classmethod
    def sort(cls, a, w):
        n = len(a)
        cls.aux = [''] * n

        def _sort(d=w-1):

            while d >= 0:

                # sort by key-indexed counting on dth character
                cls.count = [0 for _ in range(cls.R + 1)]

                # compute frequency counts
                for i in range(n):
                    cls.count[ord(a[i][d]) + 1] += 1

                # compute cumulates
                for r in range(cls.R):
                    cls.count[r + 1] += cls.count[r]

                # move data
                for i in range(n):
                    cls.aux[cls.count[ord(a[i][d])]] = a[i]
                    cls.count[ord(a[i][d])] += 1

                # copy back
                for i in range(n):
                    a[i] = cls.aux[i]
                d -= 1

        return _sort()


def main():
    with open("../Resources/words3.txt") as f:
        a = "".join(f.readlines()).splitlines()
        words = []
        w = len(a[0].split(' '))
        for line in a:
            assert w == len(line.split(' '))
            words.extend(line.split())
        LSD.sort(words, len(words[0]))
        for item in words:
            print(item)


if __name__ == '__main__':
    main()
