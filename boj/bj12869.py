# n = int(input())
# scvs = list(map(int, input().split()))
# d = [9, 3, 1]
# s = {(18, 6, 2), (18, 4, 4), (12, 10, 4), (12, 12, 2), (10, 10, 6)}

# cnt = 0
# is_end = False
# while not is_end:
#     scvs.sort(key=lambda x: -x)
#     print(scvs)
#     if tuple(scvs) in s:
#         cnt += 2
#         break
#     cnt += 1
#     is_end = True
#     for i in range(n):
#         scvs[i] -= d[i]
#         if scvs[i] > 0:
#             is_end = False
# print(cnt)

n = int(input())
scvs = list(map(int, input().split()))
scvs.sort()
scvs.append(0)
d = [
    [],
    [[9]],
    [(9, 3), (3, 9)],
    [(9, 3, 1), (9, 1, 3), (3, 9, 1), (1, 9, 3), (3, 1, 9), (1, 3, 9)]
]
chk = [[[False for i in range(61)] for j in range(61)]for k in range(61)]

q = [scvs]
go = True

while go:
    tmp = q.pop(0)
    # print(tmp)
    time = tmp[len(tmp)-1]+1
    for dd in d[len(tmp)-1]:
        new = list()
        for i in range(len(dd)):
            nn = tmp[i]-dd[i]
            if nn > 0:
                new.append(nn)
        new.sort()
        if len(new) == 0:
            print(time)
            go = False
            break
        elif len(new) == 1:
            if chk[new[0]][0][0]:
                continue
            else:
                chk[new[0]][0][0] = True
        elif len(new) == 2:
            if chk[new[0]][new[1]][0]:
                continue
            else:
                chk[new[0]][new[1]][0] = True
        elif len(new) == 3:
            if chk[new[0]][new[1]][new[2]]:
                continue
            else:
                chk[new[0]][new[1]][new[2]] = True

        new.append(time)
        q.append(new)


# print(type([9]))
