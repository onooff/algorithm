def solution(n, t, m, timetable):

    timetable.sort()
    hour = 9
    min = 0

    while n > 0:
        bus_m = m
        n -= 1
        hour += (min // 60)
        min %= 60

        if n == 0:  # 막차일때:탈수있는 시간보기
            while (int(timetable[0][:2]) < hour) or ((int(timetable[0][:2]) == hour) and (int(timetable[0][3:]) <= min)):
                timetable.pop(0)
                bus_m -= 1
                if bus_m == 1:
                    return (int(timetable[0][:2]) == hour) and (int(timetable[0][3:])
            print(timetable)
            pass
        else:  # 막차아닐때:그냥보내기
            while (int(timetable[0][:2]) < hour) or ((int(timetable[0][:2]) == hour) and (int(timetable[0][3:]) <= min)):
                timetable.pop(0)
                bus_m -= 1
                if bus_m == 0:
                    break

        min += t


# print(solution(1, 1, 5, ["00:02", "00:01", "00:01", "00:01", "00:01"]))
print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
