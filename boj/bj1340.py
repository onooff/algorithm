month_dict = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12
}
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

exp = input().split()
month = month_dict[exp[0]]
day = int(exp[1][:-1])
year = int(exp[2])
h = int(exp[3][:2])
m = int(exp[3][-2:])
# print(year, month, day, h, m)
d = 525600
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    d += 1440
    days[2] += 1
fast = sum(days[:month])*1440
fast += (day-1)*1440
fast += h*60
fast += m
print(fast/d*100)
