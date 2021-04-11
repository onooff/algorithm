import itertools
import copy


def solution(expression):
    sp = list()
    oper = set()
    last = 0
    for i in range(len(expression)+1):
        if i == len(expression):
            sp.append(int(expression[last:i]))
            break
        if not str.isdigit(expression[i]):
            sp.append(int(expression[last:i]))
            sp.append(expression[i])
            oper.add(expression[i])
            last = i+1
    print(sp)
    print(oper)

    perm = list(itertools.permutations(oper))

    max_val = -1
    exp = list()
    for p in perm:
        exp = copy.deepcopy(sp)
        for o in p:
            tmp = list()
            while len(exp) > 0:
                e = exp.pop(0)
                if e == o:
                    n1 = tmp.pop()
                    n2 = exp.pop(0)
                    if e == '+':
                        e = n1+n2
                    elif e == '-':
                        e = n1-n2
                    elif e == '*':
                        e = n1*n2
                tmp.append(e)
            exp = tmp
        # print(exp)
        max_val = max(max_val, abs(exp[0]))
    return max_val


print(solution(	"100-200*300-500+20"))
