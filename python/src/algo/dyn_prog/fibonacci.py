'''
Created on Jul 3, 2017

@author: lzhang938
'''

import time

def fib_r(n):
    if n < 0: raise "Input cannot be negative for Fibonacci"
    if n == 0: return 0
    if n == 1: return 1
    return fib_r(n-1) + fib_r(n-2)

M = {0: 0, 1: 1}
def fib_r_m(n):
    if n < 0: raise "Input cannot be negative for Fibonacci"
    if M.__contains__(n):
        return M[n]

    M[n] = fib_r_m(n-1) + fib_r_m(n-2)
    return M[n]

def fib_bottom_up(n):
    a = 0
    b = 1
    for i in range(n):
        c = a + b
        a = b
        b = c
    return a
    
if __name__ == '__main__':
    # b = time.time()
    # print(fib_r(30))    # will take 66' to calculate fib(40)
    # print("Recursive method takes", time.time() - b)

    b = time.time()
    print(fib_r_m(60))
    print("Memorized recursive method takes", time.time() - b)
    print(M)

    b = time.time()
    print(fib_bottom_up(60))
    print("Memorized recursive method takes", time.time() - b)