board = input()+'.'
ans = []
cnt = 0
for c in board:
    if c == '.':
        if cnt % 2 == 1:
            ans = ["-1", '']
            break
        while cnt > 0:
            if cnt < 4:
                ans.append("BB")
                cnt -= 2
            else:
                ans.append("AAAA")
                cnt -= 4
        ans.append('.')
    else:
        cnt += 1
print(''.join(ans[:-1]))
