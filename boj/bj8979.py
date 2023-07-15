n, k = map(int, input().split())
d = dict()
for _ in range(n):
    num, gold, silver, bronze = map(int, input().split())
    t = (gold, silver, bronze)
    d.setdefault(t, set())
    d[t].add(num)

l = sorted(list(d.keys()), key=lambda x: (-x[0], -x[1], -x[2]))

rank = 1
for t in l:
    if k in d[t]:
        print(rank)
        break
    rank += len(d[t])
