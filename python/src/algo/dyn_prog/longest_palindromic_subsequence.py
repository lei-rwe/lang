import unittest

def pprint(L):
    n = len(L)
    for i in range(n):
        print(L[i])
    print('')

# A Dynamic Programming based Python program for LPS problem
# Returns the length of the longest palindromic subsequence in seq
def lps(str):
    n = len(str)

    # Create a table to store results of subproblems
    L = [[0 for x in range(n)] for x in range(n)]

    # Strings of length 1 are palindrome of length 1
    for i in range(n):
        L[i][i] = 1
    pprint(L)

    for c in range(2, n+1):
        for i in range(n-c+1):
            j = i+c-1
            if str[i] == str[j]:
                L[i][j] = 2 if c == 2 else L[i+1][j-1] + 2
            else:
                a = L[i][j-1]
                b = L[i+1][j]
                L[i][j] = a if a > b else b
        pprint(L)

    return L[0][n-1]

# notice that only two rows are useful, we can reduce the memory usage
# by using dictionary
def lps_opt(str):
    n = len(str)

    # Create a table to store results of subproblems
    L = [[0 for x in range(n)] for x in range(n)]
    D = {}

    # Strings of length 1 are palindrome of length 1
    for i in range(n):
        L[i][i] = 1
        D[(i, i)] = 1
    pprint(L)
    print('D =', D)
    print('')

    for c in range(2, n+1):
        for i in range(n-c+1):
            j = i+c-1
            if str[i] == str[j]:
                L[i][j] = 2 if c == 2 else L[i+1][j-1] + 2
                D[(i,j)] = 2 if c == 2 else 2 if (i+1,j-1) not in D else D[(i+1,j-1)] + 2
            else:
                a = L[i][j-1]
                b = L[i+1][j]
                L[i][j] = a if a > b else b

                a = D[(i, j-1)]
                b = D[(i+1, j)]
                D[(i, j)] = a if a > b else b

        pprint(L)
        print('D =', D)
        print('')

    return D[(0, n-1)]


class TestLPS(unittest.TestCase):
    def test_1(self):
        self.assertEqual(lps_opt("GEEKS FOR GEEKS"), 7)
    def test_2(self):
        self.assertEqual(lps_opt("AABCDEBAZ"), 5)

if __name__ == '__main__':
    unittest.main()
