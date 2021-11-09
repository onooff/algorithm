n = int(input())
l = map(int, input().split())
target = int(input())

d = dict()
for num in l:
    d.setdefault(num, 0)
    d[num] += 1

ans = 0
lim = target//2
for i in range(1, lim+1):
    j = target-i
    if i in d and j in d:
        if i == j:
            ans += d[i]//2
        else:
            ans += min(d[i], d[j])

print(ans)
