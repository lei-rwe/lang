def solution(S):
    exp = list()
    for s in S:
        print(s)
        if s in '0123456789':
            exp.append(s)
        elif s == '+':
            if len(exp) == 0: return -1
            a = exp.pop()

            if len(exp) == 0: return -1
            b = exp.pop()

            exp.append(int(a) + int(b))
        elif s == '*':
            if len(exp) == 0: return -1
            a = exp.pop()
            if len(exp) == 0: return -1

            b = exp.pop()
            exp.append(int(a) * int(b))
        print(exp)

solution('345689++**')
