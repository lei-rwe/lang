import random
import unittest

class test(unittest.TestCase):
    def test_media_2(self):
        N = 10
        A = list(range(0, N))
        random.shuffle(A)
        print(A)
        q = partition(A, 0, N-1)
        print(q, A)

def partition(A, p, r):
    pivot = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] < pivot:
            i += 1
            print(pivot, i, j, A[i], A[j], A)
            A[i], A[j] = A[j], A[i]

    print(pivot, i+1, r, A[i+1], A[r], A)
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

if __name__ == '__main__':
    unittest.main()

