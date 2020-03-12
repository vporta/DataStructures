class Heap:

    def __init__(self):
        self.__array = []
        self.__last_index = -1

    def __get_parent(self, index):
        # O(1)
        if index == 0:
            return None, None
        parent_index =  (index - 1) // 2
        # return parent index and value
        return parent_index, self.__array[parent_index]

    def push(self, value):
        # Big O(logn)
        self.__array.append(value)
        self.__last_index += 1
        self.__siftup(self.__last_index)

    def pop(self):
        # Big O(logn)
        if self.__last_index == -1:
            raise IndexError("Can't pop from empty heap")
        root_value = self.__array[0]
        if self.__last_index > 0:  # more than one element in the heap
            self.__array[0] = self.__array[self.__last_index]
            self.__siftdown(0)
        self.__last_index -= 1
        return root_value

    def __siftup(self, index):
        """ 
        Swaps a node that is too large with its parent (thereby moving it up) until it is no larger than the node above it. The build_heap function takes an array of unsorted items and moves them until it they all satisfy the heap property.
        """
        current_value = self.__array[index]
        parent_index, parent_value = self.__get_parent(index)
        if index > 0 and self.compare(current_value, parent_value):
            self.__array[parent_index], self.__array[index] = current_value, parent_value
            self.__siftup(parent_index)
        return

    def __siftdown(self, index):
        """
        Swaps a node that is too small with its largest child (thereby moving it down) until it is at least as large as both nodes below it.
        """
        current_value = self.__array[index]
        left_child_index, left_child_value = self.__get_left_child(index)
        right_child_index, right_child_value = self.__get_right_child(index)
        # the following works because if the right_child_index is not None, then the left_child
        # is also not None => property of a complete binary tree, else left will be returned.
        best_child_index, best_child_value = (left_child_index, left_child_value)
        if right_child_index is not None and self.compare(right_child_value, left_child_value):
            best_child_index, best_child_value = (right_child_index, right_child_value)
        if best_child_index is not None and self.compare(best_child_value, current_value):
            self.__array[index], self.__array[best_child_index] = best_child_value, current_value
            self.__siftdown(best_child_index)
        return

    def compare(self, value1, value2):
        raise NotImplementedError("Should not use the baseclass heap instead use the class MinHeap or MaxHeap.")

    def __get_left_child(self, index):
        """ Get left child"""
        left_child_index = 2 * index + 1  # 2i + 1
        if left_child_index > self.__last_index:
            return None, None
        return left_child_index, self.__array[left_child_index]

    def __get_right_child(self, index):
        """ Get right child """
        right_child_index = 2 * index + 2  # 2i + 2
        if right_child_index > self.__last_index:
            return None, None
        return right_child_index, self.__array[right_child_index]

    def peek(self):
        if not self.__array:
            return None 
        return self.__array[0]

    def replace(self, new_value):
        """ remove root & put NEW element as root & sift down -> no need to sift up """
        if self.__last_index == -1:
            raise IndexError("Can't pop from empty heap")
        root_value = self.__array[0]
        self.__array[0] = new_value
        self.__siftdown(0)
        return root_value

    # this method works like max_heapify. It is particular to this class. 
    def heapify(self, input_list):
        # O(logn)
        """
            each leaf is a trivial subheap, so we may begin to call
            Heapify on each parent of a leaf.  Parents of leaves begin
            at index n/2.  As we go up the tree making subheaps out
            of unordered array elements, we build larger and larger
            heaps, joining them at the i'th element with Heapify,
            until the input list is one big heap.
        """
        n = len(input_list)
        self.__array = input_list
        self.__last_index = n - 1
        for index in reversed(range(n // 2)):
            self.__siftdown(index)

    @classmethod
    def build_heap(cls, input_list):
        # O(nlogn) upper bound. 
        # Asymptotically tight is O(n)
        """ Create a heap based on an inputed list. """
        heap = cls()
        heap.heapify(input_list)
        return heap

    def __max_heapify(self, arr, n, index):
        # O(log n)
        largest = index
        self.__array = arr
        left = self.__get_left_child(index)
        right = self.__get_right_child(index)

        if left < n and self.__array[i] < self.__array[left]:
            largest = left 

        if right < n and self.__array[largest] < self.__array[right]:
            largest = right 

        if largest != index:
            self.__array[largest], self.__array[index] = self.__array[index], self.__array[largest]
            self.__max_heapify(self.__array, n, largest)

    def heap_sort(self, arr):
        n = len(arr)
        for i in range(n, -1, -1):
            self.__max_heapify(arr, n, i)
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.__max_heapify(arr, i, 0)
        print(arr)
        return arr

    def __repr__(self):
        return str(self.__array[:self.__last_index+1])

    def __eq__(self, other):
        if isinstance(other, Heap):
            return self.__array == other.__array
        if isinstance(other, list):
            return self.__array == other
        return NotImplementedError


class MinHeap(Heap):
    def compare(self, value1, value2):
        return value1 < value2

class MaxHeap(Heap):
    def compare(self, value1, value2):
        return value1 > value2

minh = MinHeap.build_heap([2,7,3,1,9,44,23]) == [1, 2, 3, 7, 9, 44, 23]
maxh = MaxHeap.build_heap([2,7,3,1,9,44,23]) == [44, 9, 23, 1, 7, 3, 2]

# print(minh, maxh)

from hypothesis import given, assume
import hypothesis.strategies as st

@given(st.lists(st.integers()))
def test_minheap(l):
    h = MinHeap.build_heap(l)
    s = sorted(l)
    for i in range(len(s)):
        assert(h.pop() == s[i])

@given(st.lists(st.integers()))
def test_maxheap(l):
    h = MaxHeap.build_heap(l)
    s = sorted(l, reverse=True)
    for i in range(len(s)):
        assert(h.pop() == s[i])


      





