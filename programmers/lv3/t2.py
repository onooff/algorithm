def solution(a):
    answer = 0
    lmin = 9999999999
    rmin = 9999999999

    aa = list()
    for i in range(len(a)):
        aa.append([a[i], 0, 0])
        lmin = min(lmin, a[i])
        aa[i][1] = lmin
    for i in range(len(a)-1, -1, -1):
        rmin = min(rmin, a[i])
        aa[i][2] = rmin

    for t in aa:
        if (t[0] <= t[1]) | (t[0] <= t[2]):
            answer += 1

    # print(aa)

    return answer


print(solution(	[9, -1, -5]))
