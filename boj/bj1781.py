import sys
import heapq
inputs = sys.stdin.readlines()
n = int(inputs[0])
l = list(map(lambda x: tuple(map(int, x.split())), inputs[1:]))
l.sort(key=lambda x: (x[0], -x[1]))

pq = list()
for cur in l:
    if len(pq) >= cur[0] and pq[0] < cur[1] and len(pq) > 0:
        heapq.heappop(pq)
    if len(pq) < cur[0]:
        heapq.heappush(pq, cur[1])
print(sum(pq))
