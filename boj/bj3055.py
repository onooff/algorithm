import sys


def isin(r, c, i, j):
    if i >= 0 and j >= 0 and i < r and j < c:
        return True
    return False


d = [
    [0, 1],
    [0, -1],
    [1, 0],
    [-1, 0]
]
r, c = map(int, input().split())
map = list()
water = list()
hedgehog = list()
time = 0
for i in range(r):
    map.append(list(input()))
    for j in range(c):
        if map[i][j] == '*':
            water.append((i, j, time))
        elif map[i][j] == 'S':
            hedgehog.append(([i, j, time]))

while len(water) > 0 or len(hedgehog) > 0:
    while len(water) > 0 and water[0][2] == time:
        w = water.pop(0)
        for i in range(len(d)):
            ni = w[0]+d[i][0]
            nj = w[1]+d[i][1]
            # if isin(r, c, ni, nj) and (map[ni][nj] == '.' or map[ni][nj] == 'S'):
            if isin(r, c, ni, nj) and (map[ni][nj] == '.'):
                water.append((ni, nj, time+1))
                map[ni][nj] = '*'
    while len(hedgehog) > 0 and hedgehog[0][2] == time:
        h = hedgehog.pop(0)
        for i in range(len(d)):
            ni = h[0]+d[i][0]
            nj = h[1]+d[i][1]
            if isin(r, c, ni, nj):
                if map[ni][nj] == 'D':
                    print(time+1)
                    sys.exit()
                elif map[ni][nj] == '.':
                    hedgehog.append((ni, nj, time+1))
                    map[ni][nj] = 'S'
    time += 1
    # for i in range(r):
    #     print(map[i])
    # print(water)
    # print(hedgehog)
    # print('-----------')

print('KAKTUS')
