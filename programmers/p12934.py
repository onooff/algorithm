from math import sqrt


def solution(n):
    n = sqrt(n)
    if n % 1 == 0:
        return (n+1)*(n+1)
    else:
        return -1
