n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

ans = list()
inter = set(a) & set(b)
while len(inter) > 0:
    maxx = max(inter)
    ans.append(str(maxx))
    a = a[a.index(maxx) + 1 :]
    b = b[b.index(maxx) + 1 :]
    inter = set(a) & set(b)
print(len(ans))
print(" ".join(ans))
