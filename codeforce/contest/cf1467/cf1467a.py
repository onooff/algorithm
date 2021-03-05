t = int(input())

for tc in range(t):
    n = int(input())

    if n == 1:
        print(9)
    elif n == 2:
        print(98)
    else:
        n -= 2
        print(98, end='')
        num = 9
        for i in range(n):
            print(num, end='')
            num = (num+1) % 10
        print()
