import sys
import math

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))

l = [[a[i], b[i]] for i in range(n)]
l.sort(key=lambda x: x[1])

answer = 0
cur_max = -1
last_max = -1
for i in range(n):
    if i > 0 and l[i - 1][1] < l[i][1]:
        last_max = cur_max
        cur_max = -1

    if last_max == -1:
        ans = math.ceil((l[i][1] - l[i][0]) / 30)
    else:
        ans = math.ceil((max(l[i][1], last_max) - l[i][0]) / 30)
    if ans > 0:
        answer += ans
        l[i][0] += 30 * ans
    cur_max = max(cur_max, l[i][0])

print(answer)
