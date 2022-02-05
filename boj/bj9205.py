import sys
input = sys.stdin.readline
lim = 50*20
answer = {True: "happy", False: "sad"}
t = int(input())
for _ in range(t):
    n = int(input())
    home = tuple(map(int, input().rstrip().split()))
    nodes = set()
    for _ in range(n):
        nodes.add(tuple(map(int, input().rstrip().split())))
    festival = tuple(map(int, input().rstrip().split()))
    nodes.add(festival)

    q = [home]
    idx = 0
    nq = list()
    ans = False
    while len(q) > 0:
        cur = q[idx]
        if cur == festival:
            ans = True
            break
        idx += 1
        for nxt in list(nodes):
            d = abs(cur[0]-nxt[0])+abs(cur[1]-nxt[1])
            if d <= lim:
                nodes.discard(nxt)
                nq.append(nxt)
        if len(q) <= idx:
            idx = 0
            q = nq
            nq = list()
    print(answer[ans])
