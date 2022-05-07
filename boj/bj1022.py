base = [[1], [1], [1], [1]]
level = 0
n = 1
lim = 5000
while level < lim:
    level += 1
    n += level
    for i in range(4):
        base[i].append(n)
        n += level*2
    n -= level


def get_num(i, j):
    maxx = max(abs(i), abs(j))
    level = maxx
    d = -1
    if maxx == abs(i):
        minn = j
        if i > 0:
            d = 3
        else:
            d = 1
            minn = -minn
    else:
        minn = i
        if j > 0:
            d = 0
            minn = -minn
        else:
            d = 2
    return base[d][level]+minn


inputs = list(map(int, input().split()))
if inputs[0] > inputs[2]:
    inputs[0], inputs[2] = inputs[2], inputs[0]
if inputs[1] > inputs[3]:
    inputs[1], inputs[3] = inputs[3], inputs[1]

ans = list()
max_len = -1
l = -1
for i in range(inputs[0], inputs[2]+1):
    l += 1
    ans.append(list())
    for j in range(inputs[1], inputs[3]+1):
        n = str(get_num(i, j))
        max_len = max(max_len, len(n))
        ans[l].append(n)

for i in range(len(ans)):
    for j in range(len(ans[i])):
        print(f"{ans[i][j]:>{max_len}}", end=' ')
    print()
