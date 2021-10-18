def solution(a, s):
    answer = list()
    last = 0
    for n in s:
        b = a[last:last+n]
        last += n
        if n == 1:
            answer.append(1)
            continue

    return
