import math

n = int(input())
l = list(map(int, input().split()))
total = int(input())

summ = sum(l)
maxx = max(l)

if summ <= total:
    print(maxx)
else:
    l.sort()
    l.pop()
    cnt = 1
    goal = summ - total  # 절감해야 하는 액수
    while len(l) > 0 and (cnt * (maxx - l[-1])) < goal:
        goal -= (maxx - l[-1]) * cnt
        maxx = l.pop()
        cnt += 1
    # print(l, maxx, cnt, goal)
    print(max(total // n, maxx - math.ceil(goal / cnt)))
