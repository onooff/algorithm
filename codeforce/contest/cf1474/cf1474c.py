import math

t = int(input())
for tc in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    d = dict()
    for num in l:
        if num not in d:
            d.setdefault(num, 0)
        d[num] += 1
    # print(d)
    ans = ['YES']
    nextn = max(d)
    if d[nextn] > 1:
        ans = 'NO'
        print(ans)
        continue
    d.pop(nextn)
    ans.append(str(nextn)+' ')
    flag = True
    while len(d) > 1:
        a = max(d)
        b = nextn-a
        if b not in d or (a == b and d[a] < 2):
            if flag == True:
                flag = False
                d[a] -= 1
                if d[a] == 0:
                    d.pop(a)
                ans[1] += str(a)
                continue
            ans = 'NO'
            break
        ans.append(str(a)+'-'+str(b))
        d[a] -= 1
        if d[a] == 0:
            d.pop(a)
        d[b] -= 1
        if d[b] == 0:
            d.pop(b)
        nextn = a
    if flag == False and len(d) > 0:
        ans = 'NO'

    if type(ans) == str:
        print(ans)
    else:
        if flag == True:
            ans[1] += str(max(d))
        print('\n'.join(ans))
