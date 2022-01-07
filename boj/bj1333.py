import heapq
n, l, d = map(int, input().split())
playing = False
q = [(0, 0), (0, 1)]
t = 0
while len(q) > 0:
    cur = heapq.heappop(q)
    t = cur[0]
    if cur[1] == 0:  # song event
        if playing:
            playing = False
            heapq.heappush(q, (cur[0]+5, 0))
        elif not playing and n > 0:
            n -= 1
            playing = True
            heapq.heappush(q, (cur[0]+l, 0))
    else:  # cur[1] == 1 # ring event
        if playing:
            heapq.heappush(q, (cur[0]+d, 1))
        else:
            break
print(t)
