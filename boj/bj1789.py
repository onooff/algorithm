n = int(input())
d = 1
nd = n-d
while d < nd:
    n -= d
    d += 1
    nd = n-d
print(d)
