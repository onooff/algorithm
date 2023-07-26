n, m = map(int, input().split())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))


def dfs(i, j, last_d, summ, lim):
    if i + 1 >= n:
        return summ

    for nxt_d in range(-1, 2):
        if nxt_d == last_d:
            continue
        if 0 <= j + nxt_d < m and summ + l[i + 1][j + nxt_d] <= lim:
            lim = dfs(i + 1, j + nxt_d, nxt_d, summ + l[i + 1][j + nxt_d], lim)

    return lim


minn = float("inf")
for i in range(m):
    minn = dfs(0, i, 9, l[0][i], minn)
print(minn)
