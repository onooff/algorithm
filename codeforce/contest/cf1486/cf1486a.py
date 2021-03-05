t = int(input())

for tc in range(t):
    n = int(input())
    h = list(map(int, input().split()))

    remain = 0
    idx = 0
    is_no = False
    for num in h:
        num += remain
        if num-idx < 0:
            is_no = True
            break
        else:
            remain = num-idx
            idx += 1
    if is_no:
        print('no')
    else:
        print('yes')
