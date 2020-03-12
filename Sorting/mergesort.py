# Basic mergesort implementation
# 1. Continuously split the lists into 2 lists, then 4 lists, then 8 lists etc. until single list per element. 
# 2 repeatedly merge pairs of lists using the merge algorithm. Merge into sorted pairs first. 
# 3 merge pairs of lists again. merge to 4 elements per list again. Now we have two sorted lists of size four.
# 4 merge the two 4 element lists into one sorted list. 
# TC: O(n log n) best, avg, worst case

class MergeSort:

    def merge_sort(self, array):
        n = len(array)
        if n > 1:
            mid = n // 2 
            L = array[:mid]
            R = array[mid:]
            self.merge_sort(L)
            self.merge_sort(R)
            return self.__merge(array, L, R)


    def __merge(self, array, L, R):
        i, j, k  = 0, 0, 0 
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]        
                i += 1
            else:
                array[k] = R[j]
                j += 1 
            k += 1 
        while i < len(L):
            array[k] = L[i]
            i += 1 
            k += 1 
        while j < len(R):
            array[k] = R[j]
            j += 1 
            k += 1 
        return array
    

def main():
    array = [5, 2, 1, 4, 9]
    m = MergeSort()
    print(m.merge_sort(array))

main()







