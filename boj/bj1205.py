n, a, p = map(int, input().split())
l = list()
if n != 0:
    l = list(map(int, input().split()))
l.append(a)
l.sort(key=lambda x: -x)

for i in range(n):
    if l[i] == a and (i + 1 >= len(l) or l[i + 1] != a):
        l = l[: i + 1]
        break

ans = -1
if len(l) <= p:
    rank = 1
    cnt = 1
    for i in range(1, len(l)):
        if l[i] != l[i - 1]:
            rank += cnt
            cnt = 0
        if l[i] == a:
            break
        cnt += 1
    ans = rank
print(ans)
