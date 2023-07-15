h, w, n, m = map(int, input().split())
a, b = 0, 0
for i in range(0, h, n + 1):
    a += 1
for i in range(0, w, m + 1):
    b += 1
print(a * b)
