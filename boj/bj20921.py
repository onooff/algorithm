n, m = map(int, input().split())
ans = [0 for _ in range(n)]
maxx = n
minn = 1
for i in range(n):
    if m >= n-(i+1):
        m -= n-(i+1)
        ans[i] = maxx
        maxx -= 1
    else:
        ans[i] = minn
        minn += 1
for a in ans:
    print(a, end=' ')
