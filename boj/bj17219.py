n, m = map(int, input().split())

d = dict()
for i in range(n):
    url, pw = input().split()
    d.setdefault(url, pw)
for i in range(m):
    print(d[input()])
