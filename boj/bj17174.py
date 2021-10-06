n, m = map(int, input().split())
ans = n
while n//m > 0:
    ans += n//m
    n = n//m
print(ans)
