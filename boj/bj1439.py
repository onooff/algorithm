s = input()
ans = [0, 0]
last = -1
for n in s:
    n = int(n)
    if n != last:
        ans[n] += 1
        last = n
print(min(ans))
