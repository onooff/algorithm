t = int(input())
for _ in range(t):
    n = int(input())
    l = list()
    for _ in range(n):
        p = input().split()
        p[0] = int(p[0])
        l.append(p)
    l.sort(key=lambda x: -x[0])
    print(l[0][1])
