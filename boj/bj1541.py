s = input()

ans = 0
tmp = 0
flag = 1
for c in list(s):
    if c.isdigit():
        tmp = tmp*10+int(c)
    else:
        ans += tmp*flag
        tmp = 0
        if c == '-':
            flag = -1
print(ans+tmp*flag)
