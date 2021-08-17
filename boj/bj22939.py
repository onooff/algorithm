'''
10
HXXJXXXXXB
JXXXXXWXXX
XXWXXXXBXX
CXXXXXXXXX
XXXXXXXXXX
XXCXXBXXXX
XXXXXWXXXJ
XXXXXXXXXX
XXXXCXXXXX
XXXXXXXXX#
'''
import itertools

n = int(input())
board = list()
home = 0
end = 0
stuff_dict = {"J": set(), "C": set(), "B": set(), "W": set()}
ans_dict = {"J": "Assassin", "C": "Healer", "B": "Mage", "W": "Tanker"}
for i in range(n):
    board.append(input())
    for j in range(len(board[i])):
        if board[i][j] == 'H':
            home = (i, j)
        elif board[i][j] == '#':
            end = (i, j)
        elif board[i][j] in stuff_dict:
            stuff_dict[board[i][j]].add((i, j))

ans = "?"
min_dis = 99999999999999999
for stuff in ["J", "C", "B", "W"]:
    perm = list(itertools.permutations(stuff_dict[stuff]))
    for p in perm:
        last = home
        dis = 0
        for go in p:
            dis += abs(last[0]-go[0])+abs(last[1]-go[1])
            last = go
        dis += abs(last[0]-end[0])+abs(last[1]-end[1])
        if dis < min_dis:
            min_dis = dis
            ans = stuff
print(ans_dict[ans])
