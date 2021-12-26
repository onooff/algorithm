lim = 10000
x, y, p1, p2 = map(int, input().split())
cur_x = p1
cur_y = p2
while cur_x < lim and cur_y < lim and cur_x != cur_y:
    if cur_x < cur_y:
        cur_x += x
    else:
        cur_y += y
if cur_x == cur_y:
    print(cur_x)
else:
    print(-1)
