'''
Created on Jul 3, 2017

@author: lzhang938
'''
import sys
from pynotes.array2d import Array2d

# Given an ordered list of matrix dimensions,
# find the product order which leads to the least
# number of multiplication operations

# Notice that A[m*n] * B[n*p] will have m*n*p multiplications

# We use a 1-dimension array to denote the matrix dimensions,
# and suppose matrix A[i] has dimension D[i-1] x D[i] for i = 1..n

# The complexity is O(n^3)

def MatrixChainOrder(D):
    # length[D] = n + 1
    n = len(D) - 1       # How many matrices?
    m = Array2d.create(n+1, n+1)
    s = Array2d.create(n+1, n+1)

    # m[i,j] = Minimum number of scalar multiplications (i.e., cost)
    # needed to compute the matrix A[i]A[i+1]...A[j] = A[i..j]
    # The cost is zero when multiplying one matrix
    for i in range(n+1):
        m[i][i] = 0

    for length in range(2, n+1):   # Subsequence lengths
        for i in range(1, n - length + 1 + 1):
            j = i + length - 1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                cost = m[i][k] + m[k+1][j] + D[i-1]*D[k]*D[j]
                if cost < m[i][j]:
                    m[i][j] = cost

                    #Index of the subsequence split that achieved minimal cost
                    s[i][j] = k

    Array2d.print2d(m)
    print("")
    Array2d.print2d(s)

if __name__ == "__main__":
    A = [(2,3), (3, 6), (6, 4), (4, 5)]
    B = [2, 3, 6, 4, 5]
    MatrixChainOrder(B)