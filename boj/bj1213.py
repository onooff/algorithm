chars = list(input())
chars.sort()

center = ''
cnt = 1
last = chars[0]
ans = str()
for i in range(1, len(chars)+1):
    if i == len(chars) or chars[i] != last:
        if cnt % 2 == 1 and center != '':
            ans = "I'm Sorry Hansoo"
            break
        ans += last*(cnt//2)
        if cnt % 2 == 1:
            center = last
        if i == len(chars):
            ans = ans+center+ans[::-1]
            break
        last = chars[i]
        cnt = 0
    cnt += 1
print(ans)
