def solution(n, m, section):
    answer = 0
    cur = 0
    while cur < len(section):
        answer += 1
        lim = section[cur] + m - 1
        while cur < len(section) and section[cur] <= lim:
            cur += 1
    return answer
