t = int(input())
for tc in range(t):
    l = list(map(int, input().split()))
    l.pop(0)
    l.sort()
    ans = 0
    for i in range(0, len(l)-1):
        for j in range(i+1, len(l)):
            min = l[i]
            max = l[j]
            while max % min != 0:
                max, min = min, max % min
            # print('>>>', l[i], l[j], '=', min)
            ans += min
    print(ans)
