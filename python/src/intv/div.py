# A 4-digit number with sqare the same last 4-digit
for x in range(1000, 10000):
    if (x*x - x)%10000 == 0:
        print(x)