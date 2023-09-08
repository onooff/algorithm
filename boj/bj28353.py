n, k = map(int, input().split())
li = sorted(list(map(int, input().split())))

l = 0
r = len(li) - 1
ans = 0
while l < r:
    if li[l] + li[r] <= k:
        ans += 1
        l += 1
    r -= 1
print(ans)
