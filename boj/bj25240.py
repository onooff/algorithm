import sys
input = sys.stdin.readline

u, f = map(int, input().split())
users = dict()
for _ in range(u):
    inp = input().split()
    user = inp[0]
    groups = set()
    if len(inp) == 2:
        groups = set(inp[1].split(','))
    groups.add(user)
    users[user] = groups
files = dict()
for _ in range(f):
    file, permission, owner_user, owner_group = input().split()
    p = list()
    for num in permission:
        num = int(num)
        for i in [4, 2, 1]:
            if num >= i:
                p.append(1)
                num -= i
            else:
                p.append(0)
    files[file] = (tuple(p), owner_user, owner_group)
q = int(input())
for _ in range(q):
    user, file, action = input().split()
    d = 0
    if action == 'W':
        d = 1
    elif action == 'X':
        d = 2
    if files[file][1] == user:
        d += 0
    elif files[file][2] in users[user]:
        d += 3
    else:
        d += 6
    print(files[file][0][d])
