import sys

inputs = sys.stdin.readlines()

n, m, l, star = map(int, inputs[0].split())

li = list()
for i in range(1, len(inputs)):
    li.append(tuple(map(int, inputs[i].rstrip().split())))

li.sort()


maxx = -1
for i in range(len(li)):
    pick = list()
    if len(li) - i <= maxx:
        break
    for j in range(i, len(li)):
        if li[j][0] - li[i][0] <= l:
            pick.append(li[j])
    if len(pick) <= maxx:
        continue
    pick.sort(key=lambda x: x[1])
    for j in range(len(pick)):
        if len(pick) - j <= maxx:
            break
        cnt = 0
        for k in range(j, len(pick)):
            if pick[k][1] - pick[j][1] <= l:
                cnt += 1
        maxx = max(maxx, cnt)

print(star - maxx)
