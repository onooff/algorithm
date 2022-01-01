import sys
import heapq
inputs = sys.stdin.readlines()

for i in range(2, len(inputs), 2):
    nums = list(map(int, inputs[i].rstrip().split()))
    # heapq.heapify(nums)
    nums.sort()
    cost = 0
    while len(nums) > 1:
        tmp = heapq.heappop(nums)+heapq.heappop(nums)
        cost += tmp
        heapq.heappush(nums, tmp)
    print(cost)
