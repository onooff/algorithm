def solution(n):
    answer = ''
    while n > 0:
        m = n % 3
        if m == 1:
            answer = '1'+answer
        elif m == 2:
            answer = '2'+answer
        elif m == 0:
            answer = '4'+answer
        n = (n-1)//3
    return answer
