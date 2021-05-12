def is_in(i, j, n):
    return 0 <= i < n and 0 <= j < n


n, m = map(int, input().split())
map1 = list()
map2 = list()
for i in range(n):
    map1.append(list(map(int, input().split())))
    map2.append([0 for j in range(n)])
map2[n-1][0] = 1
map2[n-1][1] = 1
map2[n-2][0] = 1
map2[n-2][1] = 1

dl = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
nd = [0, 0]

for go in range(m):
    d, s = map(int, input().split())
    d -= 1
    nd[0] = (nd[0]+dl[d][0]*s) % n
    nd[1] = (nd[1]+dl[d][1]*s) % n
    # print(d, s, nd)
    was_cloudy = set()
    for i2 in range(n):
        for j2 in range(n):
            i1 = (i2+nd[0]) % n
            j1 = (j2+nd[1]) % n
            if i1 < 0:
                i1 = n+i1
            if j1 < 0:
                j1 = n+j1
            if map2[i2][j2] == 1:
                # print(i1, j1, map1[i1][j1], i2, j2)
                was_cloudy.add((i1, j1))
                map1[i1][j1] += 1
                map2[i2][j2] = 0
    for ij in was_cloudy:
        i = ij[0]
        j = ij[1]
        for d4 in [1, 3, 5, 7]:
            ni = i+dl[d4][0]
            nj = j+dl[d4][1]
            if is_in(ni, nj, n) and map1[ni][nj] > 0:
                map1[i][j] += 1
    for i2 in range(n):
        for j2 in range(n):
            i1 = (i2+nd[0]) % n
            j1 = (j2+nd[1]) % n
            if i1 < 0:
                i1 = n+i1
            if j1 < 0:
                j1 = n+j1
            if (i1, j1) not in was_cloudy and map1[i1][j1] >= 2:
                map2[i2][j2] = 1
                map1[i1][j1] -= 2
    # print((d, s), '-------------', nd)
    # for i in range(n):
    #     print(map1[i])
    # print()
    # for i in range(n):
    #     print(map2[i])
ans = 0
for i in range(n):
    ans += sum(map1[i])
print(ans)
