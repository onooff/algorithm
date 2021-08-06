'''
1 1
2 1 1
3 1 1 1
4 2
5 2 1
6 2 1 1
7 2 1 1 1
8 2 2
9 3
...
'''
import math

n = int(input())
ans = 999999999


def dfs(n, cnt):
    global ans
    if n == 0:
        ans = min(ans, cnt)
        return
    if cnt+1 >= ans:
        return
    for i in range(max(1, int(math.sqrt(n//2))), int(math.sqrt(n))+1):
        dfs(n-i*i, cnt+1)


dfs(n, 0)
print(ans)
