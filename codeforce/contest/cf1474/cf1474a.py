'''
best
21212121
'''


t = int(input())
for tc in range(t):
    n = int(input())
    b = input()
    prev = -1
    ans = ''
    for bn in b:
        if int(bn)+1 != prev:
            ans += '1'
            prev = int(bn)+1
        else:
            ans += '0'
            prev = int(bn)
    print(ans)
