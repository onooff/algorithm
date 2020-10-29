import datetime


def solution(n, customer):
    parseCustomer = list()
    for c in customer:
        tmp = c.split(" ")
        day = tmp[0].split("/")
        time = tmp[1].split(":")
        parseCustomer.append([datetime.datetime(
            1991, int(day[0]), int(day[1]), int(time[0]), int(time[1]), int(time[2])).timestamp(), int(tmp[2])*60])
    minTime = min(parseCustomer, key=lambda x: x[0])[0]
    for p in parseCustomer:
        p[0] = int(p[0]-minTime)
    print(parseCustomer)
    # , 자기가 몇번인지=인덱스,현재 사용자 있는지, 남은시간, 몇초놀았는지
    kiosksUse = [False]*n
    kiosksRemain = [0]*n
    kiosksIdle = [0]*n
    kiosksCount = [0]*n
    next = 0
    now = 0
    for c in parseCustomer:
        if False not in kiosksUse:
            workTime = max(c[0]-now, min(kiosksRemain))
        else:
            workTime = c[0]-now

        for i in range(n):
            kiosksRemain[i] -= workTime
            if kiosksRemain[i] <= 0:
                kiosksUse[i] = False
                kiosksIdle[i] -= kiosksRemain[i]
                kiosksRemain[i] = 0

        maxIdle = -1
        for i in range(n):
            if (kiosksUse[i] == False) and (kiosksIdle[i] > maxIdle):
                maxIdle = kiosksIdle[i]
                next = i

        print(kiosksUse)
        kiosksRemain[next] = c[1]
        kiosksCount[next] += 1
        kiosksUse[next] = True
        print(next+1)

    return max(kiosksCount)


print(solution(3, ["10/01 23:20:25 30", "10/01 23:25:50 26", "10/01 23:31:00 05", "10/01 23:33:17 24",
                   "10/01 23:50:25 13", "10/01 23:55:45 20", "10/01 23:59:39 03", "10/02 00:10:00 10"]))

'''
다음손님오는시간까지 작업돌리고
손님받을 키오스크 정하고 
손님받고
'''
