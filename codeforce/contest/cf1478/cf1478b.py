t = int(input())

for tc in range(t):
    n, lucky = map(int, input().split())
    l = list(map(int, input().split()))
    for num in l:
        while True:
            if num < 0:
                print('no')
                break
            else:
                if str(num).find(str(lucky)) != -1:
                    print('yes')
                    break
                else:
                    num -= lucky
