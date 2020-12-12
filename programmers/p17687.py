def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]


def solution(n, t, m, p):
    answer = ''
    tmp = ''
    num = 0
    p -= 1
    while len(answer) < t:
        while (len(answer)*m)+p > len(tmp)-1:
            tmp += convert(num, n)
            num += 1
        answer += tmp[(len(answer)*m)+p]
    print(tmp)
    return answer
