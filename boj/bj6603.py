while True:
    l = list(map(int, input().split()))
    if l[0] == 0:
        break

    n = l.pop(0)
    chk = [False for i in range(n)]

    def dfs(last, cnt):
        global n, l
        if cnt == 6:
            for i in range(n):
                if chk[i]:
                    print(l[i], end=' ')
            print()
            return
        if n-last < 6-cnt:
            return

        for i in range(last+1, n):
            if not chk[i]:
                chk[i] = True
                dfs(i, cnt+1)
                chk[i] = False
    dfs(-1, 0)
    print()
