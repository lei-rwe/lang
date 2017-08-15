# Loop statements may have an else clause; it is executed when the loop
# terminates through exhaustion of the list (with for) or when the condition
# becomes false (with while), but not when the loop is terminated by a break
# statement. This is exemplified by the following loop, which searches for]
# prime numbers
import math
def prime_generator(n):
    for n in range(2, n):
        for x in range(2, int(math.sqrt(n))+1):
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                break
        else:
            # loop fell through without finding a factor
            yield n

for x in prime_generator(30):
    print(x)
