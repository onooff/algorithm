def solution(x):
    xSum = 0
    for c in str(x):
        xSum += int(c)
    if x % xSum == 0:
        return True
    else:
        return False
