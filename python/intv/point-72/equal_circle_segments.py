from itertools import combinations
'''
Given a list of radius and a number N, find the maximum area that
this many N areas can be cut from the list of circles.
For example, R = [1, 1, 1, 2, 2, 3] and N = 6, the cut will be
C = [0, 0, 0, 1, 1, 4]. The maximum area is: pi * 3^2 / 4, which
means to get 4 areas from the 6th, 1/1 from 4th/5th.

This comes to check each solution of x_1 + ... + x_n = m
'''


def solve_sum(N, S):
    '''
    List all solutions of N positive numbers which sum to S
    :param N: N numbers
    :param S: Sum to S
    :return: The list of all solutions
    '''
    if N <= 1:
        return [[S]]

    T = []
    for i in range(S-N+1):
        A = solve_sum(N-1, S-i-1)
        T.extend([[i+1]+a for a in A])

    return T


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
    print(Y)
    for y in Y:
        v = [y[i+1] - y[i] for i in range(len(y)-1)]
        print(v)


if __name__ == "__main__":
    A = solve_sum(3, 5)
    print(A)

    B = list(combinations('1234', 2))

    # Note A and B are 1-1 corresponding, in the following way:
    # Imagine that we list 5 objects in a line, and mark the spaces
    # between them 1, 2, 3, 4. Then each solution of the combinations
    # will divide the objects into three parts. For example, [1,2]
    # divides the 5 objects to [1, 1, 3]

    sum_from_combinations(3, 5)
