# N개의 최소공배수

def solution(arr):
    answer = 1
    f = list()
    for n in arr:
        tmp = dict()
        d = 2
        while n != 1:
            if n % d == 0:
                if d not in tmp:
                    tmp.setdefault(d, 0)
                tmp[d] += 1
                n //= d
            else:
                d += 1
        f.append(tmp)
    print(f)

    ans = dict()
    for i in f:
        for d in i:
            if d not in ans:
                ans.setdefault(d, i[d])
            else:
                ans[d] = max(ans[d], i[d])

    for a in ans:
        answer *= (a**ans[a])

    return answer


print(solution([2, 6, 8, 14]))
