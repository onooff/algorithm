import math
n = int(input())
l = [-1 for _ in range(n+1)]
sq = list()
for i in range(int(math.sqrt(n))+1):
    sq.append(i*i)
    l[sq[i]] = 1

sq_idx = -1
for i in range(n+1):
    if l[i] < 0:
        l[i] = l[i-1]+1
        for j in range(sq_idx, 2, -1):
            l[i] = min(l[i], l[i-sq[j]]+1)
    else:
        sq_idx += 1

print(l[n])
