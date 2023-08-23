n, a, b = map(int, input().split())

aa = [i for i in range(1, a + 1)]
bb = [i for i in range(b, 0, -1)]
ans = None
if a > b:
    ans = aa + bb[1:]
else:
    ans = aa[:-1] + bb

if len(ans) > n:
    print(-1)
else:
    if a == 1:
        ans = ans[0:1] + [1 for _ in range(n - len(ans))] + ans[1:]
    else:
        ans = [1 for _ in range(n - len(ans))] + ans
    print(*ans)
