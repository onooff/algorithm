n, m = map(int, input().split())
s = set()
ans = 0
for i in range(n):
    s.add(input())
for i in range(m):
    if input() in s:
        ans += 1
print(ans)
