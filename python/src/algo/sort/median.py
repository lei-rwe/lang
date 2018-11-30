import random
import unittest

class ZMedian(unittest.TestCase):
    def check_sorted(self, A):
        for i in range(0, len(A)-1):
            if A[i] > A[i+1]:
                return False
        else:
            return True
    def _test_qs(self):
        N = 100
        A = [random.randint(0, N) for i in range(0, N)]
        print(A)
        qsort(A, 0, len(A)-1)
        print(A)
        assert self.check_sorted(A)

    def _test_media(self):
        N = 7
        # A = [random.randint(0, N) for i in range(0, N)]
        # A = list(range(0, N))
        # random.shuffle(A)
        A = [0, 5, 3, 6, 1, 4, 2]
        print(A)
        median(A, 0, len(A)-1, N // 2)
        print(A[N//2])
    def test_media_2(self):
        N = 15
        m = 5
        A = [random.randint(0, N) for i in range(0, N)]
        # A = list(range(0, N))
        # random.shuffle(A)
        print(A)
        median(A, 0, len(A)-1, m)
        print(A)
        print(A[m])

def partition(A, p, r):
    pivot = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] < pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def qsort(A, p, r):
    if p<r:
        q = partition(A, p, r)
        qsort(A, p, q - 1)
        qsort(A, q + 1, r)

def median(A, p, r, m):
    if  p<r:
        q = partition(A, p, r)
        if q == m:
            return
        elif q > (p+r) // 2:
            median(A, p, q-1, m)
        else:
            median(A, q+1, r, m)

if __name__ == '__main__':
    unittest.main()

