'''
2
8
3 2 7 8 1 4 5 6
10
2 1 3 4 5 6 7 9 10 8
'''

t = int(input())
for tc in range(t):
    n = int(input())
    graph = list(map(int, input().split()))
    chk = [False for i in range(n+1)]
    ans = 0
    for i in range(n):
        if not chk[i]:
            ans += 1
            now = i
            chk[i] = True
            while not chk[graph[now-1]]:
                now = graph[now-1]
                chk[now] = True
    print(ans)
