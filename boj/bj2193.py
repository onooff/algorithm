n = int(input())
a = [0 for _ in range(n + 1)]
a[0] = 1
for i in range(n + 1):
    if i < n:
        a[i + 1] += a[i]
    if (i < n - 1) and i > 0:
        a[i + 2] += a[i]
print(a[n])
