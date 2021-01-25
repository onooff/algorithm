day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m, d = map(int, input().split())

tmp = 0
for i in range(1, m):
    tmp += month_days[i]
tmp += d

print(day[tmp % 7])
