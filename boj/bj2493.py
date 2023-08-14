# import sys

# input = sys.stdin.readline
# n = int(input())
# l = list(map(int, input().rstrip().split()))

# ans = [0 for _ in range(n)]
# stk = list()
# for i in range(n - 1, -1, -1):
#     ii = i + 1
#     while len(stk) > 0 and stk[-1][0] < l[i]:
#         ans[stk[-1][1]] = ii
#         stk.pop()
#     stk.append((l[i], i))

# print(*ans)

import sys

input = sys.stdin.readline
n = int(input())
l = list(map(int, input().rstrip().split()))

ans = [0 for _ in range(n)]
stk = [(float("inf"), -1)]
for i, num in enumerate(l):
    while stk[-1][0] < num:
        stk.pop()
    ans[i] = stk[-1][1] + 1
    stk.append((num, i))

print(*ans)
