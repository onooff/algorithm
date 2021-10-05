n, m = map(int, input().split())
l = list(map(int, input().split()))

ans = set()
for num in l:
    tmp = num
    while tmp <= n:
        ans.add(tmp)
        tmp += num

print(sum(ans))
