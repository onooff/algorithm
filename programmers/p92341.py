import math


def solution(fees, records):
    d = dict()
    dd = dict()
    for r in records:
        time, car_num, status = r.split()
        h, m = map(int, time.split(":"))
        time = h*60+m
        car_num = int(car_num)
        if status == 'IN':
            d[car_num] = time
        else:
            dd.setdefault(car_num, 0)
            dd[car_num] += time-d.pop(car_num)
    for car_num in list(d.keys()):
        dd.setdefault(car_num, 0)
        dd[car_num] += 1439-d.pop(car_num)
    answer = list()
    for k in sorted(dd.keys()):
        t = dd[k]
        t -= fees[0]
        fee = fees[1]
        if t > 0:
            fee += math.ceil(t/fees[2])*fees[3]
        answer.append(fee)
    return answer


print(solution([120, 0, 60, 591], ["16:00 3961 IN", "16:00 0202 IN",
      "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]))
