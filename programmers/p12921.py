def solution(n):
    numbers = list(range(n+1))
    numbers[0] = -1
    numbers[1] = -1
    for num in numbers:
        if num == -1:
            continue
        else:
            nnum = num*2
            while nnum <= n:
                numbers[nnum] = -1
                nnum += num
    count = 0
    for num in numbers:
        if num == -1:
            continue
        else:
            count += 1
    return count


print(solution(100))
