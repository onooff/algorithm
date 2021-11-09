import sys
import heapq
inputs = sys.stdin.readlines()
left_q = [-int(inputs[1])]  # max queue
right_q = list()  # min queue

print(-left_q[0])
odd = True
for i in range(2, len(inputs)):
    n = int(inputs[i])
    if n < -left_q[0]:
        heapq.heappush(left_q, -n)
    else:
        heapq.heappush(right_q, n)
    odd = not odd
    if odd:
        while len(left_q)-1 != len(right_q):
            if len(left_q)-1 > len(right_q):
                heapq.heappush(right_q, -heapq.heappop(left_q))
            else:
                heapq.heappush(left_q, -heapq.heappop(right_q))
    else:
        while len(left_q) != len(right_q):
            if len(left_q) > len(right_q):
                heapq.heappush(right_q, -heapq.heappop(left_q))
            else:
                heapq.heappush(left_q, -heapq.heappop(right_q))
    print(-left_q[0])
