import heapq


def change(intstr=''):
    return -int(intstr)


t = int(input())


for tc in range(t):
    n = int(input())
    board = list(map(change, input().split()))
    a = 0
    b = 0
    heapq.heapify(board)
    # print(board)

    is_a_turn = True
    while len(board) > 0:
        tmp = heapq.heappop(board)
        if is_a_turn:
            if tmp % 2 == 0:
                a += tmp
        else:
            if tmp % 2 == 1:
                b += tmp
        is_a_turn = not is_a_turn
    # print('>>>', a, b)
    if a < b:
        print('Alice')
    elif b < a:
        print('Bob')
    else:
        print('Tie')
