def insert_sort(L):
    for i in range(1, len(L)):
        key = L[i]
        # Traverse backwards, to shift elements to right
        for j in range(i-1, -1, -1):
            if L[j] > key:
                L[j+1] = L[j]
            else:
                j += 1
                break
        L[j] = key

if __name__ == "__main__":
    L = [3, 8, 4, 6, 10, 9]
    print(L)
    insert_sort(L)
    print(L)
