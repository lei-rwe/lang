import unittest
import random

def qsort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        qsort(A, p, q-1)
        qsort(A, q+1, r)

def partition(A, p, r):
    x = A[r]
    i = p
    for j in range(p, r):
        if A[j] < x:
            A[i], A[j] = A[j], A[i]
            i = i + 1
    A[i], A[r] = A[r], A[i]
    return i

class qstest(unittest.TestCase):
    def test_pt(self):
        A = list(range(100))
        random.shuffle(A)
        print(A)
        qsort(A, 0, len(A)-1)
        self.assertSequenceEqual(A, range(100))

if __name__ == '__main__':
    unittest.main()
