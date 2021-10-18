# def solution(n, left, right):
#     board = [0 for i in range(n*n)]
#     for lv in range(n):
#         num = lv+1
#         for i in range(lv):
#             board[n*lv+i] = num
#             board[n*i+lv] = num
#     return board[left:right]

def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        p = i % n
        q = i // n
        if p > q:
            answer.append(p)
        else:
            answer.append(q)
    return answer
