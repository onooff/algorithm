def solution(arr):
    answer = [arr[0]]
    for n in arr:
        if answer[len(answer)-1] != n:
            answer.append(n)
    return answer


print(solution(	[1, 1, 3, 3, 0, 1, 1]))
