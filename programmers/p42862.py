maxV = 0
students = list()


def solution(n, lost, reserve):
    global maxV, students
    students = [1]*n
    maxV = n
    for s in lost:
        students[s-1] -= 1
        maxV -= 1
    for s in reserve:
        students[s-1] += 1
        if students[s-1] == 1:
            maxV += 1

    # print(students, n)
    go(maxV)
    return maxV


def go(count):
    global maxV, students
    # print(students, count)
    for i in range(len(students)):
        if maxV == len(students):
            break
        if students[i] == 0:
            if i != 0 and students[i-1] == 2:
                students[i] = 1
                students[i-1] = 1
                go(count+1)
                students[i-1] = 2
                students[i] = 0

            if i != len(students)-1 and students[i+1] == 2:
                students[i] = 1
                students[i+1] = 1
                go(count+1)
                students[i+1] = 2
                students[i] = 0

    maxV = max(maxV, count)


print(solution(	5, [2, 4], [1, 3, 5]))
# print(solution(	5, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))
