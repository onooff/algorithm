def solution(arr1, arr2):
    answer = list()
    for i in range(len(arr1)):
        answer.append(list())
        for j in range(len(arr1[i])):
            answer[i].append(arr1[i][j]+arr2[i][j])
    return answer


print(solution([[1], [2]], [[3], [4]]))
