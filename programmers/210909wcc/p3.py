import heapq
import math


def solution(a, b, g, s, w, t):
    q = [[t[i], i] for i in range(len(w))]
    heapq.heapify(q)
    cur = 0
    while len(q) > 0:
        cur = heapq.heappop(q)
        i = cur[1]

        ww = w[i]
        half = math.floor(ww/2)
        get_gold = min(half, g[i], a)
        get_silv = min(half, s[i], b)
        ww -= get_gold+get_silv
        g[i] -= get_gold
        a -= get_gold
        s[i] -= get_silv
        b -= get_silv
        if ww > 0:
            if a > 0 and g[i] > 0:
                a -= min(ww, g[i])
            if b > 0 and s[i] > 0:
                b -= min(ww, s[i])
            # print(cur, a, b)
        if a <= 0 and b <= 0:
            break
        if g[i] == 0 and s[i] == 0:
            continue
        cur[0] += t[i]*2
        heapq.heappush(q, cur)
    return cur[0]
