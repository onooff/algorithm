input()
exp = list(map(int, input().split()))
input()
num_pool = list(map(int, input().split()))
num_pool_set = set(num_pool)

memo = dict()


def chk(num, num_pool_set, lenn):
    global memo
    num = str(num)
    if len(str(num)) != lenn:
        return False
    if num not in memo:
        result = True
        for n in num:
            if int(n) not in num_pool_set:
                result = False
                break
        memo.setdefault(num, result)
    return memo[num]


def dfs(exp, num_pool, num_pool_set, cur, num):
    if cur == exp[0]+exp[1]:
        a = 0
        for i in range(exp[0]):
            a *= 10
            a += num[i]
        summ = 0

        idx = -1
        d = 1
        for i in range(exp[0], len(num)):
            idx += 1
            tmp = a*num[i]
            if not chk(tmp, num_pool_set, exp[-(2+idx)]):
                return 0
            summ += tmp*d
            d *= 10
        if chk(summ, num_pool_set, exp[-1]):
            # print(summ, num)
            return 1
        else:
            return 0
    ans = 0
    for n in num_pool:
        num[cur] = n
        ans += dfs(exp, num_pool, num_pool_set, cur+1, num)
    return ans


num = [0 for i in range(exp[0]+exp[1])]
print(dfs(exp, num_pool, num_pool_set, 0, num))
