n = int(input())
l = list()
for i in range(n):
    l.append(int(input()))

dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if l[j] < l[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# print(l)
# print(dp)
print(n - max(dp))
