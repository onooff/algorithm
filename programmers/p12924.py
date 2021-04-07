def solution(n):
    answer = 0
    for i in range(1, (n//2)+1):
        num = i
        s = 0
        while s <= n:
            s += num
            if s == n:
                print(i)
                answer += 1
                break
            num += 1
    return answer+1
