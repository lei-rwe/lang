def print_triangle(N):
    for i in range(N):
        fmt = "{:^" + str(2 * N) + "}"
        print(fmt.format('#' * 2 * (i + 1)))

if __name__ == "__main__":
    print_triangle(10)