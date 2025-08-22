n = int(input())
eggs = list()
for i in range(n):
    eggs.append(list(map(int, input().split())))

maxx = 0


def dfs(cur, broken):
    global eggs, maxx
    if cur >= len(eggs):
        maxx = max(maxx, broken)
        return

    if eggs[cur][0] > 0:
        all_broken = True
        for target in range(len(eggs)):
            if target != cur and eggs[target][0] > 0:
                all_broken = False
                eggs[target][0] -= eggs[cur][1]
                eggs[cur][0] -= eggs[target][1]
                if eggs[cur][0] <= 0:
                    broken += 1
                if eggs[target][0] <= 0:
                    broken += 1
                dfs(cur + 1, broken)
                if eggs[cur][0] <= 0:
                    broken -= 1
                if eggs[target][0] <= 0:
                    broken -= 1
                eggs[target][0] += eggs[cur][1]
                eggs[cur][0] += eggs[target][1]
        if all_broken:
            dfs(cur + 1, broken)
    else:
        dfs(cur + 1, broken)


dfs(0, 0)
print(maxx)
