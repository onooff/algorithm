def solution(n, k):
    answer = []
    l = [i for i in range(1, n+1)]
    d = 1
    for i in range(1, n+1):
        d *= i
    dd = n
    while len(l) > 0:
        idx = 0
        d //= dd
        dd -= 1
        while k > d:
            idx += 1
            k -= d
        answer.append(l.pop(idx))
    return answer
