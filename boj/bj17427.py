lim = int(input())

ans = 0
for i in range(1, lim+1):
    ans += i*(lim//i)

print(ans)
