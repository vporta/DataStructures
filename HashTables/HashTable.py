"""
HashTable.py.
@description The HashTable.py module defines a class, HashTable.
@author Vincent Porta. 

#-------------------------------------------------
Time complexity in big O notation.
# Algorithm       Average       Worst case
# Space             O(n)            O(n)
# Search            O(1)            O(n)
# Insert            O(1)            O(n)
# Delete            O(1)            O(n)
#-------------------------------------------------

"""


class HashTable:

    def __init__(self, length=10):
        self.length = length
        self.array = [[] for i in range(length)]

    def hash(self, key):
        length = len(self.array)
        return hash(key) % length

    def add(self, key, value):
        # if self.is_full():
        #     return 
        index = self.hash(key)
        if self.array[index] is not None:
            for kvp in self.array[index]:
                if kvp[0] == key:
                    kvp[1] = value
                    break
            else:
                self.array[index].append([key, value])
        else:
            self.array[index] = []
            self.array[index].append([key, value])

    def get(self, key):
        index = self.hash(key)
        if self.array[index] is None:
            raise KeyError()
        else:
            for kvp in self.array[index]:
                if kvp[0] == key:
                    return kvp[1]
            raise KeyError()

    def is_full(self):
        items = 0
        for item in self.array:
            if item is not None:
                items += 1
        return items > len(self.array) // 2

    def double(self):
        ht2 = HashTable(length=len(self.array) * 2)
        for i in range(len(self.array)):
            if self.array[i] is None:
                continue
            for kvp in self.array[i]:
                ht2.add(kvp[0], kvp[1])
        self.array = ht2.array

    def __repr__(self):
        return f"<HashTable(array={self.array})>"

    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        i = hash(key) % len(self.array)
        print(i)
        for j in range(len(self.array[i])):
            if self.array[i][j][0] == key:
                return True
        return False

    def __iter__(self):
        yield from self.array


def main():
    hm = HashTable()
    print(hm)
    hm.add(0, 'vincent')
    hm['foo'] = 'bar'
    hm.add(1, 'bob')
    # hm.add(2, 'bert')
    hm.add(3, 'jerry')
    print(hm)
    print()
    for kvp in hm:
        print(kvp)

    if 'foo' in hm:
        print('exists')
