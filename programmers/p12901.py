def solution(a, b):
    mDay = [-1, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']  # 금토일월화수목
    return day[(sum(mDay[1:a])+b) % 7]


print(solution(1, 1))
print(solution(5, 24))
