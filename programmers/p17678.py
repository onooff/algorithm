'''
n회 t간격 배차 m명까지 탈 수 있다
'''


def parse(input_val):
    if type(input_val) == str:
        h, m = map(int, input_val.split(":"))
        return h*60+m
    else:
        m = str(input_val % 60).zfill(2)
        h = str(input_val // 60).zfill(2)
    return h+":"+m


def solution(n, t, m, timetable):
    times = list()
    for tt in timetable:
        times.append(parse(tt))
    times.sort()
    now = parse("09:00")
    ans = 0
    for i in range(n):
        seats = m
        if i == n-1:
            while seats > 1 and len(times) > 0 and times[0] <= now:
                times.pop(0)
                seats -= 1
            if len(times) == 0:
                ans = now
            else:
                ans = min(now, times[0]-1)
            break

        while seats > 0 and len(times) > 0 and times[0] <= now:
            times.pop(0)
            seats -= 1
        now += t
    return parse(ans)


print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
