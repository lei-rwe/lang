def biggest(A):
    m = len(A)
    if m == 0:
        return
    max_so_far = max_ending_here = A[0]

    for i in range(1, m):
        # Use max_so_far to memorize the maximum value for max_ending_here
        max_ending_here = A[i] + max(0, max_ending_here)  # This also equals to max(a[i] + a[i]+curr_max)
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here;
        print(i, max_ending_here, max_so_far)

    return max_so_far;


if __name__ == "__main__":
    a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, 4, 7]
    a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    b = biggest(a)
    print(b)