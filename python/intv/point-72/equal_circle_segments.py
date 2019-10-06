'''
Given a list of radius and a number N, find the maximum area that
this many N areas can be cut from the list of circles.
For example, R = [1, 1, 1, 2, 2, 3] and N = 6, the cut will be
C = [0, 0, 0, 1, 1, 4]. The maximum area is: pi * 3^2 / 4, which
means to get 4 areas from the 6th, 1/1 from 4th/5th.

This comes to check each solution of x_1 + ... + x_n = m
'''


N = 3
s = [None] * N

def solve_sum(m, S):
    '''
    List all solutions of N positive numbers which sum to S
    :param N: N numbers
    :param S: Sum to S
    :return: The list of all solutions
    '''
    if m <= 1:
        print(S)
        return

    for i in range(S-m+1):
        print(i+1)
        solve_sum(m-1, S-i-1)


if __name__ == "__main__":
    m = N
    solve_sum(m, 5)