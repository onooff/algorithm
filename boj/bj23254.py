n, m = map(int, input().split())
point = list(map(int, input().split()))
study_get = list(map(int, input().split()))
d = dict()
summ = 0
for i in range(m):
    summ += point[i]
    a, b = (100-point[i]) // study_get[i], (100-point[i]) % study_get[i]
    d.setdefault(study_get[i], 0)
    d[study_get[i]] += a
    d.setdefault(b, 0)
    d[b] += 1

maxx = list(d.keys())
maxx.sort(key=lambda x: -x)
i = 0
t = n*24
while t > 0 and i < len(maxx) and maxx[i] > 0:
    if t >= d[maxx[i]]:
        t -= d[maxx[i]]
        summ += maxx[i]*d[maxx[i]]
        i += 1
    else:
        summ += maxx[i]*t
        break

print(summ)
