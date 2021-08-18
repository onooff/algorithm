'''
4
500 500 500 500
1 4 3 -2
-2 1 4 3
3 -2 1 4
4 3 -2 1
1
'''

n = int(input())
players = list(map(int, input().split()))
r = [list(map(int, input().split())) for i in range(n)]
mafia = int(input())
answer = 0
is_max = False
for i in range(n):
    r[i][i] = 1


def dfs(live=int(), night=int()):
    global n, players, r, mafia, answer, is_max
    if live == 2:
        answer = night+1
        is_max = True
        return
    if live % 2 == 0:
        for target in range(n):
            if r[target][target] == 1 and target != mafia:
                r[target][target] = 0
                for i in range(n):
                    if r[i][i] == 1:
                        players[i] += r[target][i]
                dfs(live-1, night+1)
                if is_max:
                    return
                for i in range(n):
                    if r[i][i] == 1:
                        players[i] -= r[target][i]
                r[target][target] = 1
    else:
        most_guilty = -999999
        bye = -1
        for i in range(n):
            if r[i][i] == 1 and players[i] > most_guilty:
                most_guilty = players[i]
                bye = i
        if bye == mafia:
            answer = max(answer, night)
            return
        else:
            r[bye][bye] = 0
            dfs(live-1, night)
            if is_max:
                return
            r[bye][bye] = 1


if n == 1:
    print(0)
else:
    dfs(n, 0)
    print(answer)
