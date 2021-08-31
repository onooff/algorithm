import sys
import datetime
input = sys.stdin.readline

n, info, f = input().split()
n, f = int(n), int(f)
rp = 0
info = info.split('/')
rp += int(info[0])*1440
info = info[1].split(':')
rp += int(info[0])*60
rp += int(info[1])

dic = dict()
fdic = dict()
for i in range(n):
    log = input().split()
    date = list(map(int, log[0].split('-')))
    time = list(map(int, log[1].split(':')))
    dt = datetime.datetime(date[0], date[1], date[2], time[0], time[1], 0, 0)
    dic.setdefault(log[3], dict())
    if log[2] in dic[log[3]]:
        p = dt - dic[log[3]].pop(log[2])
        chk = (p.days*1440 + p.seconds//60)-rp
        if chk > 0:
            fdic.setdefault(log[3], 0)
            fdic[log[3]] += chk*f
    else:
        dic[log[3]].setdefault(log[2], dt)

keys = list(fdic.keys())
if len(keys) == 0:
    print(-1)
else:
    keys.sort()
    for k in keys:
        print(k, fdic[k])
