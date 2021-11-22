a, b = input().split()

maxx = -9999999999
for i in range(len(b)-len(a)+1):
    cnt = 0
    for j in range(len(a)):
        if b[i+j] == a[j]:
            cnt += 1
    maxx = max(maxx, cnt)
    if maxx == len(a):
        break
print(len(b)-(len(b)-len(a)+maxx))
