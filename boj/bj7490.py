import sys

inputs = sys.stdin.readlines()

signs = [" ", "+", "-"]
exp = ["1"]
ans = list()


def dfs(num, summ, lim):
    cur = abs(num) % 10 + 1
    # print(exp, num, summ, lim, cur)
    if cur > lim:
        summ += num
        if summ == 0:
            ans.append("".join(exp))
        return

    for i in range(len(signs)):
        if i == 0:
            exp.append(" ")
            exp.append(str(cur))
            if num > 0:
                dfs(num * 10 + cur, summ, lim)
            else:
                dfs(num * 10 - cur, summ, lim)
        elif i == 1:
            exp.append("+")
            exp.append(str(cur))
            dfs(cur, summ + num, lim)
        else:
            exp.append("-")
            exp.append(str(cur))
            dfs(-cur, summ + num, lim)
        exp.pop()
        exp.pop()


for i in range(1, len(inputs)):
    n = int(inputs[i])
    ans = list()
    dfs(1, 0, n)
    ans.append("")
    print("\n".join(ans))
