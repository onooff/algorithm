answer = 0
need = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]


def go(k, n):
    global answer, need
    for i in range(10):
        if(k-need[i]) == 0:
            answer += 1
        else:
            if (n == 1) & (i == 0):
                pass
            elif (k-need[i]) > 0:
                go(k-need[i], n+1)


def solution(k):
    global answer, need
    go(k, 1)
    return answer


for j in range(1, 51):
    answer = 0
    solution(j)
    print('['+str(j)+','+str(answer)+']')
