import sys

input = sys.stdin.readline

n = int(input())
li = list(map(int, input().rstrip().split()))

answer = 0
l = 0
r = 0
cnt = [0 for _ in range(100001)]
cnt[li[0]] = 1
while l < n:
    if r + 1 < n and cnt[li[r + 1]] == 0:
        r += 1
        cnt[li[r]] += 1
    else:
        answer += r - l + 1
        cnt[li[l]] -= 1
        l += 1
print(answer)
