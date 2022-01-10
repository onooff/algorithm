import sys
def input(): return sys.stdin.readline().rstrip()


def next_person(cur, n):
    if cur == 0:
        return n-1
    return cur-1


sq = 0
while True:
    n = int(input())
    if n == 0:
        break
    sq += 1
    print('Group', sq)
    data = list()
    for i in range(n):
        data.append(input().split())
    nobody = True
    for i in range(n):
        chk = next_person(i, n)
        for j in range(1, n):
            if data[i][j] == 'N':
                nobody = False
                print(data[chk][0], 'was nasty about', data[i][0])
            chk = next_person(chk, n)
    if nobody:
        print('Nobody was nasty')
    print()
