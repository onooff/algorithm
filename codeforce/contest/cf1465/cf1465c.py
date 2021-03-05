t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    y_set = set()
    x_set = set()
    rooks = set()
    rooks_list = list()
    for i in range(m):
        tmp = tuple(map(int, input().split()))
        rooks.add(tmp)
        rooks_list.append(tmp)
        y_set.add(tmp[0])
        x_set.add(tmp[1])
    # print(rooks, y_set, x_set)

    cnt = 0
    is_ok = False
    while not is_ok:
        print(rooks, y_set, x_set)
        is_ok = True
        # tmp_set = set()
        for rook in rooks_list:
            print(rook, 'move to', end='')
            if rook[0] == rook[1]:
                pass
            elif (rook[1] not in y_set):
                is_ok = False
                cnt += 1
                rooks.remove(rook)
                y_set.remove(rook[0])
                x_set.remove(rook[1])
                # rook[0] = rook[1]
                rook = (rook[1], rook[1])
                y_set.add(rook[0])
                x_set.add(rook[1])
                rooks.add(rook)
                # tmp_set.add(rook)
            elif (rook[0] not in x_set):
                is_ok = False
                cnt += 1
                rooks.remove(rook)
                y_set.remove(rook[0])
                x_set.remove(rook[1])
                # rook[1] = rook[0]
                rook = (rook[0], rook[0])
                y_set.add(rook[0])
                x_set.add(rook[1])
                rooks.add(rook)
                # tmp_set.add(rook)
            else:
                is_ok = False
                for i in range(1, n+1):
                    if (i not in y_set) and (i not in x_set):
                        cnt += 1
                        rooks.remove(rook)
                        y_set.remove(rook[0])
                        x_set.remove(rook[1])
                        # rook[0] = i
                        rook = (i, rook[1])
                        y_set.add(rook[0])
                        x_set.add(rook[1])
                        rooks.add(rook)
                        # tmp_set.add(rook)
                        break
            print(rook)
            if not is_ok:
                break
        rooks_list = list(rooks)
        # rooks = tmp_set
    print(cnt)
