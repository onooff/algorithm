n, k = map(int, input().split())
s = list(input())

cnt = 0
for i in range(n):
    if s[i] == "P":
        for j in range(i - k, i + k + 1):
            if 0 <= j < n and s[j] == "H":
                cnt += 1
                s[i] = "X"
                s[j] = "X"
                break

print(cnt)
