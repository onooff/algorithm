t = int(input())

for tc in range(t):
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    d = dict()
    for num in l:
        num = num % m
        if num not in d:
            d.setdefault(num, 0)
        d[num] += 1
    ans = 0
    # print(d)

    if 0 in d:
        ans += 1
        d.pop(0)

    i = 0
    while len(d) > 0:
        # print(d, ans)
        i += 1
        if i in d and m-i in d:
            if m-i == i:
                ans += 1
                d.pop(i)
            else:
                tmp = min(d[m-i], d[i])
                d[m-i] -= tmp
                d[i] -= tmp
                ans += 1
                if d[m-i] == 0 and d[i] == 0:
                    d.pop(m-i)
                    d.pop(i)
                elif d[m-i] == 0:
                    d.pop(m-i)
                    d[i] -= 1
                    ans += d[i]
                    d.pop(i)
                else:
                    d.pop(i)
                    d[m-i] -= 1
                    ans += d[m-i]
                    d.pop(m-i)
        else:
            if i in d:
                ans += d[i]
                d.pop(i)
            elif m-i in d:
                ans += d[m-i]
                d.pop(m-i)
    # print('>>>', ans)
    print(ans)
