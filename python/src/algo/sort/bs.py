import random

# binary search.
# If found, return its index.
# If not found, return the index the target should be
def bs(A, n):
    # print("Searching", n, "in", A)
    b = 0           # beginning index
    e = len(A) - 1  # ending index
    while b <= e:
        m = (b + e) // 2
        if A[m] > n:
            e = m - 1
        elif A[m] < n:
            b = m + 1
        else:
            return True, m    # Found it

    return False, b

if __name__ == "__main__":
    N = 10
    A = [-1] * N
    for i in range(N):
        A[i] = random.randint(1, N*N)

    for i in range(10):
        print(bs(sorted(A), random.randint(1, N*N)))