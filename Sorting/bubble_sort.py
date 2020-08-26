# Bubble sort 
# O(n**2)


def bubble_sort(array):
    is_sorted = False
    n = len(array) - 1 
    while not is_sorted:
        is_sorted = True 
        for i in range(n):
            j = i + 1
            if array[i] > array[j]:
                swap(array, i, j)
                is_sorted = False 
        n -= 1
    return array


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def main():
    array = [8, 5, 7, 2, 10]
    print(bubble_sort(array))

if __name__ == '__main__':
    main()