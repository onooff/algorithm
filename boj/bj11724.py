import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))
graph = [set() for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split(' '))
    graph[a].add(b)
    graph[b].add(a)

ans = 0
chk = [False for i in range(n+1)]
for i in range(1, n+1):
    if not chk[i]:
        ans += 1
        q = [i]
        chk[i] = True
        while len(q) > 0:
            now = q.pop(0)
            for nxt in graph[now]:
                if not chk[nxt]:
                    q.append(nxt)
                    chk[nxt] = True
print(ans)
