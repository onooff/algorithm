a, b, c = map(int, input().split())
d = dict()
for i in range(1, a+1):
    for j in range(1, b+1):
        for k in range(1, c+1):
            summ = i+j+k
            d.setdefault(summ, 0)
            d[summ] += 1
maxx = -1
ans = -1
for k in d:
    if d[k] > maxx:
        maxx = d[k]
        ans = k
    elif d[k] == maxx and ans > k:
        ans = k
print(ans)
