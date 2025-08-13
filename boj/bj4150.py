D = 1
i = int(input())


def mul_maxrix(a, b, d=1):
    if len(a[0]) != len(b):
        return None
    l = len(a[0])
    y = len(a)
    x = len(b[0])
    ret = [[0 for _ in range(x)] for _ in range(y)]
    for i in range(y):
        for j in range(x):
            for k in range(l):
                ret[i][j] += a[i][k] * b[k][j]
            if d > 1:
                ret[i][j] %= d
    return ret


memo = {1: [[1, 1], [1, 0]]}
cur = 1
while cur + cur <= i:
    nxt = cur + cur
    memo[nxt] = mul_maxrix(memo[cur], memo[cur], D)
    cur = nxt

k = list(memo.keys())
k.sort(key=lambda x: -x)

if i == 0:
    print(0)
else:
    cur = 0
    mat = [
        [memo[k[cur]][0][0], memo[k[cur]][0][1]],
        [memo[k[cur]][1][0], memo[k[cur]][1][1]],
    ]
    i -= k[cur]
    while i > 0:
        while k[cur] > i:
            cur += 1
        mat = mul_maxrix(mat, memo[k[cur]], D)
        i -= k[cur]
    print(mat[0][1])
