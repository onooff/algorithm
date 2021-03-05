t = int(input())
for tc in range(t):
    n = int(input())
    s = input()
    cnt = 0
    for i in range(n-1, -1, -1):
        if s[i] != ')':
            break
        else:
            cnt += 1
    # print(cnt)
    if n-cnt < cnt:
        print('Yes')
    else:
        print('No')
