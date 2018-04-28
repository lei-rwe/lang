# Prefixes:
#    Prefixes are denoted with the name of the sequence,
#    followed by a subscript to indicate how many characters
#    the prefix contains.
#    For example: S="abcdef", the prefix S3="abc"

# To find the LCS of two strings is based on the following property:
# Given X[1...n], Y[1...m]
#    If X[n] == Y[m] = x, LCS(X, Y) = LCS(X[1...n-1], Y[1...m-1]) + x
#    Otherwise, LCS(X, Y) = longest{LCS(X, Y[1...m-1]), LCS(X[1...n-1], Y)}

# Using recursive, its complexity is 2^m (if m==n)
def lcs_recursive(s1, s2):
    if len(s1)==0 or len(s2)==0:
        return 0
    if s1[-1] == s2[-1]:
        return lcs_recursive(s1[:len(s1)-1], s2[:len(s2)-1]) + 1
    return max(lcs_recursive(s1[:len(s1)-1], s2), lcs_recursive(s1, s2[:len(s2)-1]))

# Comparing the last character, or comparing the first character, is the same
def lcs_first(s1, s2):
    if len(s1)==0 or len(s2)==0:
        return 0
    if s1[0] == s2[0]:
        return 1+lcs_first(s1[1:], s2[1:])
    return max(lcs_first(s1[1:], s2), lcs_first(s1, s2[1:]))

# Using recursive, the complexity is 2^m, but there are just (m+1)(n+1) subproblems.
# Hence some of the subproblems must be solved over and over again.
# Instead, we can memorize the middle results to avoid the duplicated solvings.
# To do this, we use a dictionary of tuple to the length
M = {}
def lcs_recursive_m(s1, s2):
    if len(s1)==0 or len(s2)==0:
        return 0
    if M.__contains__( (s1, s2) ):
        return M[ (s1, s2) ]
    if s1[-1] == s2[-1]:
        l = lcs_recursive_m(s1[:len(s1)-1], s2[:len(s2)-1]) + 1
    else:
        l = max(lcs_recursive_m(s1[:len(s1)-1], s2), lcs_recursive_m(s1, s2[:len(s2)-1]))

    key = (s1, s2)
    M[key] = l
    return l

def print2d(A):
    l = len(A)
    for i in range(l):
        print(A[i])
# The bottom up dynamic programming method will fill in a matrix for the given two
# strings by computing the LCS of all the "increasing" pairs. Using the property
# stated at the beginning, we do not need to compute a new pair from beginning,
# but we can use the values we already computed.
def bottom_up_matrix(s1, s2):
    l1 = len(s1) + 1
    l2 = len(s2) + 1
    # A = [[0] * l1] * l2
    A = [[0 for x in range(l1)] for y in range(l2)]
    print2d(A)
    for i in range(1, l2):
        for j in range(1, l1):
            c1 = s1[j-1]
            c2 = s2[i-1]
            if c1 == c2:
                A[i][j] = A[i-1][j-1] + 1
            else:
                A[i][j] = max(A[i-1][j], A[i][j-1])
    print2d(A)

if __name__ == "__main__":
    s1 = "abcdef"
    s2 = "acbcf"
    print(lcs_recursive(s1, s2))
    print(lcs_recursive("AGCAT", "GAC"))

    print(lcs_first(s1, s2))
    print(lcs_first("AGCAT", "GAC"))

    print(lcs_recursive_m(s1, s2))
    print(lcs_recursive_m("AGCAT", "GAC"))
    print(M)

    bottom_up_matrix(s1, s2)