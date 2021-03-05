t = int(input())

for tc in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    d = dict()
    for i in range(n):
        d.setdefault(a[i], i)
    ans = [0 for i in range(n)]

    def go(start=0, end=n, depth=0):
        global n, a, ans, d
        try:
            max_val = max(a[start:end])
            ans[d[max_val]] = depth
            go(start, d[max_val], depth+1)
            go(d[max_val]+1, end, depth+1)
            return
        except:
            return
    go(0, n, 0)
    for answer in ans:
        print(answer, end=' ')
    print()
