import sys
input = sys.stdin.readline

t = int(input())

for tc in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    is_yes = True
    for num in l:
        if num % 2 == 1:
            print('no')
            break
    if not is_yes:
        break

    