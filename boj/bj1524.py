import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    input()
    input()
    s = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    s_idx = 0
    b_idx = 0
    while s_idx < len(s) and b_idx < len(b):
        if s[s_idx] < b[b_idx]:
            s_idx += 1
        else:
            b_idx += 1
    if s_idx == len(s):
        print('B')
    else:
        print('S')
