'''
Created on Jul 3, 2017

@author: lzhang938
'''

# A Dynamic Programming based Python Program for 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of capacity W
# Note: this algorithm creates an 2d array with the target weight,
# so that each column increase the weight by 1

# define K[i][w] to be the maximum value that can be attained with weight <= w,
# using items up to i (first i items)
#
# Then recursively define K[i][w] as followings:
#   K[0][w] = 0
#   K[i][w] = K[i-1][w]                                 if wt[i] > w
#           = max{K[i-1][w], K[i-1, w-wt[i]] + v[i]}    if wt[i] <= w

from pynotes import array2d

def knapSack(W, wt, val):
    n = len(val)
    K = [[0 for x in range(W+1)] for x in range(n+1)]

    # adjust val and wt to align with the matrix
    val = [0] + val
    wt = [0] + wt

    # Build table K[][] in bottom up manner
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif wt[i] <= w:
                a = val[i] + K[i-1][w-wt[i]]
                b = K[i-1][w]
                if a > b:
                    K[i][w] = a
                    print("1. For weight {}, using {}, value {}".format(w, i, K[i][w]))
                else:
                    K[i][w] = b
                    print("2. For weight {}, using {}, value {}".format(w, i-1, K[i][w]))
                # K[i][w] = max(val[i] + K[i-1][w-wt[i]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
                print("3. For weight {}, using {}, value {}".format(w, i-1, K[i][w]))

    array2d.Array2d.print2d(K)
    return K[n][W]


def main():
    val = [1, 4, 5, 7]
    wt = [1, 3, 4, 5]
    W = 7
    print(knapSack(W, wt, val))
    return

    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    print(knapSack(W, wt, val))

    val = [60, 100, 120]
    wt = [1, 2, 3]
    W = 5
    print(knapSack(W, wt, val))

    val = [10, 40, 30, 50]
    wt = [5, 4, 6, 3]
    W = 10
    print(knapSack(W, wt, val))

if __name__ == '__main__':
    main()
