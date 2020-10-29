def solution(n):
    samjin = ""
    while n > 0:
        samjin = str(n % 3)+samjin
        n //= 3

    return int(''.join(reversed(samjin)), 3)


print(solution(45))
