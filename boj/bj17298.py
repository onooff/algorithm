n = int(input())
l = list(map(int, input().split()))
ans = [-1 for i in range(n)]

stk = list()
for i in range(len(l)):
    num = l[i]

    while len(stk) > 0 and l[stk[len(stk)-1]] < num:
        ans[stk.pop()] = num

    stk.append(i)
    stk_min = num


for a in ans:
    print(a, end=' ')
