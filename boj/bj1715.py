import sys
import heapq

inputs = sys.stdin.readlines()
nums = list(map(int, inputs[1:]))
heapq.heapify(nums)
ans = 0
while len(nums) > 1:
    tmp = 0
    tmp += heapq.heappop(nums)
    tmp += heapq.heappop(nums)
    ans += tmp
    heapq.heappush(nums, tmp)
print(ans)
