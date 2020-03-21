"""
Shell.py
Shell sort implementation.
"""



class Shell:

    @staticmethod
    def sort(a):
        N = len(a)
        print(a)
        # 3x + 1 increment sequence: 1, 4, 13, 40 ...
        h = 1 
        while h < N // 3: 
            h = 3 * h + 1 
        while h >= 1:
            for i in range(h, N):
                j = i 
                while j >= h and Shell._less(a[j], a[j - h]):
                    Shell._exch(a, j, j - h)
                    j -= h
            h /= 3
        assert Shell.is_sorted(a, round(h))
        print(a)
        
    @staticmethod
    def _less(v, w) -> bool:
        return v < w 

    @staticmethod
    def _exch(a, i, j):
        a[i], a[j] = a[j], a[i]

    @staticmethod
    def is_sorted(a, h):
        for i in range(1, len(a)):
            if Shell._less(a[i], a[i - h]): return False 
        return True 



Shell.sort([8, 4, 2, 5, 21])
Shell.sort(['r', 'a', 'g', 'b'])


