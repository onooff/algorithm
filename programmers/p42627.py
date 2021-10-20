import heapq


def solution(jobs):
    n = len(jobs)
    jobs.sort(key=lambda x: x[0])

    q = list()
    t = 0
    summ = 0
    while len(jobs) > 0 or len(q) > 0:
        while len(jobs) > 0 and jobs[0][0] <= t:
            j = jobs.pop(0)
            # print(t, j)
            heapq.heappush(q, (j[1], j[0]))
        if len(q) == 0:
            t = jobs[0][0]
            continue
        proc = heapq.heappop(q)
        # print(proc)
        t += proc[0]
        summ += t-proc[1]
    return summ//n
