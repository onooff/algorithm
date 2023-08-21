import sys

inputs = sys.stdin.readlines()

d = dict()
for i in range(2, len(inputs) - 1):
    cur = list(inputs[i].rstrip().split())
    ii = i - 1
    d.setdefault(ii, set())
    for j in range(len(cur)):
        if cur[j] == "1":
            jj = j + 1
            d[ii].add(jj)

course = list(map(int, inputs[-1].rstrip().split()))
s = set(course)
s.discard(course[0])
q = [course[0]]
visit = set(q)

while q:
    cur = q.pop(0)
    for nxt in d[cur]:
        if nxt not in visit:
            visit.add(nxt)
            q.append(nxt)
            s.discard(nxt)

if s:
    print("NO")
else:
    print("YES")
