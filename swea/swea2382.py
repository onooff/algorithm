t = int(input())


def is_red(y, x, n):
    return x == 0 or y == 0 or x == n-1 or y == n-1


direction = ((-1, 0), (1, 0), (0, -1), (0, 1))
convert = {0: 1, 1: 0, 2: 3, 3: 2}
for tc in range(1, t+1):
    n, m, k = map(int, input().split())
    # n*n 사이즈 맵, m시간, k개 미생물
    d = dict()
    for i in range(k):
        y, x, num, go = map(int, input().split())
        yx = (y, x)
        d.setdefault(yx, list())
        d[yx].append((num, go-1))

    for i in range(m):
        nd = dict()
        for key in d:
            if len(d[key]) > 1:
                s = 0
                max_val = -1
                sum_go = -1
                for info in d[key]:
                    if info[0] > max_val:
                        max_val = info[0]
                        sum_go = info[1]
                    s += info[0]
                d[key] = [(s, sum_go)]
            val = d[key][0][0]
            go = d[key][0][1]
            ny = key[0]+direction[go][0]
            nx = key[1]+direction[go][1]
            if is_red(ny, nx, n):
                val = val//2
                if val == 0:
                    continue
                go = convert[go]
            nynx = (ny, nx)
            nd.setdefault(nynx, list())
            nd[nynx].append((val, go))
        d = nd
    ans = 0
    for key in d:
        for info in d[key]:
            ans += info[0]
    print('#', tc, ' ', ans, sep='')
