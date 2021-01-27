n = int(input())
l = list(map(int, input().split()))
chk = [False for i in range(n)]
ans = 0


def dfs(sum, chked, last):
    global n, l, chk, ans
    if chked == n:
        ans = max(sum, ans)
        return
    for i in range(n):
        if not chk[i]:
            if chked == 0:
                chk[i] = True
                dfs(sum, chked+1, l[i])
                chk[i] = False
            else:
                chk[i] = True
                dfs(sum+abs(last-l[i]), chked+1, l[i])
                chk[i] = False


dfs(0, 0, -1)
print(ans)
