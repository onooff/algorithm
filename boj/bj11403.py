'''
3
0 1 0
0 0 1
1 0 0
'''
import sys
input = sys.stdin.readline

n = int(input())
graph = list()
ans = list()

for i in range(n):
    tmp = list(map(int, input().split(' ')))
    ans.append([0 for i in range(n)])
    tmp_set = set()
    for j in range(n):
        if tmp[j] == 1:
            tmp_set.add(j)
    graph.append(tmp_set)

for i in range(n):
    chk = [False for j in range(n)]
    q = [i]
    while len(q) > 0:
        tmp = q.pop(0)
        for nxt in graph[tmp]:
            if not chk[nxt]:
                ans[i][nxt] = 1
                q.append(nxt)
                chk[nxt] = True


for i in range(n):
    for j in range(n):
        print(ans[i][j], end=' ')
    print()
