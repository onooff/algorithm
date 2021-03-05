t = int(input())
for tc in range(t):
    l = list(map(int, input().split()))
    s = sum(l)
    if s % 9 == 0 and s//9 <= min(l):
        print('YES')
    else:
        print('NO')
