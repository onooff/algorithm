# 직전 달의 말일 날짜를 출력
day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
n = int(input())
for _ in range(n):
    y, m = map(int, input().split())
    ay, am = y, m-1
    d = 0
    if m == 1:
        ay -= 1
        am = 12
    elif m == 3:
        if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
            d = 1
    print(ay, am, day[am]+d)
