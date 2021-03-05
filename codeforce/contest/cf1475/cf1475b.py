t = int(input())

for tc in range(t):
    n = int(input())
    if n//2020 >= n % 2020:
        print('yes')
    else:
        print('no')
