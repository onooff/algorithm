n, k = map(int, input().split())

t = 0
q = [k]
nq = []
while k > 0 and k % 2 == 0:
    k //= 2
    q.append(k)
visit = set(q)

while len(q) > 0:
    cur = q.pop()
    if cur == n:
        break
    for d in (1, -1):
        nxt = cur + d
        while True:
            if nxt not in visit:
                nq.append(nxt)
                visit.add(nxt)
            else:
                break

            if nxt % 2 != 0:
                break
            nxt //= 2

    if len(q) == 0:
        q = nq
        nq = []
        t += 1

print(t)
