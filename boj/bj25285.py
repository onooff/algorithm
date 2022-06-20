n = int(input())
for _ in range(n):
    h, w = map(int, input().split())
    bmi = w/((h/100)**2)
    grade = -1
    if h < 140.1:
        grade = 6
    elif h < 146:
        grade = 5
    elif h < 159:
        grade = 4
    elif h < 161:
        if 16 <= bmi <= 35:
            grade = 3
        else:
            grade = 4
    elif h < 204:
        if 20 <= bmi < 25:
            grade = 1
        elif 18.5 <= bmi < 20 or 25 <= bmi < 30:
            grade = 2
        elif 16 <= bmi < 18.5 or 30 <= bmi < 35:
            grade = 3
        else:
            grade = 4
    else:
        grade = 4
    print(grade)
