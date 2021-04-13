def solution(n, a, b):
    answer = 0

    while a != b:
        answer += 1
        if a % 2 == 1:
            a += 1
        if b % 2 == 1:
            b += 1
        a //= 2
        b //= 2

    return answer
