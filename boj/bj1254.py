def f(s, l, r):
    ret = True
    while l > -1 and r < len(s):
        if s[l] != s[r]:
            ret = False
            break
        l -= 1
        r += 1
    return ret


s = input()

l = len(s)//2
if len(s) % 2 == 0:
    l -= 1
    r = l+1
else:
    r = l

while r < len(s):
    if f(s, l, r):
        break
    if l < r:
        l += 1
    else:
        r += 1

answer = l*2+1
if l != r:
    answer += 1
print(answer)
