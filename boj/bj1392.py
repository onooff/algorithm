n, m = map(int, input().split())
l = [0]
for _ in range(n):
    l.append(int(input()))
t = list()
for i in range(1, n+1):
    for _ in range(l[i]):
        t.append(i)
for _ in range(m):
    print(t[int(input())])
