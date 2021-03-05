import heapq

t = int(input())

for tc in range(t):
    n = int(input())
    board = list(map(int, input().split()))

    odds = list()
    evens = list()
    for n in board:
        if n % 2 == 1:
            heapq.heappush(odds, -n)
        else:
            heapq.heappush(evens, -n)

    a = 0  # even
    b = 0  # odd
    while not(len(odds) == 0 and len(evens) == 0):
        if len(odds) > 0 and len(evens) > 0:
            if evens[0] > odds[0]:
                heapq.heappop(odds)
            else:
                a += heapq.heappop(evens)

            if len(odds) > 0 and len(evens) > 0:
                if odds[0] > evens[0]:
                    heapq.heappop(evens)
                else:
                    b += heapq.heappop(odds)
            else:
                if len(odds) > 0:
                    b += heapq.heappop(odds)
                else:
                    heapq.heappop(evens)
        else:
            if len(odds) > 0:
                heapq.heappop(odds)
                if len(odds) > 0:
                    b += heapq.heappop(odds)
            else:
                a += heapq.heappop(evens)
                if len(evens) > 0:
                    heapq.heappop(evens)
    # print('>>>', a, b)
    if a < b:
        print('Alice')
    elif b < a:
        print('Bob')
    else:
        print('Tie')
