# Quick Sort algorithm class 
# Big O notation.
#                 Algorithm       Best           Worst case
  # TC                            O(n log n)      O(n**2)
  # SC                            O(log n)        O(n)

import random 

class EmptyArrayException(Exception):
    pass

class Quick:

    @staticmethod 
    def sort(a):
        """
        Rearranges the array in ascending order
        :param a: array 
        """
        try:
            if not a: raise EmptyArrayException
            random.shuffle(a)
            Quick._sort(a, 0, len(a) -1)
            assert Quick.is_sorted(a)
        except EmptyArrayException as e:
            print(f'** Array cannot be empty: {a} **')
            print()

    @staticmethod
    def _sort(a, lo, hi):
        """
        quicksort the subarray from a[lo] to a[hi]
        :param a: array
        :param lo: lowest index of a
        :param hi: highest index of a 
        :returns: None
        :raises Exception: None
        """
        if hi <= lo: return 
        pivot = Quick._partition(a, lo, hi)
        Quick._sort(a, lo, pivot-1)
        Quick._sort(a, pivot+1, hi)
        assert Quick.is_sorted(a)


    @staticmethod
    def _partition(a, lo, hi):
        """
        _partition the subarray a[lo..hi] so that a[lo..j-1] <= a[j] <= a[j+1..hi]
        and return the index j.
        :param a: array
        :param lo: lowest index of a
        :param hi: highest index of a 
        :returns: None
        :raises Exception: None
        """
        if lo == hi:
            return lo 
        pivot = a[hi]
        for i in range(lo, hi):
            # all elements less than 'pivot' will be before the index 'lo'
            if a[i] < pivot:
                Quick.exch(a, i, lo)  # swap a[lo] with a[i] 
                lo += 1

        # put the pivot in its correct place
        Quick.exch(a, lo, hi)  # swap a[lo] with a[hi]
        return lo


    @staticmethod
    def is_sorted(a):
        """
        Check if array is sorted
        :param a: array 
        :returns: boolean
        """
        return Quick._is_sorted(a, 0, len(a) - 1)

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
            if Quick.less(a[i], a[i-1]): return False 
        return True 


# ***************************************************************************
# *  Helper sorting functions.
# ***************************************************************************

    @staticmethod
    def less(v, w):
        """
        is v < w ?
        :param v: value of array 
        :param w: value of array 
        :returns: boolean 
        """
        if v == w: return False 
        return Comparator.compare_to(v, w) < 0 

    @staticmethod
    def exch(a, i, j):
        """
        exchange a[i] and a[j]
        :param a: array 
        :param i: index i 
        :param j: index j         
        """
        a[i], a[j] = a[j], a[i]


    @staticmethod
    def show(a):
        for i in range(len(a)):
            print(a[i])

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
    array = [5, 22, 7, 8, 1]
    issorted = Quick.is_sorted(array)
    print(issorted)
    if not issorted:
        Quick.sort(array)
        Quick.show(array)
    issorted = Quick.is_sorted(array)
    print(issorted)

main()

        














