import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, k, t, m = map(int, input().split())  # 팀수 문제수 내팀 로그수
    d = {x: [{y: 0 for y in range(1, k + 1)}, 0, 0] for x in range(1, n + 1)}
    for sq in range(m):
        i, j, s = map(int, input().split())
        d[i][0][j] = max(s, d[i][0][j])
        d[i][1] += 1
        d[i][2] = sq
    for k in d:
        d[k] = (-sum(d[k][0].values()), d[k][1], d[k][2])
    l = sorted(list(d.keys()), key=lambda x: d[x])
    # print(l)
    # print(d)
    for i in range(len(l)):
        if t == l[i]:
            print(i + 1)
            break
