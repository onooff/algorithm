import sys
import heapq
inputs = sys.stdin.readlines()

start = dict()
end = dict()
for i in range(1, len(inputs)):
    s, h, e = map(int, inputs[i].rstrip().split())
    start.setdefault(s, set())
    start[s].add(h)
    end.setdefault(e, set())
    end[e].add(h)

chk = list(set(start.keys()) | set(end.keys()))
chk.sort()

# print(chk, start, end)

cur = [0]
ended = dict()
maxx = 0
ans = list()
for c in chk:
    if c in start:
        for h in start[c]:
            heapq.heappush(cur, -h)
    if c in end:
        for h in end[c]:
            ended.setdefault(h, 0)
            ended[h] += 1
        while -cur[0] in ended:
            h = -heapq.heappop(cur)
            ended[h] -= 1
            if ended[h] == 0:
                ended.pop(h)
    if maxx != -cur[0]:
        maxx = -cur[0]
        ans.append(str(c))
        ans.append(str(maxx))

print(' '.join(ans))
