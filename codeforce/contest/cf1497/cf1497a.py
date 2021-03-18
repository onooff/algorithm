t = int(input())

for tc in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    sort = [0 for i in range(101)]
    for num in l:
        sort[num] += 1
    ans = list()
    for i in range(101):
        if sort[i] > 0:
            sort[i] -= 1
            ans.append(i)
    for i in range(101):
        while sort[i] > 0:
            sort[i] -= 1
            ans.append(i)
    print(*ans)
