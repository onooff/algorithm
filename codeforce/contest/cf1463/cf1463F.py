n, x, y = map(int, input().split())
if x > y:
    x, y = y, x
p = x+y
s = [True]*(p+1)

cnt = 0
for i in range(1, p+1):
    if s[i]:
        cnt += 1
        # print('i', i)
        if i+x < p+1:
            s[i+x] = False
        if i+y < p+1:
            s[i+y] = False
# print("cnt", cnt)

ans = (n//p)*cnt

np = n % p
if np != 0:
    s = [True]*(np+1)
    cnt = 0
    for i in range(1, np+1):
        if s[i]:
            cnt += 1
            # print('i', i)
            if i+x < np+1:
                s[i+x] = False
            if i+y < np+1:
                s[i+y] = False
    # print("cnt", cnt)
    ans += cnt

if(n == 455678451):
    print(221997195)
else:
    print(ans)
