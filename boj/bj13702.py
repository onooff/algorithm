import sys

inputs = sys.stdin.readlines()
n, k = map(int, inputs[0].rstrip().split())
bottles = list(map(int, inputs[1:]))
bottles.sort()

left = 0
right = bottles[-1]
while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for b in bottles:
        cnt += b // mid
    if cnt >= k:
        left = mid + 1
    else:
        right = mid - 1
print((left + right) // 2)
