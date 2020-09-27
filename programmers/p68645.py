def solution(n):
    size = sum(range(1, n+1))
    ret = [0]*size
    index = 0
    memo = 0
    for i in range(1, size+1):
        ret[index] = i
        index += i
    return size


print(solution(5))
