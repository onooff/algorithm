limit = list(map(int, input().split()))
start = (0, 0, limit[2])
ans = set()
ans.add(start)


def dfs(now):
    global limit, ans
    for i in range(3):
        if now[i] != 0:
            for j in range(3):
                # limit-now만큼 받을 수 있음 or 주는쪽 all
                if i != j and limit[j]-now[j] != 0:
                    change = list(now)
                    if limit[j]-now[j] > now[i]:
                        change[j] += now[i]
                        change[i] = 0
                    else:
                        change[i] -= limit[j]-now[j]
                        change[j] = limit[j]
                    change = tuple(change)
                    if change not in ans:
                        ans.add(change)
                        dfs(change)


dfs(start)
# print(ans)
answer = set()
for a in ans:
    if a[0] == 0:
        answer.add(a[2])
answer = list(answer)
answer.sort()
for a in answer:
    print(a, end=' ')
