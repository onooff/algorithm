'''
2
4
3 2 1 4
2 3 4 1
8
3 6 5 4 8 7 1 2
5 6 8 4 3 1 2 7
'''
pre_o = list()
in_o = list()
go = -1


def make_post(pool=list()):
    global pre_o, in_o, go
    go += 1
    now = pre_o[go]
    idx = pool.index(now)
    left = pool[:idx]
    right = pool[idx+1:]
    # print(pool, now, idx, left, right)
    l_ret = ""
    r_ret = ""
    if len(left) != 0:
        l_ret = make_post(left)
    if len(right) != 0:
        r_ret = make_post(right)
    return l_ret+r_ret+str(now)+" "


t = int(input())
for tc in range(t):
    go = -1
    size = int(input())
    pre_o = list(map(int, input().split()))
    in_o = list(map(int, input().split()))
    # for i in range(size):
    #     pre_o[i] -= 1
    #     in_o[i] -= 1

    print(make_post(in_o))
