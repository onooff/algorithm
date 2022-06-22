d, p = map(int, input().split())
lim = 10**d
q = [1]
nq = set()
for i in range(p):
    for cur in q:
        for i in range(2, 10):
            tmp = cur*i
            if tmp < lim:
                nq.add(tmp)
    q = list(nq)
    nq = set()
if len(q) > 0:
    print(max(q))
else:
    print(-1)
