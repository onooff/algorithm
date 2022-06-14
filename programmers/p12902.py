def solution(n):
    if n % 2 == 1:
        return 0
    mod = 1000000007
    a = 0
    b = 3
    mid = 0
    for i in range(n//2):
        mid = (mid+a*2) % mod
        a, b = b, (b*3+mid+2) % mod
    return a
