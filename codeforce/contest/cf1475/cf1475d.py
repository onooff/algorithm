t = int(input())

for tc in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    reg = list()
    imp = list()

    for i in range(n):
        if b[i] == 1:
            reg.append(a[i])
        else:
            imp.append(a[i])

    reg.sort()
    reg.reverse()
    imp.sort()
    imp.reverse()
    print(reg, imp)

    tmp = 0
    ans = 0
    while True:
        if len(reg) > 0:
            if tmp+reg[0] >= m:
                tmp += reg.pop(0)
                ans += 1
                break
        if len(reg) > 1 and len(imp) > 0:
            if reg[0]+reg[1] >= imp[0]:
                tmp += reg.pop(0)
                tmp += reg.pop(0)
                ans += 2
            else:
                tmp += imp.pop(0)
                ans += 2
        elif len(imp) > 0:
            tmp += imp.pop(0)
            ans += 2
        else:
            break
        if tmp >= m:
            break
        print('>>>', tmp, ans)

    if tmp < m:
        for n in reg:
            tmp += n
            ans += 1
            if tmp >= m:
                break
    print('-----------')
    if tmp < m:
        print('-1')
    else:
        print(ans)
    print('-----------')
