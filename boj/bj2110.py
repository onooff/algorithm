import sys
n, c = map(int, sys.stdin.readline().split())
p = list()
for _ in range(n):
    p.append(int(sys.stdin.readline()))
p.sort()

l = 1
r = p[-1]-p[0]
ans = -1
while l <= r:
    mid = (l+r)//2
    cnt = 1
    last = p[0]
    for i in range(1, len(p)):
        if p[i]-last >= mid:
            cnt += 1
            last = p[i]
    # print(l, mid, r, cnt)
    if cnt >= c:
        ans = mid
        l = mid+1
    else:
        r = mid-1
print(ans)
