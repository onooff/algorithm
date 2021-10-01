import sys
inputs = sys.stdin.readlines()
n = int(inputs[0])
stat = list()
for i in range(1, n+1):
    stat.append(list(map(int, inputs[i].rstrip().split())))

nn = n//2
ans = 9999999999999999999999999999999999999


def dfs(team1, team2, idx):
    global n, stat, nn, ans
    if idx == n:
        team1_stat = 0
        team2_stat = 0
        for m1 in team1:
            for m2 in team1:
                team1_stat += stat[m1][m2]
        for m1 in team2:
            for m2 in team2:
                team2_stat += stat[m1][m2]
        ans = min(ans, abs(team1_stat-team2_stat))
        return

    if len(team1) < nn:
        team1.add(idx)
        dfs(team1, team2, idx+1)
        team1.discard(idx)

    if len(team2) < nn:
        team2.add(idx)
        dfs(team1, team2, idx+1)
        team2.discard(idx)


dfs(set(), set(), 0)
print(ans)
