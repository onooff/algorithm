n = int(input())
l = list(map(int, input().split()))
ans = [str(x) for x in range(1, n + 1)]
for i in range(n - 1, -1, -1):
    ii = i
    for j in range(l[i]):
        ans[ii], ans[ii + 1] = ans[ii + 1], ans[ii]
        ii += 1
print(" ".join(ans))
