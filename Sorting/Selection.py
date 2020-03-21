"""
Selection.py
Selection sort implementation.
"""



class Selection:

    @staticmethod
    def sort(a):
        N = len(a)
        print(a)
        for i in range(N):
            _min = i 
            for j in range(i+1, N):
                if Selection._less(a[j], a[_min]):
                    _min = j 
            Selection._exch(a, i, _min)
        print(a)
        
    @staticmethod
    def _less(v, w) -> bool:
        return v < w 

    @staticmethod
    def _exch(a, i, j):
        a[i], a[j] = a[j], a[i]



Selection.sort([8, 4, 2, 5, 21])
Selection.sort(['r', 'a', 'g', 'b'])


