"""
heap_sort.py
Sorts a sequence of strings from standard input using heapsort.
"""
from typing import *


class HeapSort:

    @staticmethod
    def sort(pq: List[str]):
        n = len(pq) 
        # heapify phase  
        k = n // 2 - 1    
        for i in range(k, -1, -1):
            HeapSort._sink(pq, i, k)

        # sortdown phase
        for i in range(n-1, 0, -1):
            HeapSort._exch(pq, 0, i)
            n -= 1 
            HeapSort._sink(pq, 0, n)

    @staticmethod
    def _sink(pq: List[str], k: int, n: int):
        while 2*k <= n:
            j = 2*k 
            if j+1 < n and HeapSort._less(pq, j+1, j+2): 
                j += 1
            if not HeapSort._less(pq, k, j): break 
            HeapSort._exch(pq, k, j)
            k = j 

    @staticmethod
    def _less(pq: List, i: int, j: int):
        return Comparator.compare_to(pq[i-1], pq[j-1]) < 0 

    @staticmethod
    def _exch(pq: List, i: int, j: int):
        pq[i-1], pq[j-1] = pq[j-1], pq[i-1] 

    @staticmethod
    def show(a):
        def _show():
            for element in a:
                print(element) 
        return _show() 

class Comparator:

    @staticmethod
    def compare_to(v, w):
        if v > w:
            return 1
        elif v == w:
            return 0
        else:
            return -1

def main():
    a = ['S', 'O', 'R', 'T', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
    print(a)
    print()
    HeapSort.sort(a)
    HeapSort.show(a)

if __name__ == '__main__':
    main()
