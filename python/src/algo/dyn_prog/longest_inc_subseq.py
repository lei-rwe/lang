import bs

def longest_inc_subsequence(mylist):
    # Create a lis array to hold the number of elements
    # for the longest increasing subsequence ending here
    # The complexity is O(n^2)
    # For each index i, compare its value with the elements
    # before it. If running into a smaller one, adjust its
    # length
    L = len(mylist)
    lis = [1] * L       # The length is at least one
    print(lis)

    for i in range(L):
        print("Checking index", i, "with value", mylist[i])
        for j in range(i):
            if mylist[i] > mylist[j]:
                lis[i] = max(lis[i], lis[j]+1)

    print(lis)

def trace_lis(mylist):
    # Create an array to back-track the longest increasing subsequence
    L = len(mylist)
    lis = [1] * L
    trace = [-1] * L

    for i in range(L):
        print("Checking index", i, "with value", mylist[i])
        for j in range(i):
            if mylist[i] > mylist[j]:
                # lis[i] = max(lis[i], lis[j]+1)
                if lis[i] < lis[j] + 1:                    
                    lis[i] = lis[j] + 1
                    trace[i] = j

    print(mylist)
    print(lis)
    print(trace)
    # Using trace, to re-construct the longest path
    idx = trace.index( max(trace) )
    print("The maximum value is at index:", idx)
    while idx >= 0:
        print(mylist[idx])
        idx = trace[idx]

def explain_LIS_ending_numbers(A, M, L):
    for i in range(L):
        print("LIS with length", i + 1, "has smallest number at index", M[i], "with value", A[M[i]])

def lis_fast(A):
    # Example: [3, 4, -1, 5, 8, 2, 3, 12, 7, 9, 10]
    # Note: here both P and M are list of indices
    N = len(A)

    # P[k]: index of the predecessor of X[k] in the LIS ending at X[k]
    P = [-1] * N

    # M[k]: for LISes with length (k+1), this is the index of the smallest
    # ending number for all the LISes.
    # For example: given A=[3, 4, -1]. When we check index 1, it has two
    # LISes with length 1: [3] and [4]. The smallest one is [3] with index 0.
    # Hence M[0] = 0 when we check index 1
    # But when we check index 2, we bring in -1. M[0] will become 2 
    M = [0] * N

    # the length of the LIS so far
    L = 0
    M[0] = 0    # index of LIS with length 1

    for i in range(1, N):
        # print("Checking index", i)
        # print("A=", A[0:i])
        # print("L=", L)
        # print("P=", P[0:i])
        # print("M=", M[0:L+1])
        # explain_LIS_ending_numbers(A, M, L)

        if A[i] < A[M[0]]:
            # Get a smallest number. eg: -1 in the example
            M[0] = i
            continue
        if A[i] > A[M[L]]:
            # Get a largest number. eg: 5, 8 in the example
            P[i] = M[L]     # Precedent comes from the index M[L]
            L = L + 1       # LIS length increased by one
            M[L] = i
            continue

        # Now A[i] falls between the scanned values
        # Build the list with length (L+1) which are the smallest numbers
        # for the LISes with length 1 to L+1
        ending_numbers = [0] * (L+1)
        for t in range(L+1):
            ending_numbers[t] = A[M[t]]
        # print("LIS Ending numbers: ", ending_numbers)

        search = bs.bs(ending_numbers, A[i])
        idx = search[1]
        M[idx] = i      # The smallest number is at index "i"
        P[i] = M[idx-1] # It comes from previous index

    # Reconstruct the longest increasing subsequence
    S = [-1] * (L + 1)
    k = M[L]
    for i in reversed(range(L+1)):
        S[i] = A[k]
        k = P[k]

    return S

if __name__ == "__main__":
    X = [3, 4, -1, 5, 8, 2, 3, 12, 7, 9, 10]
    print(lis_fast(X))

    X = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    print(lis_fast(X))

