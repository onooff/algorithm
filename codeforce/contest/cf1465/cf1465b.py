t = int(input())
for tc in range(t):
    s = input()
    n = int(s)

    is_fair = False
    while not is_fair:
        is_fair = True
        for d in list(str(n)):
            # print(d)
            if d == '0':
                pass
            elif n % int(d) != 0:
                is_fair = False
                n += 1
                break
    print(n)
