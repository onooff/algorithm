import math
t = int(input())

for tc in range(t):
    n = int(input())
    sum_x = 0
    sum_y = 0
    list_x = list()
    list_y = list()
    for i in range(n):
        input_x, input_y = map(int, input().split())
        list_x.append(input_x)
        list_y.append(input_y)
        sum_x += input_x
        sum_y += input_y

    ans_x = set()
    ans_y = set()

    tx = sum_x/n
    ty = sum_y/n
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            nx = tx+dx
            ny = ty+dy
            ans_x.add(math.ceil(nx))
            ans_y.add(math.ceil(ny))
            ans_x.add(math.floor(nx))
            ans_y.add(math.floor(ny))

    # if sum_x > 0:
    # ans_x.add(math.ceil((sum_x/n)-1))
    # ans_x.add(math.ceil(sum_x/n))
    # ans_x.add(math.floor(sum_x/n))
    # ans_x.add(math.floor((sum_x/n)+1))
    # # if sum_y > 0:
    # ans_y.add(math.ceil((sum_y/n)-1))
    # ans_y.add(math.ceil(sum_y/n))
    # ans_y.add(math.floor(sum_y/n))
    # ans_y.add(math.floor((sum_y/n)+1))

    length = list()
    for x in ans_x:
        for y in ans_y:
            l = 0
            for i in range(n):
                l += abs(list_x[i]-x)+abs(list_y[i]-y)
            length.append(l)
    min_val = min(length)
    ans = 0
    for l in length:
        if l == min_val:
            ans += 1
    # print('>>>', ans)
    print(ans)
    print(length)
