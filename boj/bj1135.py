n = int(input())
tree = {i: list() for i in range(n)}
info = list(map(int, input().split()))

for i in range(1, n):
    tree[info[i]].append(i)


t = [len(tree[i]) for i in range(n)]


def dfs(cur):
    if len(tree[cur]) == 0:
        return

    for child in tree[cur]:
        dfs(child)

    tree[cur].sort(key=lambda x: -t[x])
    for i in range(len(tree[cur])):
        t[cur] = max(t[cur], i+t[tree[cur][i]]+1)


dfs(0)
print(t[0])
