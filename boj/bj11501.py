import sys

input = sys.stdin.readline
t = int(input())

answer = []
for _ in range(t):
    n = int(input())
    l = list(map(int, input().rstrip().split()))
    maxx = -1
    ans = 0
    for i in range(len(l) - 1, -1, -1):
        if l[i] > maxx:
            maxx = l[i]
            continue
        d = maxx - l[i]
        if d > 0:
            ans += d
    answer.append(str(ans))
print("\n".join(answer))
