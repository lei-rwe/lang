def angry_animals(n, hostile_pairs):
    '''
    Divide the animals into cabins without hostile pairs together.
    Animals must be in order, like 12, 23, 123, 4567, cannot be 13, 356 etc
    '''

    count = 0
    for m in range(n):
        print(m)
        for i in range(n-m):
            candidate = list(range(i+1, i+m+2))
            print(candidate)
            good = True
            for u in hostile_pairs:
                if set(u) & set(candidate) == set(u):
                    good = False
                    break
            if good:
                count += 1

    return count


if __name__ == '__main__':
    n = 5
    hostile_pairs = [(1, 2), (3, 4)]
    print(angry_animals(n, hostile_pairs))