def solution(n):
    answer = 0

    s = str(n)
    for c in s:
        answer += int(c)

    return answer
