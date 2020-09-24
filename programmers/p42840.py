def solution(answers):
    p1 = list()
    p2 = list()
    p3 = list()
    n1 = 1
    n2 = 1
    n3 = 3
    for i in range(1, 10001):
        p1.append(n1)
        n1 += 1
        if n1 == 6:
            n1 = 1

        if i % 2 == 1:
            p2.append(2)
        else:
            p2.append(n2)
            n2 += 1
            if n2 == 2:
                n2 += 1
            elif n2 == 6:
                n2 = 1

        if i % 10 == 0:
            p3.append(3)
            p3.append(3)
            p3.append(1)
            p3.append(1)
            p3.append(2)
            p3.append(2)
            p3.append(4)
            p3.append(4)
            p3.append(5)
            p3.append(5)

    cnt = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == p1[i]:
            cnt[0] += 1
        if answers[i] == p2[i]:
            cnt[1] += 1
        if answers[i] == p3[i]:
            cnt[2] += 1

    m = max(cnt)

    ret = list()
    for i in range(len(cnt)):
        if cnt[i] == m:
            ret.append(i+1)

    # print(p1)
    # print(p2)
    # print(p3)
    return ret


print(solution(	[1, 2, 3, 4, 5]))
