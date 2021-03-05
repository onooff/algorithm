n, x, y = map(int, input().split())
if x > y:
    x, y = y, x
p = n
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

for i in range(len(s)):
    print(s[i])
