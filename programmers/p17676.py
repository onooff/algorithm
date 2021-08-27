def log_parse(line):
    line = line.split()
    time = list(map(float, line[1].split(":")))
    process = float(line[2][:-1])
    # print(time, process)
    end = (time[0]*3600+time[1]*60+time[2])*1000
    start = end - process*1000
    # print(start, end)
    return (int(start), int(end))


def solution(lines):
    start = dict()
    end = dict()
    for line in lines:
        log = log_parse(line)
        start.setdefault(log[0], 0)
        start[log[0]] += 1
        end.setdefault(log[1], 0)
        end[log[1]] += 1
    start_times = list(start.keys())
    end_times = list(end.keys())
    start_times.sort()
    end_times.sort()

    processing = 0
    max_processing = 0
    end_idx = 0
    while len(end_times) > 0:
        et = end_times.pop(0)
        end_cnt = end.pop(et)
        chk = et+999
        while len(start_times) > 0 and start_times[0] < chk:
            # st = start_times.pop(0)
            # st_cnt = start.pop(st)
            # processing += st_cnt
            # print(st, st_cnt, "개 시작")
            processing += start.pop(start_times.pop(0))
        max_processing = max(processing, max_processing)
        # print(processing, "개 연산중", chk)
        processing -= end_cnt
        # print(et, end_cnt, "개 종료")

    return max_processing
