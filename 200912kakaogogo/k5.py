def timeToint(time):
    # print(time[:2], time[3:5], time[6:])
    # print(int(time[:2])*3600+int(time[3:5])*60+int(time[7:]))
    return int(time[:2])*3600+int(time[3:5])*60+int(time[7:])


def intTotime(val):
    h = val//3600
    val = val % 3600
    m = val//60
    val = val % 60
    s = val
    return str(h).zfill(2)+":"+str(m).zfill(2)+":"+str(s).zfill(2)


def solution(play_time, adv_time, logs):
    answer = ''
    a = 0

    size = timeToint(play_time)
    timeline = [0 for i in range(size)]
    adLangth = timeToint(adv_time)
    maxview = -1

    for t in logs:
        # print("와우")
        tmp = t.split("-")
        start = timeToint(tmp[0])
        end = timeToint(tmp[1])
        for i in range(start, end):
            timeline[i] += 1
            maxview = max(maxview, timeline[i])

    # print(len(timeline))
    # print(maxview)
    flag = False
    for i in range(0, size):
        if timeline[i] == maxview:
            flag = True
        if flag and timeline[i] != maxview:
            a = max(i-adLangth, 0)
            break
    answer = intTotime(a)
    return answer


print(solution(	"02:03:55", "00:14:15", [
      "01:20:15-01:45:14", "00:25:50-00:48:29",
      "00:40:31-01:00:00", "01:37:44-02:02:30",
      "01:30:59-01:53:29"]))
