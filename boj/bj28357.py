import math

n, k = map(int, input().split())
l = sorted(list(map(int, input().split())))
l.insert(0, 0)
n += 1

summ = 0
for i in range(n - 1, -1, -1):
    if summ >= k:
        break
    summ += (l[i] - l[i - 1]) * (n - i)

if (n - i - 1) == 0:
    print(l[-1])
elif summ <= k:
    print(max(0, l[i] - math.ceil((k - summ) / (n - i - 1))))
else:
    print(l[i] + math.ceil((summ - k) / (n - i - 1)))
