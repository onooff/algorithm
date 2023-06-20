n, m, k = map(int, input().split())
ans = False
stk = list()


def dfs(n, m, stk):
    global ans, k
    if n == 0:
        if m == 0:
            k -= 1
            if k == 0:
                ans = True
        return
    base = stk[-1] if len(stk) > 0 else m//n
    for i in range(base, m+1):
        stk.append(i)
        dfs(n-1, m-i, stk)
        if ans:
            return
        stk.pop()
    return


dfs(n, m, stk)
print(*stk, sep=' ')
