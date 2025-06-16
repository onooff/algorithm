s = input()
d = [1, 3]
i = 0
ans = 0
summ = 0
for c in s:
    if c == "*":
        ans += d[i]
    else:
        summ += int(c) * d[i]
    i = (i + 1) % 2

for i in range(10):
    if (ans * i + summ) % 10 == 0:
        print(i)
        break
