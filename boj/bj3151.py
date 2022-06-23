n = int(input())
l = list(map(int, input().split()))
d = dict()
for i in range(n):
    d.setdefault(l[i], set())
    d[l[i]].add(i)
ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        k = -(l[i]+l[j])
        dup = 0
        if k not in d:
            continue
        else:
            if i in d[k]:
                dup += 1
            if j in d[k]:
                dup += 1
            ans += len(d[k])-dup
print(ans//3)
