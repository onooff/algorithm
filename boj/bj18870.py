n = int(input())
l = list(map(int, input().split()))
s = list(set(l))
s.sort()
d = dict()
for i in range(len(s)):
    d.setdefault(s[i], i)
for i in range(len(l)):
    print(d[l[i]], end=' ')
