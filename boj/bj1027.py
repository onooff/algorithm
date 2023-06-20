n = int(input())
l = list(map(int, input().split()))
ans = 0

for x in range(n):
    y = l[x]
    cnt = 0

    # print(">>>", x, y)
    for d in [1, -1]:
        nx = x+d
        maxx = None
        while 0 <= nx < n:
            ny = l[nx]
            cur = (ny-y)/abs(nx-x)
            # print(cur, maxx)
            if maxx == None or maxx < cur:
                cnt += 1
                maxx = cur
            nx += d
    # print("cnt = ", cnt)

    ans = max(ans, cnt)

print(ans)
