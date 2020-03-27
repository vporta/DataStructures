"""
# Topdown and bottom up mergesort implementation
# 1. Continuously split the lists into 2 lists, then 4 lists, then 8 lists etc. until single list per element. 
# 2 repeatedly merge pairs of lists using the merge algorithm. Merge into sorted pairs first. 
# 3 merge pairs of lists again. merge to 4 elements per list again. Now we have two sorted lists of size four.
# 4 merge the two 4 element lists into one sorted list. 
# TC: O(n log n) best, avg, worst case
"""

# Top down
class Merge:

    
    @staticmethod
    def merge(a, aux, lo, mid, hi):
        aux = a[:]  # copy 
        i, j = lo, mid+1 
        for k in range(lo, hi+1):
            if i > mid: 
                j += 1 
                a[k] = aux[j]
            elif j > hi:
                i += 1 
                a[k] = aux[i]
            elif aux[j] < aux[i]:
                j += 1 
                a[k] = aux[j] 
            else:
                i += 1 
                a[k] = aux[i] 

    @staticmethod
    def _sort(a, aux, lo, hi):
        if hi <= lo: return
        mid = lo + (hi - lo) / 2
        Merge._sort(a, aux, lo, mid)
        Merge._sort(a, aux, mid + 1, hi)
        Merge.merge(a, aux, lo, mid, hi)

    @staticmethod
    def sort(a):
        aux = list() 
        Merge._sort(a, aux, 0, len(a) - 1)
        assert Merge.is_sorted(a)

    @staticmethod
    def is_sorted(a):
        """
        Check if array is sorted
        :param a: array 
        :returns: boolean
        """
        return Merge._is_sorted(a, 0, len(a) - 1)

    @staticmethod
    def _is_sorted(a, lo, hi):
        """
        Private method to check if array is sorted
        :param a: array 
        :param lo: lowest index of a
        :param hi: lowest index of a
        :returns: boolean 
        """
        for i in range(lo+1, hi):
            if a[i] == a[i-1]: return False 
            if a[i] < a[i-1]: return False 
        return True 

# bottom up 
class MergeBU:

    @staticmethod
    def merge(a, aux, lo, mid, hi):
        aux = a[:]  # copy 
        i, j = lo, mid+1 
        for k in range(lo, hi+1):
            if i > mid: 
                j += 1 
                a[k] = aux[j]
            elif j > hi:
                i += 1 
                a[k] = aux[i]
            elif aux[j] < aux[i]:
                j += 1 
                a[k] = aux[j] 
            else:
                i += 1 
                a[k] = aux[i] 

    @staticmethod
    def sort(a):
        n = len(a)
        aux = list()
        _len = 1
        lo = 0
        while _len < n:
            while lo < n - _len: 
                mid = lo + _len-1 
                hi = min(lo+_len+_len-1, n-1)
                MergeBU.merge(a, aux, lo, mid, hi)
                lo += _len + _len 
            _len *= 2


    @staticmethod
    def show(a):
        for el in a:
            print(el)



def main():
    array = [5, 2, 1, 4, 9]
    MergeBU.sort(array)
    MergeBU.show(array)

main()







