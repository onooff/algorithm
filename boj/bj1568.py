n = int(input())
ans = 0
cnt = 1
while n > 0:
    ans += 1
    if n < cnt:
        cnt = 1
    n -= cnt
    cnt += 1
print(ans)
