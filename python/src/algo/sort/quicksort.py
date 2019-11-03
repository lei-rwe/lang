import unittest
import random

class TestQsort(unittest.TestCase):
    def _test_range(self):
        print("test_range")
        for i in range(1, 5):
            print(i)

    def test_partition(self):
        A = [2, 2, 2, 2, 2, 2, 2, 2]
        print("\nOriginal array: ", A)
        partition(A, 0, len(A)-1)
        print("After partition, array: ", A)

    def test_partition_1(self):
        A = [2, 8, 7, 1, 3, 5, 6, 4]
        print("\nOriginal array: ", A)
        partition(A, 0, len(A)-1)
        print("After partition, array: ", A)

    def _test_partition_2(self):
        A = list(range(1, 9))
        random.shuffle(A)
        print("\nOriginal array: ", A)
        partition(A, 0, len(A)-1)
        print("After partition, array: ", A)

    def _test_qs_1(self):
        A = [2, 8, 7, 1, 3, 5, 6, 4]
        print("\nOriginal array: ", A)
        qsort(A, 0, len(A)-1)
        print("After qsort, array: ", A)


def partition(A, p, r):
    # This partition is from the book "Introduction to Algorithm - 3rd Edition p192"
    pivot = A[r]
    print("Using the last element {} as pivot to partition A[{}, {}] for array ".format(pivot, p, r), A)

    i = p - 1
    for j in range(p, r):
        if A[j] <= pivot:
            i = i + 1
            if i != j:
                A[i], A[j] = A[j], A[i]
                print("Found a smaller one {} at index {}, after exchange {} and {}: ".format(A[j], j, i, j), A)

    A[i+1], A[r] = A[r], A[i+1]
    return i + 1


def qsort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        qsort(A, p, q-1)
        qsort(A, q+1, r)


if __name__ == '__main__':
    print("in main")
    unittest.main()