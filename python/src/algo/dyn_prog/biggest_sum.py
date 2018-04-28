def biggest(a, m):
    max_so_far = a[0];
    curr_max = a[0];
    for i in range(1, m):
        # Recursively add to curr_max, and see if curr_max is bigger than itself
        curr_max = a[i] + max(0, curr_max)  # This also equals to max(a[i] + a[i]+curr_max)
        if (curr_max > max_so_far):
            max_so_far = curr_max;
        print(i, curr_max, max_so_far)

    return max_so_far;

if __name__ == "__main__":
    a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, 4, 7]
    b = biggest(a, len(a))
    print(b)