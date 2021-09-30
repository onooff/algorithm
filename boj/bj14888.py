n = int(input())
l = list(map(int, input().split()))
operator = list(map(int, input().split()))

maxx = -99999999999999999999999999999999999999999
minn = 99999999999999999999999999999999999999999


def dfs(val, idx):
    global n, l, operator, minn, maxx
    if idx == len(l):
        maxx = max(val, maxx)
        minn = min(val, minn)
        return

    for i in range(4):
        if operator[i] > 0:
            if i == 0:
                nval = val+l[idx]
            elif i == 1:
                nval = val-l[idx]
            elif i == 2:
                nval = val*l[idx]
            elif i == 3:
                if val < 0:
                    nval = -((-val)//l[idx])
                else:
                    nval = val//l[idx]

            operator[i] -= 1
            dfs(nval, idx+1)
            operator[i] += 1


dfs(l[0], 1)

print(maxx)
print(minn)
