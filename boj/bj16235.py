import sys
inputs = sys.stdin.readlines()
n, m, k = map(int, inputs[0].rsplit())
refill = inputs[1:n+1]
for i in range(n):
    refill[i] = list(map(int, refill[i].rstrip().split()))
food = [[5 for _ in range(n)]for _ in range(n)]
tree = [[list() for _ in range(n)]for _ in range(n)]
tree_set = set()
for i in range(n+1, n+m+1):
    y, x, t = map(int, inputs[i].rstrip().split())
    y, x = y-1, x-1
    tree[y][x].append(t)
    tree_set.add((y, x))
for _ in range(k):
    ts = set()
    grow = dict()
    for yx in tree_set:
        goodbye = False
        for i in range(len(tree[yx[0]][yx[1]])):
            if food[yx[0]][yx[1]] >= tree[yx[0]][yx[1]][i]:
                food[yx[0]][yx[1]] -= tree[yx[0]][yx[1]][i]
                tree[yx[0]][yx[1]][i] += 1
                if tree[yx[0]][yx[1]][i] % 5 == 0:
                    grow.setdefault(yx, 0)
                    grow[yx] += 1
            else:
                goodbye = True
                break
        if goodbye:
            die = tree[yx[0]][yx[1]][i:]
            tree[yx[0]][yx[1]] = tree[yx[0]][yx[1]][:i]
            # print(_, 'year', food[yx[0]][yx[1]], tree[yx[0]][yx[1]], die)
            for deadtree in die:
                food[yx[0]][yx[1]] += deadtree//2
        if len(tree[yx[0]][yx[1]]) > 0:
            ts.add(yx)
    for yx in grow:
        baby = grow[yx]
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dy == 0 and dx == 0:
                    continue
                ny = yx[0]+dy
                nx = yx[1]+dx
                if 0 <= ny < n and 0 <= nx < n:
                    # for b in range(baby):
                    # tree[ny][nx].insert(0, 1)
                    tree[ny][nx] = [1 for i in range(baby)]+tree[ny][nx]
                    ts.add((ny, nx))
    for i in range(n):
        for j in range(n):
            food[i][j] += refill[i][j]
    tree_set = ts
    # print(food, tree_set)

ans = 0
for yx in tree_set:
    ans += len(tree[yx[0]][yx[1]])
print(ans)
