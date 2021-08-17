t = int(input())
for tc in range(t):
    n = int(input())
    # n = tc
    n -= 1
    n %= 28

    reverse = False
    if n-15 >= 0:
        n -= 15
        reverse = True
    n += 1

    ans = "{0:b}".format(n).zfill(4)
    for c in ans:
        if c == '0':
            if reverse:
                print("딸기", end='')
            else:
                print('V', end='')
        else:
            if reverse:
                print('V', end='')
            else:
                print("딸기", end='')

    print()
