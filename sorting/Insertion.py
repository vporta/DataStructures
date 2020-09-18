"""
Insertion.py
Insertion sort implementation.
"""



class Insertion:

    @staticmethod
    def sort(a):
        N = len(a)
        print(a)
        for i in range(N):
            for j in range(i, 0, -1):
                if Insertion._less(a[j], a[j - 1]):
                    Insertion._exch(a, j, j - 1)
                else:
                    break
        print(a)
        
    @staticmethod
    def _less(v, w) -> bool:
        return v < w 

    @staticmethod
    def _exch(a, i, j):
        a[i], a[j] = a[j], a[i]


Insertion.sort([8, 4, 2, 5, 21])
Insertion.sort(['r', 'a', 'g', 'b'])


