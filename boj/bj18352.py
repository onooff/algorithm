'''
4 4 2 1
1 2
1 3
2 3
2 4
'''
import sys
inputs = sys.stdin.readlines()

n, m, k, x = map(int, inputs[0].rstrip().split())
graph = dict()
chk = list()

for i in range(0, n+1):
    graph.setdefault(i, list())
    chk.append(False)

for i in range(1, m+1):
    a, b = map(int, inputs[i].rstrip().split())
    graph[a].append(b)

q = [x]
chk[x] = True
q_idx = 0
nxt_level = 0
cur_level = 1
lv = 0
while q_idx < len(q):
    cur = q[q_idx]
    q_idx += 1
    cur_level -= 1

    for nxt in graph[cur]:
        if not chk[nxt]:
            chk[nxt] = True
            q.append(nxt)
            nxt_level += 1

    if cur_level == 0:
        cur_level = nxt_level
        nxt_level = 0
        lv += 1
        if lv == k:
            break

ans = q[q_idx:]
if len(ans) <= 0:
    print(-1)
else:
    ans.sort()
    for a in ans:
        print(a)
