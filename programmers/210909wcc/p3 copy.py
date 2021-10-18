import heapq


def solution(a, b, g, s, w, t):
    q = [[t[i], i] for i in range(len(w))]
    heapq.heapify(q)
    cur = 0
    while len(q) > 0:
        cur = heapq.heappop(q)
        i = cur[1]
        ww = w[i]

        if a > b:
            if ww > 0 and a > 0 and g[i] > 0:
                get = min(ww, a, g[i])
                ww -= get
                a -= get
                g[i] -= get
            if ww > 0 and b > 0 and s[i] > 0:
                get = min(ww, b, s[i])
                ww -= get
                b -= get
                s[i] -= get
        elif a < b:
            if ww > 0 and b > 0 and s[i] > 0:
                get = min(ww, b, s[i])
                ww -= get
                b -= get
                s[i] -= get
            if ww > 0 and a > 0 and g[i] > 0:
                get = min(ww, a, g[i])
                ww -= get
                a -= get
                g[i] -= get
        else:
            if g[i] > s[i]:
                if ww > 0 and a > 0 and g[i] > 0:
                    get = min(ww, a, g[i])
                    ww -= get
                    a -= get
                    g[i] -= get
                if ww > 0 and b > 0 and s[i] > 0:
                    get = min(ww, b, s[i])
                    ww -= get
                    b -= get
                    s[i] -= get
            elif s[i] > g[i]:
                if ww > 0 and b > 0 and s[i] > 0:
                    get = min(ww, b, s[i])
                    ww -= get
                    b -= get
                    s[i] -= get
                if ww > 0 and a > 0 and g[i] > 0:
                    get = min(ww, a, g[i])
                    ww -= get
                    a -= get
                    g[i] -= get
            else:
                if ww > 0 and a > 0 and g[i] > 0:
                    get = min(ww, a, g[i])
                    ww -= get
                    a -= get
                    g[i] -= get
                if ww > 0 and b > 0 and s[i] > 0:
                    get = min(ww, b, s[i])
                    ww -= get
                    b -= get
                    s[i] -= get

        # print(cur, a, b)
        if a == 0 and b == 0:
            break
        if g[i] == 0 and s[i] == 0:
            continue
        cur[0] += t[i]*2
        heapq.heappush(q, cur)
    return cur[0]
