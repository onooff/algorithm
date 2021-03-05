t = int(input())

for tc in range(t):
    n, d = map(int, input().split())
    l = list(map(int, input().split()))

    l.sort()

    if l[n-1] <= d:
        print('yes')
    else:
        if l[0]+l[1] <= d:
            print('yes')
        else:
            print('no')
