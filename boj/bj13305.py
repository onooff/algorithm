n = int(input())
d = list(map(int, input().split()))
p = list(map(int, input().split()))

minn = p[0]
ans = 0

for i in range(len(p) - 1):
    minn = min(minn, p[i])
    ans += minn * d[i]

print(ans)
