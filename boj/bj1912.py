n = int(input())
l = list(map(int, input().split()))

ans = -99999
s = 0
for ll in l:
    s += ll
    ans = max(ans, s)
    if s < 0:
        s = 0

print(ans)
