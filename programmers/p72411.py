import itertools


def solution(orders, course):
    answer = set()
    cd = dict()
    for c_num in course:
        cd.setdefault(c_num, set())
    set_orders = list()
    for o in orders:
        o = list(o)
        for c_num in course:
            if len(o) >= c_num:
                tmp = list(itertools.combinations(o, c_num))
                for t in tmp:
                    cd[c_num].add(t)
        set_orders.append(set(o))
    # print(cd)
    for c_num in course:
        max_cnt = -1
        ans = list()
        for comb in cd[c_num]:
            comb = set(comb)
            cnt = 0
            for o in set_orders:
                if comb.issubset(o):
                    cnt += 1
            if cnt >= 2:
                # print(cnt)
                if cnt > max_cnt:
                    ans = list()
                    max_cnt = cnt
                if cnt == max_cnt:
                    ans.append(comb)
        # print(ans)
        for a in ans:
            a = list(a)
            a.sort()
            answer.add(''.join(a))
    answer = list(answer)
    answer.sort()
    # print(set_orders)
    return answer


'''
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
'''

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
