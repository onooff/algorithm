n, x = map(int, input().split())
l = list(map(int, input().split()))

summ = sum(l[:x])
maxx = summ
cnt = 1
for i in range(x, len(l)):
    summ += l[i] - l[i - x]
    if summ > maxx:
        cnt = 1
        maxx = summ
    elif summ == maxx:
        cnt += 1
if maxx == 0:
    print("SAD")
else:
    print(maxx)
    print(cnt)
