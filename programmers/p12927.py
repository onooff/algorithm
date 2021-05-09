def solution(n, works):
    answer = 0
    works.sort(key=lambda x: -x)

    while n > 0:
        first = works[0]
        if first == 0:
            break
        idx = 0
        while idx < len(works) and works[idx] == first:
            works[idx] -= 1
            n -= 1
            idx += 1
            # print(n, works)
            if n == 0:
                break
    for w in works:
        answer += w*w
    return answer


# print(solution(3, [1, 1]))
