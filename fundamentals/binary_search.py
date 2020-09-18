"""
binary_search.py
"""


class BinarySearch:

    @staticmethod
    def index_of(a, key):
        lo, hi = 0, len(a) - 1
        while lo <= hi:
            mid = hi + lo // 2  # lo + (hi - lo) / 2
            if key < a[mid]:
                hi = mid - 1
            elif key > a[mid]:
                lo = mid + 1
            else:
                return mid
        return -1


def main():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(BinarySearch.index_of(a, 10))


if __name__ == '__main__':
    main()