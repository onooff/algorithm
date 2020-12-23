n = int(input())
m = int(input())
s = list(input())

ans = 0
lenIOI = 0
is_IOIing = False
nextC = ''
for i in range(m):
    c = s[i]
    if is_IOIing:
        if c == nextC:
            if c == 'I':
                lenIOI += 1
                nextC = 'O'
            else:
                nextC = 'I'
        else:
            getIOI = lenIOI-(n-1)
            if getIOI > 0:
                ans += lenIOI-(n-1)
            lenIOI = 0
            is_IOIing = False

    if not is_IOIing:
        if c == 'I':
            nextC = 'O'
            is_IOIing = True

getIOI = lenIOI-(n-1)
if getIOI > 0:
    ans += lenIOI-(n-1)

print(ans)
