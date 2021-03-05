n, x, y = map(int, input().split())
if x > y:
    x, y = y, x
p = x+y
# s = [True]*(p+1)
for j in range(1, x):
    s = [True]*(p+1)
    ans = p
    cnt = 0
    for i in range(j, p+1):
        if s[i]:
            cnt += 1
            # print('i', i)
            if i+x < p+1:
                s[i+x] = False
                ans -= 1
            if i+y < p+1:
                s[i+y] = False
                ans -= 1
            if i+x > 0:
                s[i-x] = False
                ans -= 1
            if i+y > 0:
                s[i-y] = False
                ans -= 1
    print(cnt)
# for i in range(len(s)):
#     print(s[i])
