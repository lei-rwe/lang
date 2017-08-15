# To illustrate comma operator is not like c/C++
# And thus there is no "swap" needed
def fibonacci(n):
    a = 0
    b = 1
    for i in range(1, n):
        a, b = b, a+b
    print(a, b)

if __name__ == '__main__':
    fibonacci(7)