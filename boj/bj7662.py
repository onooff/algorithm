import sys
import heapq
input = sys.stdin.readline

t = int(input())
for tc in range(t):
    cnt = int(input())
    minq = list()
    maxq = list()
    d = dict()
    for i in range(cnt):
        command = input().split(' ')
        c = command[0]
        n = int(command[1])
        if c == 'I':
            heapq.heappush(minq, n)
            heapq.heappush(maxq, -n)
            d.setdefault(n, 0)
            d[n] += 1
        else:  # c=='D'
            if len(d) == 0:
                continue
            dn = "dn"
            if n == 1:
                while dn not in d:
                    dn = -heapq.heappop(maxq)
            else:
                while dn not in d:
                    dn = heapq.heappop(minq)
            d[dn] -= 1
            if d[dn] <= 0:
                d.pop(dn)
                if len(d) == 0:
                    minq = list()
                    maxq = list()
        # print(d, minq, maxq)
    if len(d) > 0:
        maxmax = "lol"
        minmin = "lol"
        while maxmax not in d:
            maxmax = -heapq.heappop(maxq)
        while minmin not in d:
            minmin = heapq.heappop(minq)
        print(maxmax, minmin)
    else:
        print("EMPTY")
