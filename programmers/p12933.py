def solution(n):
    l = []
    while n > 0:
        l.append(str(n % 10))
        n = n//10
    l.sort(reverse=True)
    answer = "".join(l)
    return int(answer)


print(solution(312213))
