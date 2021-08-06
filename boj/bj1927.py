# stdin 안쓰면 시간초과

import heapq
import sys
input = sys.stdin.readline

heap = list()
heapq.heapify(heap)

n = int(input())

for i in range(n):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)
