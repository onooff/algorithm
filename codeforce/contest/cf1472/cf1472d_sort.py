import heapq

t = int(input())

for tc in range(t):
    n = int(input())
    board = list(map(int, input().split()))
    a = 0
    b = 0
    board.sort()
    # print(board)

    is_a_turn = True
    while len(board) > 0:
        tmp = board.pop(len(board)-1)
        if is_a_turn:
            if tmp % 2 == 0:
                a += tmp
        else:
            if tmp % 2 == 1:
                b += tmp
        is_a_turn = not is_a_turn
    # print('>>>', a, b)
    if a > b:
        print('Alice')
    elif b > a:
        print('Bob')
    else:
        print('Tie')
