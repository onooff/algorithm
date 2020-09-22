from itertools import *


def solution(orders, course):
    answer = []

    orderlist = []
    menuset = set()
    for o in orders:
        # print(o)
        orderlist.append(set())
        for c in o:
            # print(c)
            orderlist[len(orderlist)-1].add(c)
            menuset.add(c)
    # print(menuset)
    # print(orderlist)

    for n in course:
        # check = list(combinations(menuset, n))
        check = set()

        for o in orderlist:
            for wow in list(combinations(o, n)):
                temp = list(wow)
                temp.sort()
                check.add(tuple(temp))
        check = list(check)
        # print("와이라노", check)

        checkdict = dict()
        maxv = -1
        for c in check:
            checkdict[c] = 0
            for o in orderlist:
                if set(c).issubset(o):
                    checkdict[c] += 1
            maxv = max(maxv, checkdict[c])
        if maxv >= 2:
            for key in checkdict:
                if checkdict[key] == maxv:
                    temp = list(key)
                    temp.sort()
                    # temp = "".join(temp)
                    # print(temp)
                    answer.append("".join(temp))

    answer.sort()
    return answer


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(	["XYZ", "XWY", "WXA"], [2, 3, 4]))
