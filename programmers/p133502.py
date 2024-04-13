def solution(ingredient):
    answer = 0
    stk = []

    for n in ingredient:
        if (
            n == 1
            and len(stk) >= 3
            and (stk[-1] == 3 and stk[-2] == 2 and stk[-3] == 1)
        ):
            answer += 1
            for _ in range(3):
                stk.pop()
        else:
            stk.append(n)

    return answer
