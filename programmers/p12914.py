def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    n1 = 1
    n2 = 2
    now = 0
    for i in range(n-2):
        now = n1+n2
        n1 = n2
        n2 = now
    return now % 1234567
