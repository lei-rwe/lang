from itertools import combinations
'''
Finding the number of distinct non-negative integer-valued vectors (x1, x2, . . . , xn)
such that x1 + x2 + · · · + xn = s
By combination theory, there are C(s-1, n-1) such distinct solutions.
For example:
    x1 + x2 + x3 = 5
has C(5-1, 3-1)=C(4, 2)=6 solutions, which are
    [[1, 1, 3], [1, 2, 2], [1, 3, 1], [2, 1, 2], [2, 2, 1], [3, 1, 1]]

This program is to find all the solutions
'''


def sum_from_combinations(n, s):
    '''
    Find all the n-numbers which add to sum s
    Each combination gives a solution of the corresponding equation.
    For example:
        [1,2] in comb(2, 4) gives a solution to x_1 + x_2 + x_3 = 5 as [1, 1, 3]
    This function is to build such correspondence. Namely, given a combination,
    construct the solution for the equation
    :param n: this many numbers
    :param s: add to the sum 's'
    :return: All the solutions
    '''
    # A = list(combinations(range(1, s), n-1))
    # print(A)
    Y = [[0] + list(x) + [s] for x in combinations(range(1, s), n-1)]
    V = [[y[i + 1] - y[i] for i in range(len(y) - 1)] for y in Y]
    print(f'There are {len(V)} solutions to add {n} numbers to sum {s}, which are:\n{V}')


if __name__ == "__main__":
    sum_from_combinations(2, 6)
