n = list(input())
z = n.count('0')
ans = 'YES'
if z >= 2:
    pass
elif z == 1 or len(n) <= 1:
    ans = 'NO'
else:
    l = 0
    r = len(n)-1
    a = int(n[l])
    b = int(n[r])
    while l < r:
        if a < b:
            l += 1
            if l == r:
                break
            a *= int(n[l])
        else:
            r -= 1
            if l == r:
                break
            b *= int(n[r])
    if a != b:
        ans = 'NO'
print(ans)
