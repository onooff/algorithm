n = int(input())
graph = list()
for i in range(n):
    graph.append(list(map(int, input().split())))
chk = [False for i in range(n)]
ans = 999999999


def dfs(sum, now, chked, start):
    global n, graph, chk, ans
    if chked == n:
        if graph[now][start] != 0:
            ans = min(ans, sum+graph[now][start])
        return
    for i in range(n):
        if not chk[i] and graph[now][i] != 0:
            chk[i] = True
            dfs(sum+graph[now][i], i, chked+1, start)
            chk[i] = False


for i in range(n):
    chk[i] = True
    dfs(0, i, 1, i)
    chk[i] = False

print(ans)
