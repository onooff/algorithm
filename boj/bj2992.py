n = input()
chk = set()
perm = set()
p = ['' for _ in range(len(n))]


def dfs(n=str()):
    global chk, perm, p
    if len(chk) >= len(n):
        perm.add(int(''.join(p)))
        return

    for i in range(len(n)):
        if i not in chk:
            p[len(chk)] = n[i]
            chk.add(i)
            dfs(n)
            chk.discard(i)


dfs(n)
perm = list(perm)
perm.sort()
n = int(n)
for i in range(len(perm)):
    if perm[i] == n:
        if i == len(perm)-1:
            print(0)
        else:
            print(perm[i+1])
