n = int(input())

apple_set = set()
a = int(input())
for i in range(a):
    apple_set.add(tuple(map(int, input().split())))
turn = dict()
s = int(input())
for i in range(s):
    x, c = input().split()
    x = int(x)
    turn.setdefault(x, c)

d = ((0, 1), (1, 0), (0, -1), (-1, 0))
snake_q = [(1, 1)]
snake_set = {(1, 1)}
go = 0
time = 0
die = False
while not die:
    time += 1
    ny = snake_q[len(snake_q)-1][0]+d[go][0]
    nx = snake_q[len(snake_q)-1][1]+d[go][1]
    next_head = (ny, nx)
    if 0 >= ny or ny > n or 0 >= nx or nx > n:
        die = True
        break
    elif next_head in apple_set:
        apple_set.discard(next_head)
    else:
        if next_head in snake_set:
            die = True
            break
        snake_set.discard(snake_q.pop(0))
    snake_q.append(next_head)
    snake_set.add(next_head)
    if time in turn:
        c = turn[time]
        if c == 'D':
            go += 1
            if go == 4:
                go = 0
        else:
            go -= 1
            if go == -1:
                go = 3
    #     print("turn", go)
    # print(snake_q, time)
print(time)
