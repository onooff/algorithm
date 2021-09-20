n, m, k = map(int, input().split())
while k > 0:
    k -= 1
    if n > m*2:
        n -= 1
    else:
        m -= 1
if n >= m*2:
    print(m)
else:
    print(n//2)
