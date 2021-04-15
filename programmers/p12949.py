def solution(arr1, arr2):
    answer = list()
    for i in range(len(arr1)):
        answer.append(list())
        for j in range(len(arr2[0])):
            tmp = 0
            for d in range(len(arr1[0])):
                tmp += arr1[i][d]*arr2[d][j]
            answer[i].append(tmp)
    return answer


print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
print('[[15, 15], [15, 15], [15, 15]]')
