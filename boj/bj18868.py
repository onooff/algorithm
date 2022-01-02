import sys
input = sys.stdin.readline

m, n = map(int, input().rstrip().split())
universes = list()
for _ in range(m):
    universe = list()
    inp = list(map(int, input().rstrip().split()))
    for i in range(len(inp)-1):
        for j in range(i+1, len(inp)):
            if inp[i] > inp[j]:
                universe.append('>')
            elif inp[i] < inp[j]:
                universe.append('<')
            else:
                universe.append('=')
    universes.append(''.join(universe))

cnt = 0
for i in range(m-1):
    for j in range(i+1, m):
        if universes[i] == universes[j]:
            cnt += 1
print(cnt)
