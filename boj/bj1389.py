'''
5 5
1 3
1 4
4 5
4 3
3 2
'''

n, m = map(int, input().split())
graph = [set() for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)

ans = -1
min_kb = 999999999999999
for i in range(1, n+1):
    chk = [False for i in range(n+1)]
    q = [i]
    chk[i] = True
    kb = 0
    kb_d = 1
    to_next_level = 1
    cnt = 0
    idx = 0
    while idx < len(q):
        now = q[idx]
        to_next_level -= 1
        kb += kb_d
        for friend in graph[now]:
            if not chk[friend]:
                chk[friend] = True
                q.append(friend)
                cnt += 1
        if to_next_level == 0:
            to_next_level = cnt
            cnt = 0
            kb_d += 1
        idx += 1
    if min_kb > kb:
        min_kb = kb
        ans = i
print(ans)
