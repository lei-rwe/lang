import random
import unittest

class zqs(unittest.TestCase):
    def check_sorted(self, A):
        for i in range(0, len(A)-1):
            if A[i] > A[i+1]:
                return False
        else:
            return True

    def test_partition(self):
        # A = list(range(1,10))
        T = 1
        N = 5000
        for t in range(T):
            # random.shuffle(A)
            A = [random.randint(1, N) for i in range(N)]
            print("\n", A)
            qs(A, 0, len(A)-1)
            print(A)
            assert self.check_sorted(A)

def partition(A, q, r):
    pivot = A[r]
    i = q - 1
    for j in range(q, r):
        if A[j] < pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def qs(A, q, r):
    if q < r:
        p = partition(A, q, r)
        qs(A, q, p-1)
        qs(A, p+1, r)

if __name__ == '__main__':
    unittest.main()
