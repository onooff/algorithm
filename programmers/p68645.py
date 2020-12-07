def solution(n):
    answer = []

    tmp = []
    for i in range(1, n+1):
        tmp.append([1]*i)

    count = 1
    for j in range(n//2):
        for i in range(j*2, n-1-j):
            tmp[i][j] = count
            count += 1
        for i in range(j, n-j*2):
            tmp[n-1-j][i] = count
            count += 1
        for i in range(n-2-j, j*2, -1):
            tmp[i][i-j] = count
            count += 1
    # print(tmp)
    for i in range(len(tmp)):
        for j in range(len(tmp[i])):
            answer.append(tmp[i][j])

    return answer


print(solution(1))
