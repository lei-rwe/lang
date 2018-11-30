import random
import unittest

def left(n):
    return 2 * n + 1
def right(n):
    return 2 * n + 2
def parent(n):
    return 0 if n==0 else (n-1)//2

# Assume that the binary trees rooted at
# LEFT(i) and RIGHT(i) are max-heaps, but
# A[i] might be smaller than its children
# and thus violating the heap property
# Time complexity: O(lgn)
def max_heapify(A, i, heap_size):
    l = left(i)
    r = right(i)
    if l < heap_size and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r < heap_size and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[largest], A[i] = A[i], A[largest]
        max_heapify(A, largest, heap_size)

# Time complexity: O(n)
# Note here that O(nlgn) is not tight
def build_max_heap(A, heap_size):
    for i in range(parent(len(A)-1), -1, -1):
        max_heapify(A, i, heap_size)

def heapsort(A):
    build_max_heap(A, len(A))
    for i in range(0, len(A)-1):
        A[0], A[len(A)-1-i] = A[len(A)-1-i], A[0]
        max_heapify(A, 0, len(A)-1-i)

class heaptest(unittest.TestCase):
    def test_max_heapfify(self):
        A = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
        T = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
        print('Original array is:           ', A)
        max_heapify(A, 1, len(A))
        print('After max-heapify, array is: ', A)
        self.assertSequenceEqual(A, T)

        A = [6, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        T = [9, 7, 8, 6, 6, 5, 4, 3, 2, 1]
        print('Original array is:           ', A)
        max_heapify(A, 0, len(A))
        print('After max-heapify, array is: ', A)
        self.assertSequenceEqual(A, T)
    def test_build_max_heap(self):
        A = list(range(10))
        T = [9, 8, 6, 7, 4, 5, 2, 0, 3, 1]
        print('Original array is: ', A)
        build_max_heap(A, len(A))
        print('max heap is:       ', A)
        self.assertSequenceEqual(A, T)

        A = list(range(4))
        T = [3, 1, 2, 0]
        print('Original array is: ', A)
        build_max_heap(A, len(A))
        print('max heap is:       ', A)
        self.assertSequenceEqual(A, T)

        A = list(range(20))
        T = [19, 18, 14, 17, 10, 12, 13, 16, 8, 9, 1, 11, 5, 2, 6, 15, 7, 3, 0, 4]
        print('Original array is: ', A)
        build_max_heap(A, len(A))
        print('max heap is:       ', A)
        self.assertSequenceEqual(A, T)

    def test_heap_sort(self):
        A = list(range(10))
        random.shuffle(A)
        heapsort(A)
        self.assertSequenceEqual(A, range(10))

        A = list(range(10000))
        random.shuffle(A)
        heapsort(A)
        self.assertSequenceEqual(A, range(10000))

if __name__ == '__main__':
    unittest.main()