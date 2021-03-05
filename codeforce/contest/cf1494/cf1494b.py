t = int(input())

for tc in range(t):
    n, u, r, d, l = map(int, input().split())
    chk = [u, r, d, l]

    is_yes = False
    for i in range(4):  # start point
        if is_yes:
            break
        for j in [-1, 1]:  # direction
            if is_yes:
                break
            chk[0] = u
            chk[1] = r
            chk[2] = d
            chk[3] = l
            now = i
            for k in range(4):
                next_ = (now+j+4) % 4
                if chk[now] > 0 and chk[next_] > 0:
                    chk[now] -= 1
                    chk[next_] -= 1
                now = next_
            is_yes = True
            # print(chk)
            for c in chk:
                if c > n-2:
                    is_yes = False
                    break
    if is_yes:
        print('yes')
    else:
        print('no')

        # if l > 0 and u > 0:
        #     l -= 1
        #     u -= 1
        # if u > 0 and r > 0:
        #     u -= 1
        #     r -= 1
        # if r > 0 and d > 0:
        #     r -= 1
        #     d -= 1
        # if d > 0 and l > 0:
        #     d -= 1
        #     l -= 1
        # if u > n-2 or r > n-2 or d > n-2 or l > n-2:
        #     u = backup[0]
        #     r = backup[1]
        #     d = backup[2]
        #     l = backup[3]
        #     if l > 0 and u > 0:
        #         l -= 1
        #         u -= 1
        #     if d > 0 and l > 0:
        #         d -= 1
        #         l -= 1
        #     if r > 0 and d > 0:
        #         r -= 1
        #         d -= 1
        #     if u > 0 and r > 0:
        #         u -= 1
        #         r -= 1
        #     if u > n-2 or r > n-2 or d > n-2 or l > n-2:
        #         print('no')
        #     else:
        #         print('yes')
        # else:
        #     print('yes')
