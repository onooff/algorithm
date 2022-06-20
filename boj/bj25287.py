t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    l[0] = min(l[0], n-l[0]+1)
    ans = 'YES'
    for i in range(1, n):
        change = n-l[i]+1
        if l[i] < l[i-1] and change < l[i-1]:
            ans = 'NO'
            break
        else:
            minn = min(l[i], change)
            maxx = max(l[i], change)
            if minn >= l[i-1]:
                l[i] = minn
            else:
                l[i] = maxx
    print(ans)
