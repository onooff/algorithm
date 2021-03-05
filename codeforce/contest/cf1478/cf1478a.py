t = int(input())

for tc in range(t):
    n = int(input())
    l = list(map(int, input().split()))

    last = -1
    ans = 0
    tmp = 0
    for i in l:
        if i == last:
            tmp += 1
        else:
            ans = max(ans, tmp)
            tmp = 1
            last = i
    ans = max(ans, tmp)
    print(ans)
