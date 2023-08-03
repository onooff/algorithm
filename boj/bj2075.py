import sys
import heapq

inputs = sys.stdin.readlines()

n = int(inputs[0])
h = list(map(int, inputs[1].rstrip().split()))
heapq.heapify(h)
for i in range(2, len(inputs)):
    l = list(map(int, inputs[i].rstrip().split()))
    for num in l:
        if num > h[0]:
            heapq.heappop(h)
            heapq.heappush(h, num)

print(h[0])
