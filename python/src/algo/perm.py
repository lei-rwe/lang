def swap(L, i, j):
    t = L[i]
    L[i] = L[j]
    L[j] = t
def reverse(L, f, t):
    while f < t:
        swap(L, f, t)
        f = f + 1
        t = t - 1

def next_permutation(L):
    if len(L)<=1: return False

    i = len(L) - 1
    while (1):
        ii = i
        i  = i - 1
        if (L[i] < L[ii]):
            j = len(L) - 1
            while (not L[i] < L[j]):
                j = j - 1
            # print i, ii, j
            swap(L, i, j)
            reverse(L, ii, len(L)-1)
            return True

        if (i == 0):
            print("This is the last one: ")
            print(L)
            reverse(L, 0, len(L) -1)
            return False


def test_1():
    s = [5, 1, 3, 4, 2]
    print(s)
    next_permutation(s)
    print(s)

def test_2():
    S = [1, 3, 3, 4]
    print(S)
    while next_permutation(S):
        print(S)

if __name__ == "__main__":
    test_2()
