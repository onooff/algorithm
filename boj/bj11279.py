import sys
import heapq

n = int(input())
h = list()

for i in range(n):
    command = int(sys.stdin.readline())
    if command == 0:
        try:
            print(-heapq.heappop(h))
        except:
            print(0)
    else:
        heapq.heappush(h, -command)
