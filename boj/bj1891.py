n, m = input().split()
n = int(n)
m = list(m)
m = list(map(int, m))
x, y = map(int, input().split())


def get_v(n, m):
    ret = [0, 0]
    d = 2**(n-1)
    for i in range(n):
        if m[i] == 1:
            ret[0] += d
            ret[1] += d
        elif m[i] == 2:
            ret[1] += d
        elif m[i] == 4:
            ret[0] += d
        d //= 2
    return ret


def ret_v(n, xy):
    # xy = [0, 0]
    ret = str()
    d = 2**(n-1)
    for i in range(n):
        chkx = xy[0]//d
        chky = xy[1]//d
        # print(xy, d, chkx, chky)
        if chkx and chky:
            ret += '1'
        elif chky:
            ret += '2'
        elif chkx:
            ret += '4'
        else:
            ret += '3'
        xy[0] %= d
        xy[1] %= d
        d //= 2
    return ret


now = get_v(n, m)
now[0] += x
now[1] += y

b = 2**n
if (0 <= now[0] < b) and (0 <= now[1] < b):
    print(ret_v(n, now))
else:
    print(-1)
