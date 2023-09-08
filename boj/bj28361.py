n = int(input())
ans = []
print(n)

cur = 1
d = [2, -1, 2]
i = 0
if n % 3 == 2:
    ans.append("1")
    cur += 1

while cur <= n:
    ans.append(str(cur))
    cur += d[i]
    i = (i + 1) % 3
ans.append("1")
print(" ".join(ans))
