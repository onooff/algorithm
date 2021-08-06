'''
7
1 6
6 3
3 5
4 1
2 4
4 7
'''

import sys
input = sys.stdin.readline
n = int(input())
graph = [set() for i in range(n+1)]
ans = [-1 for i in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split(' '))
    graph[a].add(b)
    graph[b].add(a)

q = [1]
ans[1] = 0
idx = 0
while idx < len(q):
    mom = q[idx]
    for baby in graph[mom]:
        if ans[baby] == -1:
            ans[baby] = mom
            q.append(baby)
    idx += 1
for i in range(2, n+1):
    print(ans[i])
