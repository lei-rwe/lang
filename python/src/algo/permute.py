def next_perm(s):
    if len(s)==1:
        return list(s[0])
    a = s[0]
    T = []
    for p in perm(s[1:]):
        for i in range(len(p)):
            T.append(p[:i] + a + p[i:])
        T.append(p + a)
    return T

if __name__ == "__main__":
    print(next_perm("1234"))