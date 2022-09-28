def solution(n, s):
    d = s//n
    if d == 0:
        return [-1]
    else:
        answer = [d for _ in range(n)]
        r = s % n
        for i in range(r):
            answer[-(i+1)] += 1
        return answer
