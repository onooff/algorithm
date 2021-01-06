n = int(input())
l = list(input().split())

chk = l[0][0]
is_ok = 1
for i in range(1, len(l)):
    if l[i][0] != chk:
        is_ok = 0
        break
print(is_ok)
