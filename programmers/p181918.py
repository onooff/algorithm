def solution(arr):
    stk = []
    for n in arr:
        while len(stk) != 0 and stk[-1] >= n:
            stk.pop()
        stk.append(n)
    return stk
