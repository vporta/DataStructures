"""
SymbolTable.py
A SymbolTable object is a collection of key-value pairs. This
# implementation uses a hash table.
"""
from HashTables.stdarray import *


class SymbolTable:

    def __init__(self, m=10):
        self._m = m
        self._keys = create2D(m, 0)
        self._vals = create2D(m, 0)

    def __getitem__(self, key):
        i = hash(key) % self._m
        for j in range(len(self._keys[i])):
            if self._keys[i][j] == key:
                return self._vals[i][j]
        raise KeyError

    def __setitem__(self, key, val):
        i = hash(key) % self._m
        for j in range(len(self._keys[i])):
            if self._keys[i][j] == key:
                self._vals[i][j] = val
                return
        self._keys[i] += [key]
        self._vals[i] += [val]

    def __contains__(self, key):
        i = hash(key) % self._m
        for j in range(len(self._keys[i])):
            if self._keys[i][j] == key:
                return True
        return False

    def __iter__(self):
        a = []
        for i in range(self._m):
            a += self._keys[i]
        return iter(a)

    def __str__(self):
        return f"<SymbolTable(_m = {self._m}, _keys = {self._keys}, _vals = {self._vals})>"

    def __repr__(self):
        return str(self)

    # -----------------------------------------------------------------------


# For testing.

def main():
    import stdio

    # Test the constructor.
    st = SymbolTable()

    # Test __setitem__():
    st['Sedgewick'] = 'Bob'
    st['Wayne'] = 'Kevin'
    st['Dondero'] = 'Bob'

    # Test __getitem__():
    stdio.writeln(st['Sedgewick'])
    stdio.writeln(st['Wayne'])
    stdio.writeln(st['Dondero'])

    # Test __contains__():
    if 'Dondero' in st:
        stdio.writeln('Dondero found')
    else:
        stdio.writeln('Dondero not found')
    if 'Kernighan' in st:
        stdio.writeln('Kernighan found')
    else:
        stdio.writeln('Kernighan not found')

    # Test iteration:
    for key in st:
        stdio.writeln(key + ': ' + st[key])
    print(st)


if __name__ == '__main__':
    main()

# -----------------------------------------------------------------------
