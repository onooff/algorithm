n = int(input())
t = 1
l = [1]
for i in range(n):
    a, b = map(int, input().split())
    for j in range(a):
        t += 1
        tmp = list()
        tmp.append(l[0])
        for k in range(1, t-1):
            tmp.append(l[k]+l[k-1])
        tmp.append(l[t-2])
        # print('>>>', tmp)
        l = tmp

    for j in range(b):
        t -= 1
        tmp = list()
        for k in range(t):
            tmp.append(l[k]+l[k+1])
        # print('>>>', tmp)
        l = tmp
print(sum(l))
