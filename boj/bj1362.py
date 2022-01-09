import sys
def input(): return sys.stdin.readline().rstrip()


ans_dict = {0: ':-)', 1: ':-(', 2: 'RIP'}
sq = 0
while True:
    sq += 1
    o, w = map(int, input().split())
    if o == 0 and w == 0:
        break
    ans = 1
    while True:
        command = input().split()
        if command[0] == "#":
            if o/2 < w < o*2:
                ans = 0
            elif w <= 0:
                ans = 2
            print(sq, ans_dict[ans])
            break
        elif w > 0:
            if command[0] == "F":
                w += int(command[1])
            else:
                w -= int(command[1])
